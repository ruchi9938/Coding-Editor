import subprocess
import json
import os
import tempfile
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

@ensure_csrf_cookie
def index(request):
    return render(request, 'editor/index.html')

@require_http_methods(["POST"])
def run_code(request):
    try:
        data = json.loads(request.body)
        code = data.get('code')
        inputs = data.get('inputs', [])
        
        if not code:
            return JsonResponse({'output': 'Error: No code provided', 'status': 'error'}, status=400)

        # Create a temporary file with a .py extension
        with tempfile.NamedTemporaryFile(suffix='.py', mode='w', delete=False) as temp_file:
            # Wrap the code to handle input properly
            wrapped_code = '''
import sys
from io import StringIO

# Store original stdin
original_stdin = sys.stdin

# Create a custom stdin that handles input properly
class CustomStdin:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0
        self.buffer = StringIO()
    
    def readline(self):
        if self.index < len(self.inputs):
            value = self.inputs[self.index]
            self.index += 1
            return value + '\\n'
        raise EOFError()

    def read(self):
        if self.index < len(self.inputs):
            value = self.inputs[self.index]
            self.index += 1
            return value
        raise EOFError()

# Set up custom stdin
custom_stdin = CustomStdin({})
sys.stdin = custom_stdin

try:
{}
except EOFError:
    print("\\nWaiting for input...", end='', flush=True)
    sys.exit(0)  # Exit with success to indicate we need input
except Exception as e:
    print(f"Error: {{str(e)}}", file=sys.stderr)
finally:
    # Restore original stdin
    sys.stdin = original_stdin
'''.format(repr(inputs), '    ' + code.replace('\n', '\n    '))
            temp_file.write(wrapped_code)
            temp_file_path = temp_file.name

        try:
            # Execute the code with input handling
            process = subprocess.Popen(
                ['python', temp_file_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Get output and errors
            stdout, stderr = process.communicate(timeout=10)  # 10 second timeout

            # If there's error output, return it
            if stderr:
                return JsonResponse({
                    'output': stderr,
                    'status': 'error',
                    'needsInput': False
                })
            
            # Check if the program is waiting for input
            if process.returncode == 0 and "Waiting for input..." in stdout:
                # Remove the "Waiting for input..." message and any trailing whitespace
                clean_output = stdout.replace("Waiting for input...", "").strip()
                return JsonResponse({
                    'output': clean_output,
                    'status': 'success',
                    'needsInput': True
                })

            # Return the output
            return JsonResponse({
                'output': stdout,
                'status': 'success',
                'needsInput': False
            })

        except subprocess.TimeoutExpired:
            return JsonResponse({
                'output': 'Error: Code execution timed out (10 second limit)',
                'status': 'error',
                'needsInput': False
            }, status=408)
        except Exception as e:
            return JsonResponse({
                'output': f'Error: {str(e)}',
                'status': 'error',
                'needsInput': False
            }, status=500)
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

    except json.JSONDecodeError:
        return JsonResponse({
            'output': 'Error: Invalid JSON in request',
            'status': 'error',
            'needsInput': False
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'output': f'Error: {str(e)}',
            'status': 'error',
            'needsInput': False
        }, status=500)
