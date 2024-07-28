# Да се напише програма, която чете n-на брой цели числа, подадени от потребителя
# и проверява дали сумата от числата на четни позиции е равна на сумата на числата на нечетни позиции.
# •	Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
# •	Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.

numbers_count = int(input())
num = 0
even_sum = 0
odd_sum = 0

for i in range(0, numbers_count, 1):
    num = int(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {even_sum}')
else:
    print(f'No')
    print(f'Diff = {abs(even_sum - odd_sum)}')

