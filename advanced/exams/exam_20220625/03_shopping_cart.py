"""
Write a function called shopping_cart that adds products to a shopping cart for the following three types of meals:
"Soup", "Pizza", and "Dessert". Every order has a limit of products that can be added to it:
•	Soup: 3
•	Pizza: 4
•	Dessert: 2
Once you reach the limit of a order, you should stop adding products to that order.
The function will receive a different number of arguments. The arguments will be passed as tuples with two elements - the first one is the type of order, and the second is the product for the order.
You need to take each argument and make a dictionary with the order's name as a key and the products as a value of the corresponding key.
There are some additional requirements:
•	If you receive the same product for the same order more than once, you must not add it again.
•	If you run into the word "Stop" (not tuple) as an argument, you must immediately stop adding products to the cart - just sort and return the desired result as described below.
In the end, sort the meals by the number of bought products in descending order. If there are meals with an equal number of products, sort them (the meals) by their name in ascending order (alphabetically). For each order sort its products in ascending order (alphabetically).
Return an output as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input, just parameters passed to your function
Output
•	Return a string for each of the 3 types of a order of the sorted result in the format:
o	"{meal_type}:"
" - {first_product_added}"
" - {second_product_added}"
 …
" - {Nth_product_added}"
o	If there are no products given for a order, return just its name in the format shown above.
•	If there are NO products in the cart (at all), return the message: "No products in the cart!"
"""

def shopping_cart(*info):
    cart = {
        'Soup': set(),
        'Pizza': set(),
        'Dessert': set()
    }

    result = ''
    lens = 0

    for data in info:
        if data == "Stop":
            break

        meal, product = data[0], data[1]
        if meal == 'Soup' and len(cart['Soup']) < 3:
            cart['Soup'].add(product)
        elif meal == 'Pizza' and len(cart['Pizza']) < 4:
            cart['Pizza'].add(product)
        elif meal == 'Dessert' and len(cart['Dessert']) < 2:
            cart['Dessert'].add(product)

    for k, v in sorted(cart.items(), key=lambda item: (-len(item[1]), item[0])):
            result += f'{k}:\n'
            for in_v in sorted(v):
                result += f' - {in_v}\n'

            lens += len(v)

    if lens == 0:
        result =  "No products in the cart!"

    return result

#
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))


#
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
