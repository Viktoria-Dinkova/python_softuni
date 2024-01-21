# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"

def is_digit_or_alphabet(pass_word: str) -> bool:
    '''
    chek if each character in password is letters or digits

        :param pass_word: str

        :return message: bool
    '''
    message = True

    for char in pass_word:
        if not(48 <= ord(char) <= 57) and  not(65 <= ord(char) <= 90) and  not(97 <= ord(char) <= 122):
            message = False
            break

    return message

def miss_digits(user_pasword: str) -> bool:
    '''
    chek if there is less then two digits in the password

        :param pass_word: str

        :return message: bool
    '''
    message = True
    count = 0
    for char in user_pasword:
        if (48 <= ord(char) <= 57):
            count += 1

    if count < 2:
        message = False

    return message
def password_validator(in_password: str) -> str:
    '''
    checks if a given password is valid

        :param in_password: str

        :return: str
    '''
    if not (6 <= len(in_password) <= 10):
        print('Password must be between 6 and 10 characters')

    elif is_digit_or_alphabet(in_password) == False:
        print('Password must consist only of letters and digits')

    elif miss_digits(in_password) == False:
        print('Password must have at least 2 digits')

    else:
        print('Password is valid')

user_pass = input()
password_validator(user_pass)