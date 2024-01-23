# Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
# and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.
input_numbers = list(map(int, input().split(', ')))
tens = 10
while True:
    next_tens = []
    for num in input_numbers[::-1]:
        if num <= tens:
            next_tens.append(num)

            if len(input_numbers) == 1:
                print(f"Group of {tens}'s: {next_tens[::-1]}")

            input_numbers.remove(num)

    if len(input_numbers) == 0:
        break
    else:
        print(f"Group of {tens}'s: {next_tens[::-1]}")
        tens += 10

