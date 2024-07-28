# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".
# Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт.

product = input()
note = ''

if (product == 'banana' or product == 'apple' or product == 'kiwi' or product == 'cherry' or product == 'lemon' or product == 'grapes'):
    note = 'fruit'
elif (product == 'tomato' or product == 'cucumber' or product == 'pepper' or product == 'carrot'):
    note = 'vegetable'
else:
    note = 'unknown'

print(f'{note}')