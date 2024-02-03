'''
Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.
'''
names_count = int(input())

names = set()

for _ in range(names_count):
    name = input()
    names.add(name)

print(*names, sep='\n')