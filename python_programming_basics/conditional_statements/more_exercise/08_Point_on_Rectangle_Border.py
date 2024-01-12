# Напишете програма, която проверява дали точка {x, y} се намира върху някоя от страните на правоъгълник {x1, y1} – {x2, y2}.
# Входните данни се четат от конзолата и се състоят от 6 реда въведени от потребителя: десетичните числа x1, y1, x2, y2, x и y
# (като се гарантира, че x1 < x2 и y1 < y2). Да се отпечата "Border" (точката лежи на някоя от страните) или "Inside / Outside" (в противен случай).

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

message = ''

if ((x1 <= x and x <= x2) and (y == y1 or y == y2)) or ((y1 <= y and y <= y2) and (x == x1 or x == x2)):
    message = 'Border'

else:
    message = 'Inside / Outside'


print(f'{message}')