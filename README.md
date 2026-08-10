# python-utils-52

A collection of Python utility functions designed to simplify common programming tasks and enhance code efficiency. These lightweight tools can help streamline your workflow and reduce repetitive code.

## Features

- **String Manipulation**: Includes functions for advanced string formatting, casing transformations, and safe HTML encoding.
- **Data Conversion**: Tools for converting between various data formats such as JSON, CSV, and XML, ensuring compatibility across applications.
- **File Operations**: Simplified methods for reading, writing, and deleting files with built-in error handling and logging capabilities.
- **Date and Time Utilities**: Functions to handle date calculations, formatting, and timezone conversions seamlessly.

## Installation

To install the `python-utils-52` package, you can use pip. Open your terminal and run:

```bash
pip install python-utils-52
```

If you'd prefer to install the package directly from the source, clone this repository and run the setup script:

```bash
git clone https://github.com/Developer/python-utils-52.git
cd python-utils-52
python setup.py install
```

## Basic Usage

Here's a quick example to demonstrate some of the functionality available in `python-utils-52`:

```python
from utils import StringUtils, FileUtils, DateUtils

# String manipulation
formatted_string = StringUtils.capitalize_words("hello world!")

# File operations
FileUtils.write_file("example.txt", "This is a test file.")
content = FileUtils.read_file("example.txt")

# Date utility
current_time = DateUtils.get_current_time()
next_week = DateUtils.add_days(current_time, 7)

print(formatted_string)  # Output: Hello World!
print(content)           # Output: This is a test file.
print(next_week)        # Output: (current time + 7 days)
```

## License

![MIT License](https://img.shields.io/badge/license-MIT-green)  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.