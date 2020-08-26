import platform
import requests


print('Imported pythontemplatemodule!')


def get_id(name):
    """
    Returns the id associated with the given name.

    :param name: The first name of the individual
    :return: Integer
    """
    if name == "John":
        return 123
    elif name == "Jane":
        return 456
    else:
        raise ValueError("my message")


def main():
    print('Executing main method!')

    # check whether runtime environment is a virtual environment
    print('Checking whether current environment is a virtual environment...')
    print('python version: ' + platform.python_version())
    print('requests version: ' + requests.__version__)


if __name__ == '__main__':
    main()
