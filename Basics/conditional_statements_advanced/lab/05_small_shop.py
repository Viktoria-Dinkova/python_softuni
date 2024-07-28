# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	0.50	0.80	1.20	1.45	1.60
# Plovdiv	0.40	0.70	1.15	1.30	1.50
# Varna	0.45	0.70	1.10	1.35	1.55
# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число), въведени от потребителя,
# и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град.

product = input()
town = input()
vol = float(input())

price = 0
bill=0


if (product == 'coffee' and town == 'Sofia'):
    price = 0.5
elif (product == 'coffee' and town == 'Plovdiv'):
    price = 0.4
elif (product == 'coffee' and town == 'Varna'):
    price = 0.45

elif (product == 'water' and town == 'Sofia'):
    price = 0.8
elif (product == 'water' and (town == 'Plovdiv' or town == 'Varna')):
    price = 0.7

if (product == 'beer' and town == 'Sofia'):
    price = 1.2
elif (product == 'beer' and town == 'Plovdiv'):
    price = 1.15
elif (product == 'beer' and town == 'Varna'):
    price = 1.1

if (product == 'sweets' and town == 'Sofia'):
    price = 1.45
elif (product == 'sweets' and town == 'Plovdiv'):
    price = 1.3
elif (product == 'sweets' and town == 'Varna'):
    price = 1.35

if (product == 'peanuts' and town == 'Sofia'):
    price = 1.6
elif (product == 'peanuts' and town == 'Plovdiv'):
    price = 1.5
elif (product == 'peanuts' and town == 'Varna'):
    price = 1.55

bill = vol * price

print(f'{bill}')
