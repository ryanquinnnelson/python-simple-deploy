# pythontemplate
A standard template for organizing python code in a git repository.

## Using this package
### Installation
1. Create and activate a virtual environment.
2. Install the package using one of several shell commands.
    ```shell script
    $ pip install pythontemplate-rnelson5  # from TestPyPi
    $ pip install -e .                     # from a local distribution
    ```
### Execution via Command Line
1. Create and activate a virtual environment?
2. Use entry point from `setup.py` file.
```shell script
$ run-pythontemplate
```

### Execution via Python Interpreter
1. Create and activate a virtual environment.
2. Start interpreter, then import package or functions to use.
```shell script
$ python
>>> from pythontemplatepackage.pythontemplatemodule import get_id
>>> get_id('John')
123
```




## Distributing this package
1. Ensure you are not inside a virtual environment.
2. Assemble a distribution using `wheel`
    ```shell script
    $ python3 setup.py sdist bdist_wheel
    ```

3. Upload the distribution using `twine`
    ```shell script
    $ python3 -m twine upload --repository testpypi dist/*
    Uploading distributions to https://test.pypi.org/legacy/
    Enter your username: __token__
    Enter your password: <TestPyPi API key>
    :
    View at:
    https://test.pypi.org/project/pythontemplate-rnelson5/0.1.0/
    ```

