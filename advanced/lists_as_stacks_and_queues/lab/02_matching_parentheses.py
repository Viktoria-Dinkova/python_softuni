'''
You are given an algebraic expression with parentheses.
Scan through the string and extract each set of parentheses.
Print the result back on the console.
'''

expression = input()

start_index = 0
end_index = 0

stack = []

if expression.count('(') == expression.count(')'):

    for element_index in range(len(expression)):
        if expression[element_index] == '(':
            stack.append(element_index)
        elif expression[element_index] == ')':
            start_index = stack.pop()
            end_index = element_index + 1
            print(f'{expression[start_index:end_index]}')
