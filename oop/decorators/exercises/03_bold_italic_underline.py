"""
Create three decorators: make_bold, make_italic, and make_underline,
which will have to wrap a text returned from a function in <b></b>, <i></i> and <u></u> respectively.
"""


def make_underline(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function(*args)}</u>"

    return wrapper


def make_italic(function):
    def wrapper(*args, **kwargs):
        return f"<i>{function(*args)}</i>"

    return wrapper


def make_bold(function):
    def wrapper(*args, **kwargs):
        return f"<b>{function(*args)}</b>"

    return wrapper


# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"


