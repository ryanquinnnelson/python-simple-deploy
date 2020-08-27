import platform
import requests


print('Imported pythontemplatemodule!')


def get_id(name):
    """
    Returns the id associated with the given name. Throws a ValueError if the given name is not John or Jane, for the
    sake of writing a unit test example involving an exception.

    :param name: The first name of the individual
    :return: Integer
    """
    if name == "John":
        return 123
    elif name == "Jane":
        return 456
    else:
        raise ValueError("my message")


def save_id(id_number, filename):
    """
    Saves a given id in a file with the specified name. Allows for the writing of a unit test involving the temporary
    directory available in pytest.
    :param id_number:
    :param filename:
    :return:
    """
    with open(filename, 'w') as f:
        f.write(id_number)


def main():
    print('Executing main method!')

    # check whether runtime environment is a virtual environment
    print('Checking whether current environment is a virtual environment...')
    print('python version: ' + platform.python_version())
    print('requests version: ' + requests.__version__)


if __name__ == '__main__':
    main()
