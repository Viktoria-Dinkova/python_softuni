# Дадени са 2*n-на брой числа. Първото и второто формират двойка, третото и четвъртото също и т.н.
# Всяка двойка има стойност – сумата от съставящите я числа.
# Напишете програма, която проверява дали всички двойки имат еднаква стойност или печата максималната разлика между две последователни двойки.
# Ако всички двойки имат еднаква стойност, отпечатайте "Yes, value={Value}" + стойността. В противен случай отпечатайте "No, maxdiff={Difference}" + максималната разлика.
import math

packs = int(input())
min_diff = 0
max_diff = 0
old_sum = 0
new_sum = 0
suma = 0

for doubles in range(1, packs + 1):
    num1 = int(input())
    num2 = int(input())

    old_sum = new_sum
    new_sum = num1 + num2

    if doubles == 1:
        max_diff = new_sum
        min_diff = new_sum

    else:
        max_diff = max(max_diff, new_sum)
        min_diff = min(min_diff, new_sum)

    suma += new_sum
    doubles += 2

if suma / packs == new_sum:
    print(f'Yes, value={new_sum}')
else:
    print(f'No, maxdiff={max_diff - min_diff}')
