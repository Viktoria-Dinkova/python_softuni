# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.
def find_substring(catalog: list, text: list) -> list:
    finded = []
    for serch_stamp in catalog:
        for current_word in text:
            if (serch_stamp in current_word) and (serch_stamp not in finded):
                finded.append(serch_stamp)

    return finded

catalog = list(input().split(', '))
text = list(input().split(', '))

print(f'{find_substring(catalog, text)}')