'''
Да се напише програма, която чете цяло число, въведено от потребителя и проверява дали е под 100, между 100 и 200 или над 200. Ако числото е:
•	под 100 отпечатайте: "Less than 100"
•	между 100 и 200 отпечатайте: "Between 100 and 200"
•	над 200 отпечатайте: "Greater than 200"
'''

number = int(input())

if number < 100:

    print('Less than 100')

elif number > 200:

    print('Greater than 200')

else:

    print('Between 100 and 200')
