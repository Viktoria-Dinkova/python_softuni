import re

class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class MoreThanOneAt(Exception):
    pass

class InvalidDomainError(Exception):
    pass

class InvalidNameError(Exception):
    pass


valid_domains = ['com', 'net', 'bg', 'org']
min_name_size = 4

while True:
    email = input()

    if email == "End":
        break

    valid_name = r'^[a-zA-Z0-9._-]+'

    if "@" not in email:
        raise MustContainAtSymbolError("The emai address must contain '@' symbol")

    if email.count("@") > 1:
        raise MoreThanOneAt("The emai address must contain only one '@' symbol")

    name = email[:email.index('@')]
    if len(name) <= min_name_size:
        raise NameTooShortError("The name is too short")
    elif not re.match(valid_name, name):
        raise InvalidNameError("The name must contain only numbers, letters, '-' and '_'")

    domain = email.split('.')[-1]
    if domain not in valid_domains:
        raise InvalidDomainError("Please select domain form list below")

    print("Email is valid")

