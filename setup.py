from setuptools import setup, find_packages

setup(
    name='pythontemplate-rnelson5',
    version='0.1.0',
    packages=find_packages(include=['pythontemplatepackage', 'pythontemplatemodule.*']),
    install_requires=['requests'],
    entry_points={'console_scripts': ['run-pythontemplate=pythontemplatepackage.pythontemplatemodule:main']}
)
