# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
# The price could be a floating-point or integer number. You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"

import re

purchase = input()
furnitures = []
total_cost = 0

while purchase != 'Purchase':

    parts_of_purchase = r'>>([a-zA-Z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)'
    found = re.search(parts_of_purchase, purchase)
    if found:
        furniture, price, count = found.groups()
        furnitures.append(furniture)
        total_cost += float(price) * int(count)

    purchase = input()

print('Bought furniture:')
for object in furnitures:
    print(f'{object}')
print(f'Total money spend: {total_cost:.2f}')