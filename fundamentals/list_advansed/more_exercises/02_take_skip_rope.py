# Write a program, which reads a string and skips through it, extracting a hidden message.
# The algorithm you should implement is as follows:
# Let us take the string "skipTest_String044160" as an example.
# Take every digit from the string and transfer it somewhere. After this operation, you should have two lists of items - a numbers list and a non-numbers list:
# •	Numbers' list: [0, 4, 4, 1, 6, 0]
# •	Non-numbers: [s, k, i, p, T, e, s, t, _, S, t, r, i, n, g]
# After that, take every digit in the numbers list and split it up into a take list and a skip list.
# In the take list, you should keep all digits at an even lindex.
# In the skip list, you should keep all digits at an odd lindex.
# •	Numbers' list: [0, 4, 4, 1, 6, 0]
# •	Take list: [0, 4, 6]
# •	Skip list: [4, 1, 0]
# Afterward, iterate over both lists:
# •	First, take m characters from the non-numbers list and store it in a result string
# •	Then, skip n characters from the non-numbers list

string = input()
numbers = [int(x) for x in string if 48 <= ord(x) <= 57]
non_numbers = [x for x in string if ord(x) < 48 or ord(x) > 57]
take = [numbers[x] for x in range(len(numbers)) if x % 2 == 0]
skip = [numbers[x] for x in range(len(numbers)) if x % 2 != 0]

take_skip = list(zip(take,skip))
take_skip = str(take_skip).strip('[]')
take_skip = [int(x) for x in take_skip if  48 <= ord(x) <= 57]

message = []
for num in range(len(take_skip)):
    if num % 2 == 0:
        message += non_numbers[:take_skip[num]]
        non_numbers = non_numbers[take_skip[num]+1:]
    else:
        non_numbers = non_numbers[take_skip[num]-1:]

print(''.join(message))


