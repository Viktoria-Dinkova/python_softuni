# Create a program that calculates how many loaves you can make with the budget you have.
# Here is the recipe for one loaf:
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l
# On the 1st line, you will receive the budget - a real number in the range [0.0…100000.0]
# On the 2nd line, you will receive the price for 1 kg flour - a real number in the range [0.0…100000.0]
# The price for 1 pack of eggs is 75% of the price for 1 kg flour.
# The price for 1L milk is 25% more than the price for 1 kg flour.
# Keep in mind that you use only 250ml milk for a bread.
# •	For every loaf of bread that you make, you will receive 3 colored eggs.
# •	For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs for your bread.
# The count of eggs you will lose is calculated when you subtract 2 from your current count of loaves - ({current_bread_count} - 2)
# In the end, print the loaves of bread you made, the eggs you have collected, and the money you have left, formatted to the 2nd decimal place:
# "You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."

budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 0.25 * (1.25 * flour_price) #The price for 1L milk is 25% more than the price for 1 kg flour. Consumption of milk	0.250 l

loaf_price = flour_price + eggs_price + milk_price
current_bread_count = 0
loaves_price = 0
colored_eggs = 0

while budget >= loaf_price:
    current_bread_count += 1
    budget -= loaf_price
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= (current_bread_count - 2)

print(f'You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')