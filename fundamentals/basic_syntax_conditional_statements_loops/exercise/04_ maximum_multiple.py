# On the first line, you will be given a positive number, which will serve as a divisor.
# On the second line, you will receive a positive number that will be the boundary.
# You should find the largest integer N, that is:
# · divisible by the given divisor
# · less than or equal to the given bound
# · greater than 0
# Note: it is guaranteed that N is found.

divisor = int(input())
boundary = int(input())

for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        break

print(f'{number}')

