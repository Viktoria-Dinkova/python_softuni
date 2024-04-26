"""
Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.
Note: Submit only the class in the judge system
"""
class vowels:
    def __init__(self, string: str):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.idx = 0
        self.end = len(self.string)

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < self.end:
            s = self.string[self.idx]
            self.idx += 1
            if s.lower() in self.vowels:
                return s

        raise StopIteration()


# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
