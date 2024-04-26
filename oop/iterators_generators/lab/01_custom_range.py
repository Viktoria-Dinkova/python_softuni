"""
Create a class called custom_range that receives a idx (int) and an end (int) upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the numbers from the idx to the end (inclusive).
Note: Submit only the class in the judge system
"""

class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            x = self.start
            self.start += 1
            return x

        raise StopIteration()

# one_to_ten = custom_range(1, 3)
# for num in one_to_ten:
#     print(num)
