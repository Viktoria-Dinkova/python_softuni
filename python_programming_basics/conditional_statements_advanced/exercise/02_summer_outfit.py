# Напишете програма, която спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече.
# От конзолата се четат точно два реда:
# •	Градусите - цяло число;
# •	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
# Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."

degrees = int(input())
time = input()

outfit = ''
shoes = ''

if (time == 'Morning' and degrees >= 10 and degrees <=18):
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'

elif (time == 'Morning' and degrees > 18 and degrees <= 24):
    outfit = 'Shirt'
    shoes = 'Moccasins'

elif (time == 'Morning' and degrees >= 25):
    outfit = 'T-Shirt'
    shoes = 'Sandals'

elif (time == 'Afternoon' and degrees >= 10 and degrees <= 18):
    outfit = 'Shirt'
    shoes = 'Moccasins'

elif (time == 'Afternoon' and degrees > 18 and degrees <= 24):
    outfit = 'T-Shirt'
    shoes = 'Sandals'

elif (time == 'Afternoon' and degrees >= 25):
    outfit = 'Swim Suit'
    shoes = 'Barefoot'

elif (time == 'Evening'):
    outfit = 'Shirt'
    shoes = 'Moccasins'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')


