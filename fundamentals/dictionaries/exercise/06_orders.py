# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.
# Input
# •	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# •	The product data is always delimited by a single space.
# Output
# •	Print information about each product in the following format:
# "{product_name} -> {total_price}"
# •	Format the total price to the 2nd digit after the decimal separator.

products = {}

while True:
    information = input().split()

    if information[0] == 'buy':
        for product, total in products.items():
            print (f'{product} -> {(total[0] * total[1]):.2f}')
        break

    if information[0] not in products:
        products[information[0]] = [float(information[1]), int(information[2])]
    else:
        products[information[0]][0] = float(information[1])
        products[information[0]][1] += int(information[2])


