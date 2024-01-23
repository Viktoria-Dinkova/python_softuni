# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.
in_list = list(map(int, input().split(', ')))
indices = [x for x in range(len(in_list)) if in_list[x] % 2 == 0]
print(f'{indices}')




