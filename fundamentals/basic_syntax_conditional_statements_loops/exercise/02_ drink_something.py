# Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky.
# Create a program that receives a person's age and prints what he/she drinks.
#
# A kid is defined as someone under or at the age of 14.
# A teen is defined as someone under or at the age of 18.
# A young adult is defined as someone under or at the age of 21.
# An adult is defined as someone above the age of 21.

age = int(input())

drink = ''
mesage = 'drink '

if age <= 14:
    drink = 'toddy'
elif age <= 18:
    drink = 'coke'
elif age <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print(f'{mesage}{drink}')
