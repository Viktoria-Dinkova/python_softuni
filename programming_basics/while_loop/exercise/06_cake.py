# Ще получите размерите на тортата (широчина и дължина – цели числа и след това на всеки ред,
# до получаване на командата "STOP" или докато не свърши тортата, броят на парчетата, които гостите вземат от нея.
# Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# •	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# •	"No more cake left! You need {брой недостигащи парчета} pieces more."

width = int(input())
length  = int(input())

pieces_area = 1
cake_area = width * length
left_cake = cake_area

pieces = 0

while left_cake > 0:
    command = input()
    if command == 'STOP':
        break

    pieces = int(command)

    if left_cake >= pieces:
        left_cake -= pieces
    else:
        break


if command == 'STOP':
    print(f'{left_cake} pieces are left.')
else:
    print(f'No more cake left! You need {pieces - left_cake} pieces more.')
