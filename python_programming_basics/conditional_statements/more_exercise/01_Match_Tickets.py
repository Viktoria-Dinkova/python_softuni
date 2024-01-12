# Билетите имат две категории с различни цени:
# •	IP – 499.99 лева.
# •	Normal – 249.99 лева.
# Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент от бюджета трябва да се задели за транспо
# •	От 1 до 4 – 75% от бюджета.
# •	От 5 до 9 – 60% от бюджета.
# •	От 10 до 24 – 50% от бюджета.
# •	От 25 до 49 – 40% от бюджета.
# •	50 или повече – 25% от бюджета.
# Напишете програма, която да пресмята дали с останалите пари от бюджета могат да си купят билети за избраната категория. И колко пари ще им останат или ще са им нужни.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# •	На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
# •	На втория ред е категорията – "VIP" или "Normal"
# •	На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако бюджетът е достатъчен:
# o	"Yes! You have {останалите пари на групата} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# o	"Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.

budget = float(input())
category = input()
fens = int(input())

ticket_price = 0
transport_price =0
bill = 0

if category == 'VIP':
    ticket_price = 499.99
elif category == 'Normal':
    ticket_price = 249.99

if fens >= 1 and fens <= 4:
    transport_price = 0.75 * budget
    bill = transport_price + fens * ticket_price

elif fens >= 5 and fens <= 9:
    transport_price = 0.6 * budget
    bill = transport_price + fens * ticket_price

elif fens >= 10 and fens <= 24:
    transport_price = 0.5 * budget
    bill = transport_price + fens * ticket_price

elif fens >= 25 and fens <= 49:
    transport_price = 0.4 * budget
    bill = transport_price + fens * ticket_price

elif fens >= 50:
    transport_price = 0.25 * budget
    bill = transport_price + fens * ticket_price

if budget >= bill:
    print(f'Yes! You have {(budget - bill):.2f} leva left.')
else:
    print(f'Not enough money! You need {(bill - budget):.2f} leva.')
