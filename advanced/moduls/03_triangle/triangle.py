"""
Create a module for printing a triangle. You will receive an integer number which is the size of the triangle.
"""


def print_tiangle(peak):
    for t in range(1, peak + 1):
        nums = [x for x in range(1, t + 1)]
        print(*nums, sep=' ')

    for b in range(peak - 1, 0, -1):
        nums = [x for x in range(1, b + 1)]
        print(*nums, sep=' ')


print_tiangle(size)
