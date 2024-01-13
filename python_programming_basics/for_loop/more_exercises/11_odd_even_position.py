# Напишете програма, която чете n-на брой числа, въведени от потребителя, и пресмята сумата, минимума и максимума на числата на четни и нечетни позиции (броим от 1).
# Когато няма минимален / максимален елемент, отпечатайте "No".
# Изходът да се форматира в следния вид:
# "OddSum=" + {сума на числата на нечетни позиции},
# "OddMin=" + { минимална стойност на числата на нечетни позиции } / {“No”},
# "OddMax=" + { максимална стойност на числата на нечетни позиции } / {“No”},
# "EvenSum=" + { сума на числата на четни позиции },
# "EvenMin=" + { минимална стойност на числата на четни позиции } / {“No”},
# "EvenMax=" + { максимална стойност на числата на четни позиции } / {“No”}

numbers_count = int(input())
odd_sum = 0
odd_min = 0
odd_max = 0
even_sum = 0
even_min = 0
even_max = 0

for i in range(1, numbers_count + 1, 1):
    curr_even_num = float(input())
    if i % 2 == 0:
        if i == 2:
            even_sum += curr_even_num
            even_min = curr_even_num
            even_max = curr_even_num
        else:
            even_sum += curr_even_num
            even_min = min(even_min, curr_even_num)
            even_max = max(even_max, curr_even_num)
    else:
        if i == 1:
            odd_sum += curr_even_num
            odd_min = curr_even_num
            odd_max = curr_even_num
        else:
            odd_sum += curr_even_num
            odd_min = min(odd_min, curr_even_num)
            odd_max = max(odd_max, curr_even_num)

if odd_sum == 0:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')

if even_sum == 0:
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')


