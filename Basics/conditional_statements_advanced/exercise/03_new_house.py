# изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен. Различните цветя са с различни цени:
# цвете	                Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	    5	3.80	2.80	3	    2.50
# Съществуват следните отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.
import math

flower = input()
count_flo = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.8
tulip_price = 2.8
narcissus_price = 3
gladiola_price = 2.5
bill = 0

# •	Вид цветя "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
if flower == 'Roses':
        if count_flo >80:
            bill = 0.9 * (count_flo * rose_price)   # •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
        else:
            bill = (count_flo * rose_price)

if flower == 'Dahlias':
    if count_flo > 90:
        bill = 0.85 * (count_flo * dahlia_price)   # •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
    else:
        bill = (count_flo * dahlia_price)

if flower == 'Tulips':
    if count_flo > 80:
        bill = 0.85 * (count_flo * tulip_price) # •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
    else:
        bill = (count_flo * tulip_price)

if  flower == 'Narcissus':
    if count_flo < 120:
        bill = 1.15 * (count_flo * narcissus_price)   # •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
    else:
        bill = (count_flo * narcissus_price)

if  flower == 'Gladiolus':
    if count_flo < 80:
        bill = 1.20 * (count_flo * gladiola_price)   # •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
    else:
        bill = (count_flo * gladiola_price)

if (bill - budget) > 0:
    print(f'Not enough money, you need {(math.fabs(bill - budget)):.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {count_flo} {flower} and {(math.fabs(bill - budget)):.2f} leva left.')

