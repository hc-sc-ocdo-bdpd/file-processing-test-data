from pathlib import Path
import pkg_resources

def get_test_files_path():
    """Returns the path to the test_files directory."""
    return Path(pkg_resources.resource_filename('file_processing_test_data', 'test_files'))

def get_all_test_files():
    """Returns a list of all test files in the test_files directory."""
    test_files_path = get_test_files_path()
    return [str(f) for f in test_files_path.glob('*') if f.is_file()]
