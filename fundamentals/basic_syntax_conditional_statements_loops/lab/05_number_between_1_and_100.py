# Write a program that reads different floating-point numbers from the console.
# When it receives a number between 1 and 100 inclusive, the program should stop reading and should print "The number {number} is between 1 and 100".

current_number = float(input())

while not (1 <= current_number <= 100):
     current_number = float(input())
else:
    print(f'The number {current_number} is between 1 and 100')

