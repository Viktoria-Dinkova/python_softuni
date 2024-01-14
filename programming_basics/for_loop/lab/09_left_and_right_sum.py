# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя,
# и проверява дали сумата на първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата " Yes, sum = " + сумата; иначе печата " No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

numbers_count = int(input())
left_num = 0
right_num = 0
left_sum = 0
right_sum = 0

for i in range(0, numbers_count, 1):
    left_num = int(input())
    left_sum += left_num

for j in range(0, numbers_count, 1):
    right_num = int(input())
    right_sum += right_num

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')
