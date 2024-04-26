"""
Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.
Note: Submit only the class in the judge system
"""
from typing import List


class reverse_iter:
    def __init__(self, iterable: List[int]):
        self.iterable = iterable
        self.start = len(self.iterable) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.start >= self.end:
            x = self.iterable[self.start]
            self.start -= 1
            return x

        raise StopIteration()

# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
