from pathlib import Path
import pkg_resources

def get_test_files_path():
    """Returns the path to the test_files directory."""
    return Path(pkg_resources.resource_filename('file_processing_test_data', 'test_files'))