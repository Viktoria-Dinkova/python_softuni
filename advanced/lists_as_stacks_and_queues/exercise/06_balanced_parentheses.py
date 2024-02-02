'''
You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.
A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs after the former.
There will be no interval symbols between the parentheses. You will be given three types of parentheses: (), {}, and [].
{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.
Input
•	On a single line, you will receive a sequence of parentheses.
Output
•	For each test case, print on a new line "YES" if the parentheses are balanced.
•	Otherwise, print "NO"

'''
from collections import deque
expresion = deque(input())

balanced = deque([])

while expresion:
    if expresion[0] == '(' or expresion[0] == '[' or expresion[0] == '{':
        balanced.append(expresion[0])
        expresion.popleft()
    else:
        if len(balanced) > 0:
            if (expresion[0] == ')' and balanced[-1] == '(') or (expresion[0] == ']' and balanced[-1] == '[') or (expresion[0] == '}' and balanced[-1] == '{'):
                balanced.pop()
                expresion.popleft()
            else:
                print('NO')
                break
        else:
            print('NO')
            break

else:
    print(f'YES')
