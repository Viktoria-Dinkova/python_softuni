# •	Магнолии – 3.25 лева
# •	Зюмбюли – 4 лева
# •	Рози – 3.50 лева
# •	Кактуси – 8 лева
# От общата сума, Мария трябва да плати 5% данъци.
# Вход
# Входът се чете от конзолата и се състои от 5 реда:
# •	Брой магнолии – цяло число в интервала [0 … 50]
# •	Брой зюмбюли – цяло число в интервала [0 … 50]
# •	Брой рози – цяло число в интервала [0 … 50]
# •	Брой кактуси – цяло число в интервала [0 … 50]
# •	Цена на подаръка – реално число в интервала [0.00 … 500.00]
# Изход
# На конзолата трябва да се отпечата един ред.
# •	Ако парите СА стигнали: "She is left with {останали} leva." – сумата трябва да е закръглена към по-малко цяло число (пр. 1.90 -> 1).
# •	Ако парите НЕ достигат: "She will have to borrow {останали} leva." – сумата трябва да е закръглена към по-голямо цяло число (пр. 1.10 -> 2).
import math

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
present_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.5
cacti_price = 8

profit = 0.95 * (magnolias_price * magnolias_count + hyacinths_price * hyacinths_count + roses_price * roses_count + cacti_price * cacti_count)

if present_price <= profit:
    print(f'She is left with {math.floor((math.fabs(present_price - profit)))} leva.')

else:
    print(f'She will have to borrow {math.ceil((math.fabs(present_price - profit)))} leva.')

