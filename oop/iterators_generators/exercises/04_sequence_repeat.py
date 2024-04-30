"""Create a class called sequence_repeat which should receive a sequence and a number upon initialization.
Implement an iterator to return the given elements, so they form a string with a length - the given number.
If the number is greater than the number of elements, then the sequence repeats as necessary. For more clarification, see the examples:"""

class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number - 1:
            raise StopIteration()

        self.idx += 1
        residue = self.idx % len(self.sequence)
        return self.sequence[residue]




# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')


# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')
