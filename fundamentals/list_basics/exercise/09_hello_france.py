# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00c
# Shoes	35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if the budget after selling all the items is enough for buying the train ticket.
# Input / Constraints
# •	On the 1st line, you will receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
# •	On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
# Output
# •	First, print the list with the bought item’s new prices, formatted to the second decimal point in the following format:
# "{price1} {price2} {price3} … {priceN}"
# •	Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# •	Finally:
# o	If the budget is enough for buying the train ticket, print: "Hello, France!"
# o	Otherwise, print: "Not enough money."
from math import ceil

collection = input().split('|')
budget = float(input())

purchases = []
old_price = 0
new_price = 0
ticket = 150

for element in collection:
    pair = element.split('->')
    type_cloth = pair[0]
    price = float(pair[1])

    if price > budget:
        continue

    if (type_cloth == 'Clothes' and price <= 50.00) or (type_cloth == 'Shoes' and price <= 35.00) or (type_cloth == 'Accessories' and price <= 25.50):
        budget -= price
        old_price += price
        new_price = 1.4 * price
        purchases.append(new_price)
    else:
        continue

for element in purchases:
    print(f'{element:.2f}',end=' ')

print(f'\nProfit: {(sum(purchases) - old_price):.2f}')
if budget + sum(purchases) >= ticket:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')