# Според размера на групата, катерачите ще изкачват различни върхове.
# •	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# •	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до втората цифра след десетичната запетая.

groups = int(input())

peoples = 0
musalla = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for group_count in range(groups):
    people_in_group = int(input())

    if people_in_group <= 5:
        musalla += people_in_group
    elif people_in_group <= 12:
        mont_blanc += people_in_group
    elif people_in_group <= 25:
        kilimanjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group

    peoples += people_in_group
    group_count += 1

musalla = musalla / peoples * 100
mont_blanc = mont_blanc / peoples * 100
kilimanjaro = kilimanjaro / peoples * 100
k2 = k2 / peoples * 100
everest = everest / peoples * 100

print(f'{musalla:.2f}%')
print(f'{mont_blanc:.2f}%')
print(f'{kilimanjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')

