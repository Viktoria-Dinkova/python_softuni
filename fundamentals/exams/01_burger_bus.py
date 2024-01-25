# he Burger Bus travels around the country and serves delicious burgers.
# You need to help the owner keep track of his income and expenses along the way.
# First, you will receive the number of cities the bus has visited.
# Then for every city, you will receive:
# • the name of the city
# • how much money the owner earned
# • owner's expenses
# Every 3rd (third) city  the  bus  visits, the  owner organizes a special  event
# to  ensure  a true "Burger  Bus" experience, spending an additional 50% over costs.
# In  every 5th (fifth) city,  it  is raining, and the  owner losses  10% of  the  money he  earned.
# In  a rainy  city, there  is no possibility to organize a special event.
# You  have  to  calculate the  owner's profit  for  each  city and  his total  profit  from  the  tour.
# Profit  is  calculated  by deducting the expenses from the income.
# Input The input will consist of:
# • Number of cities – integer in the range [1...15].
# • For each city, you will receive the following information:
# o name of the city - string
# o owner's income - a real number in the range [0.0...10 000.0]
# o owner's expenses - a real number in the range [0.0...10 000.0]
# • The input will always be in the correct format. Output
# • For every city, you need to print the following message:  "In {cityName} Burger Bus earned {profit} leva."
# • At the end of the tour, print: "Burger Bus total profit: {totalProfit} leva." NOTE: The profit and the total profit should be formatted to the 2nd decimal place

number_of_cities = int(input())
earn = 0
expenced_money = 0
total = 0
for current_city in range(1, number_of_cities + 1):
    #note = input().split('\n')
    city = input()
    income = float(input())
    expenses = float(input())
    if current_city % 3 == 0 and current_city % 5 != 0:
        expenses *= 1.5
    if current_city % 5 == 0:
        income *= 0.9
    earn = income - expenses
    print(f'In {city} Burger Bus earned {earn:.2f} leva.')

    total += earn

print(f'Burger Bus total profit: {total:.2f} leva.')