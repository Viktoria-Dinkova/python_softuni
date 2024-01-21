# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
# Print the result formatted to the second decimal place.

product = input()
quantity = int(input())

def total_price_calculation(item: str, valuee: int) -> float:
    '''
    function that calculates the total price of an order
    :param order:
        item - str
        valuee - int
    :return:
        bill of order - float
    '''
    total_price = 0
    single_price = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00
    }
    if item in single_price.keys():
        total_price = (valuee * single_price[item])

    return total_price

print(f'{total_price_calculation(product, quantity):.2f}')