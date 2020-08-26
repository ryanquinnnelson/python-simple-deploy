import platform
import requests


# check whether runtime environment is a virtual environment
print(platform.python_version())
print(requests.__version__)

# use requests
r = requests.get('https://api.github.com/events')
print(r.status_code)


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
