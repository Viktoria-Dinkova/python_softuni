# you'll receive different strings n times. Your task is to check if
# the given strings do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
#
# · If a string is pure, print "{string} is pure."
# · Otherwise, print "{string} is not pure!"

number_of_strings = int(input())
string = ''
message = ''

for current_string in range(number_of_strings):
    string = input()
    if "," in string \
            or "." in string \
            or "_" in string:
        message = ' is not pure!'
    else:
        message = ' is pure.'

    print(f'{string}{message}')
