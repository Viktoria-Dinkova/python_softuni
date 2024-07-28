# Вход
# От конзолата се четат пет реда:
# •	Първи ред – брой дни – цяло число в интервал [1…5000]
# •	Втори ред – оставена храна в килограми – цяло число в интервал [0…100000]
# •	Трети ред – храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
# •	Четвърти ред – храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
# •	Пети ред – храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]
# Изход
# На конзолата трябва да се отпечата на един ред:
# •	Ако оставената храна Е достатъчна:
# o	"{килограма остатък} kilos of food left."
# 	Резултатът трябва да е закръглен към по-ниското цяло число
# •	Ако оставената храна НЕ Е достатъчна:
# o	“{килограма недостигат} more kilos of food are needed.”
# 	Резултатът трябва да е закръглен към по-високото цяло число
import math

days = int(input())
food = int(input())
dog_day_food = float(input())
cat_day_food = float(input())
turtal_day_food = float(input()) / 1000

needed_food = days * (dog_day_food + cat_day_food + turtal_day_food)

if needed_food <= food:
    print(f'{math.floor((math.fabs(needed_food - food)))} kilos of food left.')

else:
    print(f'{math.ceil((math.fabs(needed_food - food)))} more kilos of food are needed.')
