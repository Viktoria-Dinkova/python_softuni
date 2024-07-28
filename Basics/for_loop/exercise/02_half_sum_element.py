# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,
# и проверява дали сред тях съществува число, което е равно на сумата на всички останали.
# •	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# •	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност)
import math

numbers_count = int(input())
max_num = 0
sum = 0

for i in range(numbers_count):
    curr_num = int(input())
    sum += curr_num

    if max_num < curr_num:
        max_num = curr_num

if max_num == sum - max_num:
    print(f'Yes')
    print(f'Sum = {max_num}')
else:
    print(f'No')
    print(f'Diff = {int(math.fabs(max_num - (sum - max_num)))}')
