# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements. Print the resulting integer list.

input_numbers = list(input().split(', '))

count_element_to_removes = input_numbers.count('0')

for _ in range(count_element_to_removes):
    input_numbers.remove('0')
for _ in range(count_element_to_removes):
    input_numbers.append('0')

result = [int(x) for x in input_numbers]
print(f'{result}')