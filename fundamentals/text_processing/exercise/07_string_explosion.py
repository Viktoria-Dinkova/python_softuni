# Write a program that reads a string from the console that contains:
# •	Explosions marked with '>'
# •	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# •	Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark ('>')
# while deleting characters, you should add the strength to your previous explosion. You should not delete the explosion character – '>'.
# When all characters are processed, print the final string.
# Constraints
# •	You will always receive strength for the explosions
# •	The path will consist only of letters from the Latin alphabet, integers, and the char '>'
# •	The strength of the punches will be in the interval [0…9]
in_string = input()
strenght = 0
out_string = ''

for char in range(len(in_string)):
    current = in_string[char]
    if in_string[char] == '>':
        out_string += in_string[char]
        strenght += int(in_string[char + 1])
    elif strenght > 0 and in_string[char] != '>':
        strenght -= 1
    else:
        out_string += in_string[char]

print(f'{out_string}')