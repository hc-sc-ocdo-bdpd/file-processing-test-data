# file-processing-test-data

This repository contains test files for use with the file-processing suite of libraries, such as `file-processing-ocr` and `file-processing-transcription`. It provides a collection of sample files to facilitate testing and development.

## Installation

You can install this package directly from the GitHub repository using pip:

```bash
pip install git+https://github.com/hc-sc-ocdo-bdpd/file-processing-test-data.git@main
```

## Usage

To access the test files in your code:

```python
from file_processing_test_data import get_test_files_path, get_all_test_files

# Get the path to the test files directory
test_files_path = get_test_files_path()
sample_file = test_files_path / 'sample_image.jpg'

# Get a list of all test files
all_test_files = get_all_test_files()
```

- `get_test_files_path()`: Returns the path to the directory containing the test files, allowing you to specify individual files within that directory.
- `get_all_test_files()`: Returns a list of all file paths (as strings) in the `test_files` directory, useful for batch testing or loading all test files at once.

Now you can use `sample_file` or `all_test_files` in your tests or processing code.
