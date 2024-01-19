# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive one of the following:
# •	Opening bracket – "(",
# •	Closing bracket – ")" or
# •	Random string
# Your task is to find out if the brackets are balanced. That means after every opening bracket should follow a closing one.
# Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist,
# the expression should be marked as unbalanced. You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.
command_count = int(input())
balans = 0
for command in range(command_count):
    current_command = input()

    if current_command == '(':
        balans += 1
        if balans > 1:
            print("UNBALANCED")
            break
    elif current_command == ')':
        if balans == 0:
            print("UNBALANCED")
            break
        else:
            balans -= 1
else:
    if balans == 0:
        print('BALANCED')
    else:
        print('UNBALANCED')