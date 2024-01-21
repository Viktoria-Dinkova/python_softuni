# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().

in_numbers = list(map(float, input().split(' ')))
def rounding(number: float) -> int:
    out_num = []
    for number in in_numbers:
        out_num.append(round(number))
    print (f'{out_num}')

rounding(in_numbers)