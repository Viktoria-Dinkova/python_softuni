"""
Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely.
The first two numbers in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current number with the previous one.
"""

def fibonacci():
    num_1, num_2 = 0, 1

    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


# generator = fibonacci()
# for i in range(10):
#     print(next(generator))
