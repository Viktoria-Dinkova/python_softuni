# Write a program that receives a single string containing positive and negative numbers
# separated by a single space. Print a list containing the opposite of each number.

string = input().split(' ')
output_string = []

for num in string:
    curr_num = int(num) * -1
    output_string.append(curr_num)

print(f'{output_string}')