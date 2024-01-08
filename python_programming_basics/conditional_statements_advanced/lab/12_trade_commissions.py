# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
# Град	0 ≤ s ≤ 500	500 < s ≤ 1 000	1 000 < s ≤ 10 000	s > 10 000
# Sofia	5%	7%	8%	12%
# Varna	4.5%	7.5%	10%	13%
# Plovdiv	5.5%	8%	12%	14.5%
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка. При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

town = input()
sales = float(input())

per_comm = 0
com = 0
profit = 0

if (town == 'Sofia'):
    if (0 <= sales <= 500):
        com = 0.05
    elif (500 < sales <= 1000):
        com = 0.07
    elif (1000 < sales <= 10000):
        com = 0.08
    elif (sales > 10000):
        com = 0.12

    profit = com * sales

if (town == 'Varna'):
    if (0 <= sales <= 500):
        com = 0.045
    elif (500 < sales <= 1000):
        com = 0.075
    elif (1000 < sales <= 10000):
        com = 0.1
    elif (sales > 10000):
        com = 0.13

    profit = com * sales

if (town == 'Plovdiv'):
    if (0 <= sales <= 500):
        com = 0.055
    elif (500 < sales <= 1000):
        com = 0.08
    elif (1000 < sales <= 10000):
        com = 0.12
    elif (sales > 10000):
        com = 0.145

    profit = com * sales

if profit > 0:
    print(f'{profit:.2f}')
else:
    print('error')