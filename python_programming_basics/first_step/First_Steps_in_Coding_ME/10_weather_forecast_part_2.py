# при въведени градуси (реално число) принтира какво е времето
# 26.00 - 35.00	Hot
# 20.1 - 25.9	Warm
# 15.00 - 20.00	Mild
# 12.00 - 14.9	Cool
# 5.00 - 11.9	Cold

weather = float(input())

if (26 <= weather <=35):
    print(f'Hot')

elif (20 < weather < 26):
    print(f'Warm')

elif (15 <= weather <= 20):
    print(f'Mild')

elif (12 <= weather < 15):
    print(f'Cool')

elif (5 <= weather < 12):
    print(f'Cold')

else:
    print(f'unknown')
