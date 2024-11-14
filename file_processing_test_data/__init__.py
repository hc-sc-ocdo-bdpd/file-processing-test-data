"""
The file_processing_test_data package provides sample test files for use in testing
the file-processing suite of libraries. This package includes utilities to retrieve
the path to test files and list all available test files.

Functions:
    get_test_files_path: Returns the path to the directory containing test files.
    get_all_test_files: Returns a list of all test files in the test_files directory.
"""

from pathlib import Path
import pkg_resources

def get_test_files_path():
    """
    Returns the path to the test_files directory.

    This function locates the directory containing test files, which can be used
    for testing and development with the file-processing suite.

    Returns:
        Path: Path object pointing to the test_files directory.
    """
    return Path(pkg_resources.resource_filename('file_processing_test_data', 'test_files'))

def get_all_test_files():
    """
    Returns a list of all test files in the test_files directory.

    This function gathers all files in the test_files directory, providing a list
    of file paths for use in automated tests.

    Returns:
        list: A list of file paths (as strings) for all files in the test_files directory.
    """
    test_files_path = get_test_files_path()
    return [str(f) for f in test_files_path.glob('*') if f.is_file()]
