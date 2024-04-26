"""
Create a generator function called genrange that receives a start (int) and an end (int) upon initialization. It should generate all the numbers from the start to the end (inclusive).
Note: Submit only the function in the judge system
"""

def genrange(start: int, end: int):
    n = start
    while n <= end:
        yield n
        n += 1

# print(list(genrange(1, 10)))