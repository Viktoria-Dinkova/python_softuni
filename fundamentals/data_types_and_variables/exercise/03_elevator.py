# Calculate how many courses will be needed to elevate N persons
# by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.
from math import ceil

people = int(input())
capacity = int(input())

courses = 0

courses = ceil(people / capacity)

print(f'{courses}')