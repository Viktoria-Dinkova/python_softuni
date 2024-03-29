# Студент трябва да пропътува n километра. Той има избор измежду три вида транспорт:
# •	Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
# •	Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
# •	Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.
# Напишете програма, която въвежда броя километри n и период от деня (ден или нощ) и изчислява цената на най-евтиния транспорт.
# Вход
# От конзолата се четат два реда:
# •	Първият ред съдържа числото n – брой километри – цяло число в интервала [1…5000]
# •	Вторият ред съдържа дума “day” или “night” – пътуване през деня или през нощта
# Изход
# Да се отпечата на конзолата най-ниската цена за посочения брой километри, форматирана до втория знак след десетичния разделител.

distance = int(input())
day_night = input()

if  day_night == 'day':
    taxi_tax = 0.79
else:
    taxi_tax = 0.9

bus_tax = 0.09
train_tax = 0.06

total_taxi = 0.7 + distance * taxi_tax
total_bus = distance * bus_tax
total_train = distance * train_tax

if distance >= 100:
    print(f'{(min(total_train, total_bus, total_taxi)):.2f}')

elif distance < 20:
    print(f'{total_taxi:.2f}')

else:
    print(f'{(min(total_bus, total_taxi)):.2f}')