# Using a dictionary comprehension, write a program that receives country names on the first line, separated by comma and space ", ",
# and their corresponding capital cities on the second line (again separated by comma and space ", ").
# Print each country with their capital on a separate line in the following format: "{country} -> {capital}".
# Hints
# •	You could use the zip() method.
polit_geo = {}
countrys = input().split(', ')
capirals = input().split(', ')

for i in range(len(countrys)):
    polit_geo[countrys[i]] = capirals[i]

for country, capiral in polit_geo.items():
    print(f'{country} -> {capiral}')
