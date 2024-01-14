# Write a program that reads a floating-point number and:
# -	prints "zero" if the number is zero
# -	prints "positive" or "negative"
# -	adds "small" if the abs value is less than 1 and not 0, or "large" if it exceeds
# 1 000 000

input_number = float(input())
sign = ''
size = ''

# determines the sign of the number

if input_number == 0:
    sign = 'zero'
elif input_number < 0:
    sign = 'negative'
else:
    sign = 'positive'

# determines the size of the number
if abs(input_number) < 1 and input_number != 0:
    size = 'small '
elif abs(input_number) > 1000000:
    size = 'large '
else:
    size = ''

print(f'{size}{sign}')