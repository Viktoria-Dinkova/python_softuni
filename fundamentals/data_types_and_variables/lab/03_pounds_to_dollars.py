# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.

pounds = int(input())
dollars = 1.31 * pounds

print(f'{dollars:.3f}')
