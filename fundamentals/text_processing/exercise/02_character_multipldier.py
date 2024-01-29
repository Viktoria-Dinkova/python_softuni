# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum,
# then continue with the next two characters. If one of the strings is longer than the other, add the remaining character codes to the total
# sum without multiplication.

first_string, second_string = input().split()
total_sum = 0

shorter = min(len(first_string), len(second_string))

for i in range(shorter):
    total_sum += ord(first_string[i]) * ord(second_string[i])

if len(first_string) == shorter:
    for letter in second_string[shorter::]:
        total_sum += ord(letter)
else:
    for letter in first_string[shorter::]:
        total_sum += ord(letter)

print(f'{total_sum}')

