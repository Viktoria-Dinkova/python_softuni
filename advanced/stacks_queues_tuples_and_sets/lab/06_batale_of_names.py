'''
You will receive a number N. On the following N lines, you will be receiving names.
You should sum the ASCII values of each letter in the name and integer divide it by the number of the current row (starting from 1).
 Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even.
  After that, sum the values of each set.
•	If the sums of the two sets are equal, print the union of the values, separated by ", ".
•	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
•	If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".
NOTE: On every operation, the starting set should be the odd set
'''

inputs = int(input())

even_set = set()
odd_set = set()

for i in range(1, inputs+1):
    name_num = int(sum(ord(x) for x in input()) / i)
    if name_num % 2 == 0:
        even_set.add(name_num)
    else:
        odd_set.add(name_num)

odd_sum = sum(odd_set)
even_sum = sum(even_set)
if even_sum == odd_sum:
    print(*odd_set.union(even_set), sep=', ')
elif odd_sum > even_sum:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')

#
# inputs = int(input())
#
# even_set = set()
# odd_set = set()
#
# for i in range(1, inputs+1):
#     name = input()
#     name_num = int(sum(ord(x) for x in name) / i)
#     if name_num % 2 == 0:
#         even_set.add(name_num)
#     else:
#         odd_set.add(name_num)
#
# odd_sum = sum(odd_set)
# even_sum = sum(even_set)
# if even_sum == odd_sum:
#     add = [str(s) for s in (odd_set | even_set)]
#     print(f'{", ".join(add)}')
# elif odd_sum > even_sum:
#     diff = [str(s) for s in (odd_set - even_set)]
#     print(f'{", ".join(diff)}')
# else:
#     symmetric_diff = [str(s) for s in (odd_set ^ even_set)]
#     print(f'{", ".join(symmetric_diff)}')