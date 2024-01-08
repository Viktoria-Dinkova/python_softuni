# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя, и пресмята цената според цените от таблиците по-горе:
# •	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# •	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# •	количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка. При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".

product = input()
day = input()
vol = float(input())
price = 0
bill = 0

if (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'):
    if product == 'banana':
        price = 2.5
    elif product == 'apple':
        price = 1.2
    elif product == 'orange':
        price = 0.85
    elif product == 'grapefruit':
        price = 1.45
    elif product == 'kiwi':
        price = 2.7
    elif product == 'pineapple':
        price = 5.5
    elif product == 'grapes':
        price = 3.85

elif (day == 'Saturday' or day == 'Sunday'):
    if product == 'banana':
        price = 2.7
    elif product == 'apple':
        price = 1.25
    elif product == 'orange':
        price = 0.9
    elif product == 'grapefruit':
        price = 1.6
    elif product == 'kiwi':
        price = 3
    elif product == 'pineapple':
        price = 5.6
    elif product == 'grapes':
        price = 4.2

bill = vol * price

if bill > 0:
    print(f'{bill:.2f}')
else:
    print('error')






