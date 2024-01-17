# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.

start_year = int(input())
new_year = start_year + 1
new_year = str(new_year)
happy_year = False

while happy_year == False:
    set_year = set(new_year)
    if len(new_year) != len(set_year):
        new_year = int(new_year) + 1
        new_year = str(new_year)
        continue
    else:
        happy_year = True
        break

print(f'{new_year}')


