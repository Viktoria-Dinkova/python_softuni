"""
Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int).
Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step.
For more clarification, see the examples:
"""


class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self._iter = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self._iter == self.count - 1:
            raise StopIteration()

        self._iter += 1
        return self._iter * self.step



# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
