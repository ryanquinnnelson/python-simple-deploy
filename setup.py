#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# sourced from https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
# sourced from https://github.com/ionelmc/python-nameless

from setuptools import find_packages
from setuptools import setup


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pythontemplate-rnelson5',
    version='0.1.0',
    author='Example Author',
    author_email='author@example.com',
    description='A small example package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ryanquinnnelson/pythontemplate',
    packages=find_packages(include=['src', 'src.*']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=['requests'],
    tests_require=['pytest'],
    entry_points={'console_scripts': ['run-pythontemplate=src.pythontemplatemodule:main']}
)
