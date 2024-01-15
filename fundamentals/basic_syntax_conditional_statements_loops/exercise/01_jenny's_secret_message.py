# program that greets the user when he/she gives his/her name.
# The greeting should be in the format "Hello, {name}!".
# Jenny is in love with Johnny and would like to greet him differently: "Hello, my love!"

name = input()

if name == 'Johnny':
    name = 'my love'

print(f'Hello, {name}!')