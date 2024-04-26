"""
Create a generator function called squares that should receive a number n. It should generate the squares of all numbers from 1 to n (inclusive).
Note: Submit only the function in the judge system
"""


def squares(n: int):
    next_num = 1
    while next_num <= n:
        yield next_num ** 2
        next_num += 1


# print(list(squares(5)))