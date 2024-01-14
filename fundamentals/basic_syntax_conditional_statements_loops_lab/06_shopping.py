# Write a program that reads an integer number representing a budget. On the following lines, it reads integer
# numbers representing the prices of each product you should buy until it receives the command "End".
# During the iterations, if there is not enough budget left to buy the next product, it prints "You went in overdraft!" and end the program.
# Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."

budget = int(input())
price_of_product = input()

while price_of_product != 'End':
        price_of_product = int(price_of_product)

        if budget >= price_of_product:
            budget -= price_of_product
            price_of_product = input()
        else:
            print(f'You went in overdraft!')
            break
else:
    print(f'You bought everything needed.')

