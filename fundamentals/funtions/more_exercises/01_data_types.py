# Write a function that, depending on the first line of the input,
# reads one of the following strings: "int", "real", or "string".
# •	If the data type is an int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is a string, surround the input with "$".
# Print the result on the console.

def data_types(command: str, incom: str):
    '''
    do somting with number, depand of command
    :param command: str
    :param number: str

    :return result
    '''
    if command == 'int':
        result = int(incom) * 2

    elif command == 'real':
        result = f'{(float(incom) * 1.5):.2f}'

    elif command == 'string':
        result = '$' + incom + '$'

    return result

user_comand = input()
user_number = input()
print(data_types(user_comand, user_number))