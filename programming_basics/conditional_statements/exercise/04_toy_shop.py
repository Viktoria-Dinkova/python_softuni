'''
Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, които ще спечели иска да отиде на екскурзия.
Цени на играчките:
•	Пъзел - 2.60 лв.
•	Говореща кукла - 3 лв.
•	Плюшено мече - 4.10 лв.
•	Миньон - 8.20 лв.
•	Камионче - 2 лв.
Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена. От спечелените пари Петя трябва да даде 10% за наема на магазина.
Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
'''

excursion_price = float(input())
puzzle_count = int(input())
talkingDoll_count = int(input())
teddyBear_count = int(input())
mignon_count = int(input())
truck_count = int(input())

puzzle_price = 2.6
talkingDoll_price = 3
teddyBear_price = 4.1
mignon_price = 8.2
truck_price = 2

account = puzzle_price * puzzle_count + talkingDoll_price * talkingDoll_count + teddyBear_price * teddyBear_count + mignon_price * mignon_count + truck_price * truck_count

if (puzzle_count + talkingDoll_count + teddyBear_count + mignon_count + truck_count) >= 50:
    account -= account * 0.25

profit = account - account * 0.1

if (profit >= excursion_price):
    print(f'Yes! {(profit - excursion_price):.2f} lv left.')

else:
    print(f'Not enough money! {(excursion_price - profit):.2f} lv needed.')

