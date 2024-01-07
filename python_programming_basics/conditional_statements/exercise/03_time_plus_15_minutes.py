'''
Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е часът след 15 минути.
Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.
'''

import math
hours = int(input()) * 60
minutes = int(input())

total_time = hours + minutes + 15

total_time_hours = math.floor(total_time / 60)
total_time_minutes = total_time % 60

if (total_time_hours == 24):
    total_time_hours = 0

if (total_time_minutes <10):
    print(f'{total_time_hours}:0{total_time_minutes}')

else:
    print(f'{total_time_hours}:{total_time_minutes}')
