# You are an astronaut who just embarked on a mission across the solar system. Since you will be in space for a long time,
# you have packed a lot of food with you. Create a program, which helps you identify how much food you have left
# and gives you information about its expiration date.
# On the first line of the input, you will be given a text string. You must extract the information about the food and calculate the total calories.
# First, you must extract the food info. It will always follow the same pattern rules:
# •	It will be surrounded by "|" or "#" (only one of the two) in the following pattern:
# #{item name}#{expiration date}#{calories}#   or
# |{item name}|{expiration date}|{calories}|
# •	The item name will contain only lowercase and uppercase letters and whitespace.
# •	The expiration date will always follow the pattern: "{day}/{month}/{year}", where the day, month, and year will be exactly two digits long.
# •	The calories will be an integer between 0-10000.
# Calculate the total calories of all food items and then determine how many days you can last with the food you have.
# Keep in mind that you need 2000kcal a day.
# Input / Constraints
# •	You will receive a single string.
# Output
# •	First, print the number of days you will be able to last with the food you have:
# "You have food to last you for: {days} days!"
# •	The output for each food item should look like this:
# "Item: {item name}, Best before: {expiration date}, Nutrition: {calories}"

import re

total_calories_of_all_food = 0
days = 0
food_list = []

food_information = input()
pattern = r'([|#])([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
matches = re.findall(pattern, food_information)


for elements in matches:
    item_name, expiration_date, calories = elements[1], elements[2], int(elements[3])
    # print(f'Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}')
    food_list.append(f'Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}')
    total_calories_of_all_food += calories


days = total_calories_of_all_food // 2000
print(f'You have food to last you for: {days} days!')
for i in food_list:
    print(i)