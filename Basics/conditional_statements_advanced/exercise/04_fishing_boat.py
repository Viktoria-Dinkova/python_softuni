# В зависимост от сезона:
# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# •	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  -  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# Вход
# От конзолата се четат три реда:
# •	Бюджет на групата - цяло число;
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари - цяло число.
# Изход
# На конзолата да се отпечата следното:
# •	Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.
import math

budget = int(input())
season = input()
men = int(input())
spring_price = 3000
summ_aut_price = 4200
winter_price = 2600
bill = 0

if season == 'Spring':
    if men<= 6:
        bill = 0.9 * spring_price
    elif 7 < men and men <= 11:
        bill = 0.85 * spring_price
    elif men >= 12:
        bill = 0.75 * spring_price

if (season == 'Summer' or season == 'Autumn'):
    if men<= 6:
        bill = 0.9 * summ_aut_price
    elif 7 < men and men <= 11:
        bill = 0.85 * summ_aut_price
    elif men >= 12:
        bill = 0.75 * summ_aut_price

if season == 'Winter':
    if men<= 6:
        bill = 0.9 * winter_price
    elif 7 < men and men <= 11:
        bill = 0.85 * winter_price
    elif men >= 12:
        bill = 0.75 * winter_price

if men % 2 == 0 and season != 'Autumn':
    bill *= 0.95

if budget >= bill:
    print(f'Yes! You have {math.fabs(budget - bill):.2f} leva left.')
else:
    print(f'Not enough money! You need {math.fabs(budget - bill):.2f} leva.')
