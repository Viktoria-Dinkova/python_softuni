# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.

max_num = int(input())

while max_num:
    curr_num = input()

    if curr_num == 'Stop':
        break

    curr_num = int(curr_num)

    if max_num < curr_num:
        max_num = curr_num

print(f'{max_num}')