"""
On the first line, you will be given a sequence of integers representing the amount of money in Henry's pocket. In the next line, you will be given another sequence of integers representing the prices of foods that Henry can buy.
Henry has gone to his favorite fast food place, fumbles in his pocket and pulls out some change.
 You have to start with the last element from the amount of money sequence and compare it with the first element from the prices sequence.
•	If their values are equal, Henry buys the food. After that, you should remove both of them from their sequences.
•	If the amount of money is bigger than the price, he buys the food again, taking change (the difference between the amount of money and the price) and putting it in his pocket. You should calculate the difference between the values, and keep it.
o	Remove the current amount of money from its sequence and increase the next amount of money value in the sequence by the resulting difference you have calculated.
o	Remove the price from the prices sequence.
•	If the amount of money is lower than the price remove both of them from their sequences.
You need to stop comparing when you have no more amounts of money or prices.
Input / Constraints
•	On the first line, you will receive the integers, representing the amount of money size, separated by a single space.
•	On the second line, you will receive the integers, representing the price size, separated by a single space.
•	All given numbers will be valid integers in the range [1, 20].
Output
•	The output of your program should be a single line of text, formatted according to the following rules:
	If Henry managed to eat four or more foods print the following:
o	"Gluttony of the day! Henry ate {food count} foods."
	If Henry has eaten some of the foods print the following:
o	"Henry ate: {food count} foods."
•	in case Henry has eaten only one food, print: "Henry ate: {food count} food."
	If Henry has not eaten any food:
o	"Henry remained hungry. He will try next weekend again."

"""
from collections import deque

money = [int(x) for x in input().split()]
prices = deque([int(x) for x in input().split()])

curr_money = 0
food = 0
while True:
    curr_money += money.pop()
    curr_price = prices.popleft()

    if curr_money >= curr_price:
        curr_money -= curr_price
        food += 1
    else:
        curr_money = 0

    if not money or not prices:
        break

if food >= 4:
    print(f"Gluttony of the day! Henry ate {food} foods.")
elif food == 0:
    print(f"Henry remained hungry. He will try next weekend again.")
else:
    if food == 1:
        print(f"Henry ate: {food} food.")
    else:
        print(f"Henry ate: {food} foods.")