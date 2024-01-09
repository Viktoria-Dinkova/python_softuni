# Напишете програма, която чете n на брой цели числа.
# Принтирайте най-голямото и най-малкото число сред въведените.

numbers_count = int(input())
num = 0
min_num = 0
max_num = 0

for i in range(0, numbers_count, 1):
    if i == 0:
        num = int(input())
        min_num = max_num = num
    else:
        num = int(input())
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
