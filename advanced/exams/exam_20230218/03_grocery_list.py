"""
Write a function called shop_from_grocery_list that receives information about a budget, a grocery list, products, and their prices, and returns the result after the shopping.
The function will receive a different number of arguments. The arguments will be passed as follows:
•	The first argument will be the budget - an integer in the range [0, 200];
•	The second argument will be the grocery list - a list with one, many, or no strings representing the products needed to be bought;
•	The following arguments will be the tuples with two elements - the first one is the product name (string), and the second one is its price (float);
After receiving the information and calling the function, the program should start tracking the shopping process:
•	Take the product name from each tuple successively and if you have enough money, buy it, and proceed to the next one.
•	If a product has already been purchased, ignore it, and proceed to the next one.
•	If you receive a product that is not on the grocery list, ignore it, and proceed to the next one.
•	If the budget you have is less than the price of the product, STOP shopping!
 In the end:
•	If you manage to buy all the products from the grocery list, return the message: "Shopping is successful. Remaining budget: {budget_left}."
o	The remaining budget should be formatted to the second decimal place.
•	Otherwise, return the message: "You did not buy all the products. Missing products: {"product1", "product2", …, "product N"}."
Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function.
Output
•	Return one of the strings shown above depending on the result.
"""
def shop_from_grocery_list(budget: int, grocery_list: list, *price_list: tuple) -> str:
    result = ''
    caught = []
    for articles in price_list:
        product = articles[0]
        price = float(articles[1])
        if product in grocery_list and product not in caught:
            if budget >= price:
                budget -= price
                caught.append(product)
                grocery_list.remove(product)
            else:
                break
        if budget <= 0:
            break

    set_gross = set(grocery_list)
    set_caught = set(caught)
    diff = set_gross.difference(set_caught)
    if not diff:
        result += f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result += f"You did not buy all the products. Missing products: {', '.join(diff)}."

    return result

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))

