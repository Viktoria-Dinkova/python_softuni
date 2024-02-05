'''
Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m,
separated by a single space - representing the lengths of two separate sets. On the next n + m lines,
you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set.
Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}
'''

'''
Write a program that keeps all the unique chemical elements.
On the first line, you will be given a number n - the count of input lines that you will receive.
On the following n lines, you will be receiving chemical compounds separated by a single space.
Your task is to print all the unique ones on separate lines (the order does not matter):
'''

count_of_inputs = int(input())

unique_elements = set()

for _ in range(count_of_inputs):
    for elements in input().split():
        unique_elements.add(x)

print(*unique_elements, sep='\n')

#
# count_of_inputs = int(input())
#
# unique_elements = set()
#
# for _ in range(count_of_inputs):
#     elements = input().split()
#     for x in elements:
#         unique_elements.add(x)
#
# print(*unique_elements, sep='\n')