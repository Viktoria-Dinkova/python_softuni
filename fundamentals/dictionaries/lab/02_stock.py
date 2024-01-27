# After you have completed your first task, your boss decides to give you another one right away.
# Now not only you have to keep track of the stock, but also you should answer customers if you have some products in stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left".
# •	Otherwise, print "Sorry, we don't have {product}".

all_stocks = input().split()
stocks = {}
for i in range(0, len(all_stocks), 2):
    key = all_stocks[i]
    value = int(all_stocks[i+1])
    stocks[key] = value

asks = input().split()
for product in asks:
    if product in stocks:
        print(f'We have {stocks[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")