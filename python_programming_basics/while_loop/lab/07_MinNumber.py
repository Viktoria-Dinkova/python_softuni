# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-малкото измежду тях и го принтира. Въвежда се по едно число на ред.

min_num = int(input())

while min_num:
    curr_num = input()

    if curr_num == 'Stop':
        break

    curr_num = int(curr_num)

    if min_num > curr_num:
        min_num = curr_num

print(f'{min_num}')