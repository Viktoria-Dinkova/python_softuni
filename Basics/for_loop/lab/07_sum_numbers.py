# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя и ги сумира.
# •	От първия ред на входа се въвежда броят числа n.
# •	От следващите n реда се въвежда по едно цяло число.
# Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им.

numbers_count = int(input())
number = 0
sum = 0

for i in range(0, numbers_count, 1):
    number = int(input())
    sum += number

print(f'{sum}')