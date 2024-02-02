'''
You have an empty stack. You will receive an integer – N. On the following N lines, you will receive queries. Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"
'''

n_queries = int(input())

stack = []

map_function = {
    '1': lambda x: stack.append(int(x[1])),
    '2': lambda x: stack.pop() if stack else None,
    '1': lambda x: max(stack) if stack else None,
    '1': lambda x: min(stack) if stack else None
}

for _ in range(n_queries):
    query = input().split()
    map_function[query[0]](query)

# stack = []
#
# for _ in range(n_queries):
#     query = input().split()
#
#     if '1' in query:
#         number = int(query[1])
#         stack.append(number)
#     elif '2' in query and len(stack) > 0:
#         stack.pop()
#     elif '3' in query and len(stack) > 0:
#         print(f'{max(stack)}')
#     elif '4' in query and len(stack) > 0:
#         print(f'{min(stack)}')
#
# while stack:
#     print(stack.pop(),end='')
#     if stack:
#         print(', ',end='')

