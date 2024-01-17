# Write a program, which sums the ASCII codes of N characters and prints the sum on the console.
# On the first line, you will receive N – the number of lines.
# On the following N lines – you will receive a letter per line.
# Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].

number_of_lines = int(input())
a_code  = 0
total_sum = 0

for char in range(number_of_lines):
    a_code = ord(input())
    total_sum += a_code

print(f'The sum equals: {total_sum}')
