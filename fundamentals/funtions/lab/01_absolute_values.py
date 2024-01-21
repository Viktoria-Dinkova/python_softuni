# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as a list. Use abs().

input_list = list(map(float, input().split()))
output_list = []

for current_number in input_list:
    output_list.append(abs(current_number))


print(f'{output_list}')