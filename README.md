# python-i18n-showcase

A demonstration of internationalization (i18n) features in Python, showcasing multiple language support, pluralization rules, and string interpolation.

## Features

- 🌐 Multi-language support (English, Spanish, Chinese)
- 📝 Pluralization rules demonstration
- 🔄 String interpolation with variables
- 📦 Simple and clean implementation using Python i18n package

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ysskrishna/python-i18n-showcase.git
cd python-i18n-showcase
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the demonstration:
```bash
python app.py
```

This will show translations in all supported languages, demonstrating:
- Basic text translations
- Pluralization with different counts (0, 1, many)
- String interpolation with dynamic values
- Date formatting

## Project Structure

```
.
├── app.py                 # Main application file
├── translations/          # Translation files
│   ├── en.json           # English translations
│   ├── es.json           # Spanish translations
│   └── zh.json           # Chinese translations
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## Translation Examples

### Basic Translation
```python
print(i18n.t('GREETING'))
# English: "Hello"
# Spanish: "Hola"
# Chinese: "你好"
```

### Pluralization
```python
print(i18n.t('MESSAGES.ITEMS_COUNT', count=0))
print(i18n.t('MESSAGES.ITEMS_COUNT', count=1))
print(i18n.t('MESSAGES.ITEMS_COUNT', count=5))
```

### String Interpolation
```python
print(i18n.t('MESSAGES.WELCOME_USER', name='John'))
print(i18n.t('MESSAGES.FILE_INFO', filename='document.txt', date='2024-03-21'))
```

## Contributing

Contributions are welcome! Feel free to:
- Add more language support
- Improve translation structures
- Add more complex pluralization rules
- Enhance documentation

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

**Author:** [ysskrishna](https://github.com/ysskrishna)