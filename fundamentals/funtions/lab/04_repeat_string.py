# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.

in_string = input()
repeater = int(input())

def repeating(single_text: str, counter: int) -> str:
    out_string = ''
    for i in range(counter):
        out_string += single_text

    return out_string

print(repeating(in_string, repeater))
