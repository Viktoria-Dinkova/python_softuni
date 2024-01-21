# Write a function that receives two characters and returns a single string
# with all the characters in between them (according to the ASCII code),
# separated by a single space. Print the result on the console.

def characters_between(start_char: str, last_char: str) -> list:
    '''
    return characters in interval according to the ASCII code

        :param start_char - str:
        :param last_char - str:

        :return - list:
    '''
    interval = []
    for char in range(ord(start_char) + 1, ord(last_char)):
        interval.append(chr(char))

    return ' '.join(interval)

start = input()
end = input()

print(characters_between(start, end))
