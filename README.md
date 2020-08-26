# pythontemplate
The goal of this project is to build an example Python package using industry-standard techniques for organizing distributable code. 

## Using this package
### Installation
1. Ensure you are inside a virtual environment.
2. Install the package. The easiest method is to follow package documentation on TestPyPi or PyPi, which will provide the exact `pip` command. For ease of use, the commands are repeated in this document. *Note that TestPyPi is periodically purged, so the distribution may no longer be available there.*
    ```shell script
    $ pip install pythontemplate-rnelson5 # from PyPi 
    ```
    ```shell script
    $ pip install -i https://test.pypi.org/simple/ pythontemplate-rnelson5==0.1.0  # from TestPyPi
    ```
    ```shell script
    $ pip install -e . # from local files (if downloaded)
    ```

### Execution via Command Line
1. Ensure you are inside the same virtual environment in which you installed the package.
2. Use an entry point from the distribution's `setup.py` file, if there is one, or execute the script from the command line in the usual way.
    ```shell script
    $ run-pythontemplate  # entry point
    ```
    ```shell script
    $ python pythontemplatepackage/pythontemplatemodule.py  # usual way
    ```

### Execution via the Python Interpreter
1. Ensure you are inside the same virtual environment in which you installed the package.
2. Start your interpreter, then import the package or functions from the package to use.
    ```shell script
    $ python
    >>> from pythontemplatepackage.pythontemplatemodule import get_id
    >>> get_id('John')
    123
    ```

### Using this package inside another python project
1. Ensure you are inside the same virtual environment in which you installed the package.
2. Import the package or functions from the package to use.
    ```python
    from pythontemplatepackage.pythontemplatemodule import get_id
    ```




## Distributing this package to PyPi / TestPyPi
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

## A Project for Exploration and Learning
The project is designed to be as teachable as possible:
- Components in the project are uniquely named to help users clearly identify package components which might otherwise be confusing due to naming standards (i.e. git repository, Python package, Python module, and virtual environment are typically given the same name).
- The output of the `main()` method of the `pythontemplatemodule` module allows users to explore the concept of virtual environments. Users can maintain different versions of python and the `requests` library in their regular environment versus a virtual environment, and see how output changes depending on where code is executed.
- The `__init__.py` files print out statements whenever they are imported. This helps users understand when packages and modules are imported. 
