"""
Create a generator function called reverse_text that receives a string and yields all string characters on one line in reversed order.
"""

def reverse_text(string: str):
    idx = len(string) - 1
    while idx >= 0:
        yield string[idx]
        idx -= 1

# for char in reverse_text("step"):
#     print(char, end='')
