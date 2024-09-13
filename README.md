# file-processing-test-data

This repository contains test files for use with the file-processing suite of libraries, such as `file-processing-ocr` and `file-processing-transcription`. It provides a collection of sample files to facilitate testing and development.

## Installation

You can install this package directly from the GitHub repository using pip:

```bash
pip install git+https://github.com/hc-sc-ocdo-bdpd/file-processing-test-data.git@main
```

# Usage

To access the test files in your code:

```python
from file_processing_test_data import get_test_files_path

test_files_path = get_test_files_path()
sample_file = test_files_path / 'sample_image.jpg'
```

Now you can use `sample_file` in your tests or processing code.