"""
Create a decorator called logged. It should return the name of the function that is being called and its parameters.
It should also return the result of the execution of the function being called. See the examples for more clarification.
"""


def logged(function):
    def wrapper(*args, **kwargs):
        return f"you called {function.__name__}{args}\n" \
               f"it returned {function(*args)}"

    return wrapper



# @logged
# def func(*args):
#     return 3 + len(args)
#
#
# print(func(4, 4, 4))
