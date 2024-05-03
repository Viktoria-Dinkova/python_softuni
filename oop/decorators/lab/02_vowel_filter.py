"""
def vowel_filter(function):

    def wrapper():

        # TODO: Implement -> ["a", "e"]

    return wrapper

"""


def vowel_filter(function):
    def wrapper():
        strings = function()
        return [v for v in strings if v in 'ayouei']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

# print(get_letters())
