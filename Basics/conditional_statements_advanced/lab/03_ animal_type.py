# 1.	dog -> mammal
# 2.	crocodile, tortoise, snake -> reptile
# 3.	others -> unknown

animal = input()
comment = ''

if animal == 'dog':
    comment = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    comment = 'reptile'
else:
    comment = 'unknown'

print(f'{comment}')
