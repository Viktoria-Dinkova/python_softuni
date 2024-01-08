# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на различни цени:
# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете
# тип прожекция (текст),
# брой редове и
# брой колони в залата (цели числа),
# и изчислява общите приходи от билети при пълна зала.
# Резултатът да се отпечата във формат 2 знака след десетичната точка.


movie_type = input()
row = int(input())
column =int(input())

premier = 12
normal = 7.5
discount = 5
income = 0

tickets = column * row

if  movie_type == 'Premiere':
    income = tickets * premier

elif movie_type == 'Normal':
    income = tickets * normal

elif movie_type == 'Discount':
    income = tickets * discount

print(f'{income:.2f} leva')
