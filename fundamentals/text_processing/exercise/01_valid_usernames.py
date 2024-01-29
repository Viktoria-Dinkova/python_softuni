# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

usernames = input().split(', ')

def characters_is_valid(some_username: str):
    for ch in some_username:
        if (not ch.isalpha() and not ch.isdigit() and ch != '-'  and ch != '_'):
            return False
            break
    return True

for username in usernames:
    if (3 <= len(username) <= 16 and " "  not in usernames and characters_is_valid(username)):
        print(f'{username}')
