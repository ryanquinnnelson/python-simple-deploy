from setuptools import setup, find_packages

setup(
    name='pythontemplatepackage-rnelson5',
    version='0.1.0',
    packages=find_packages(include=['pythontemplatepackage', 'pythontemplatepackage.*']),
    install_requires=['requests'],
    entry_points={'console_scripts': ['my-command=pythontemplatepackage.pythontemplatepackage.py:main']}
)
