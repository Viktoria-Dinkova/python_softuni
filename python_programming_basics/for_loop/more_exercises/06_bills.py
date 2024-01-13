# За всеки месец разходите са следните:
# •	За ток – всеки месец е различен, ще се чете от конзолата
# •	за вода – 20 лв.
# •	за интернет – 15 лв.
# •	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
# За всеки разход трябва да се пресметне колко общо е платено за всички месеци.
# Вход
# Входът се чете от конзолата:
# •	Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
# •	За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]
# Изход
# Да се отпечата на конзолата 5 реда:
# •	1ви ред: "Electricity: {ток за всички месеци} lv"
# •	2ри ред: "Water: {вода за всички месеци} lv"
# •	3ти ред: "Internet: {интернет за всички месеци} lv"
# •	4ти ред: "Other: {други за всички месеци} lv"
# •	5ти ред: "Average: {средно всички разходи за месец} lv"
# Всички числа трябва да са форматирана до вторият знак след запетаята.

months = int(input())

el_bill = 0
water_bill = 20
inet_bill = 15
all_bill = 0
other_bill = 0
all_other =0

for curr_month in range(months):

    curr_el_bill = float(input())
    el_bill += curr_el_bill
    other_bill += 1.2 * (curr_el_bill + water_bill + inet_bill)
    curr_month += 1

all_bill = el_bill + months * (water_bill + inet_bill) +  other_bill

print(f'Electricity: {el_bill:.2f} lv')
print(f'Water: {(water_bill * months):.2f} lv')
print(f'Internet: {(inet_bill * months):.2f} lv')
print(f'Other: {other_bill:.2f} lv')
print(f'Average: {(all_bill / months):.2f} lv')

