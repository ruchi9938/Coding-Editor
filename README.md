# Online Python Editor

A modern, feature-rich online Python editor built with Django and Monaco Editor. This project provides a web-based environment for writing, running, and testing Python code with a beautiful and intuitive interface.

## Features

- 🚀 **Modern UI**: Clean and intuitive interface inspired by VS Code
- 💻 **Advanced Code Editor**: Powered by Monaco Editor (same as VS Code)
- ✨ **Intelligent Code Completion**: Full Python keyword and function suggestions
- 📝 **Code Snippets**: Quick templates for common Python patterns
- 🔍 **Syntax Highlighting**: Advanced Python syntax highlighting
- ⌨️ **Keyboard Shortcuts**: 
  - `Ctrl + Enter`: Run code
  - `Ctrl + Space`: Trigger suggestions
- 📊 **Real-time Output**: Instant feedback for your code execution
- 🔄 **Input Handling**: Support for interactive Python programs
- 🎨 **Dark Theme**: Easy on the eyes with a modern dark theme
- 📱 **Responsive Design**: Works on desktop and mobile devices

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd codeeditor_project
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to:
```
http://localhost:8000
```

## Usage

1. **Writing Code**:
   - Use the editor to write your Python code
   - Get intelligent code completion and suggestions
   - Use snippets for common code patterns

2. **Running Code**:
   - Click the "Run" button or press `Ctrl + Enter`
   - View the output in the right panel
   - Handle program input when required

3. **Input Handling**:
   - When your program requires input, an input field will appear
   - Type your input and press Enter or click Submit
   - Cancel input if needed

## Editor Features

### Code Completion
- All Python keywords
- Built-in functions with parameter hints
- Intelligent suggestions based on context

### Snippets
- Function definitions
- Class definitions
- Control flow statements
- Exception handling
- And more...

### Keyboard Shortcuts
- `Ctrl + Enter`: Run code
- `Ctrl + Space`: Show suggestions
- `Tab`: Accept suggestion
- `Esc`: Close suggestion panel

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) - The code editor component
- [VS Code](https://code.visualstudio.com/) - Inspiration for the UI design

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository. 