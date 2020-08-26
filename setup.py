"""
Follows https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
"""
from setuptools import setup, find_packages

setup(
    name='pythontemplate-rnelson5',
    version='0.1.0',
    packages=find_packages(include=['pythontemplatepackage', 'pythontemplatepackage.*']),
    install_requires=['requests'],
    entry_points={'console_scripts': ['run-pythontemplate=pythontemplatepackage.pythontemplatemodule:main']}
)
