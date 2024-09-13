from setuptools import setup, find_packages

setup(
    name='file-processing-test-data',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,  # Include files specified in MANIFEST.in
    description='Test data files for file-processing libraries.',
)
