# За да се наспи добре, нормата за игра на Том е 30 000  минути в година.
# •	Когато е на работа, стопанинът му си играе с него по 63 минути на ден.
# •	Когато почива, стопанинът му си играе с него  по 127 минути на ден.
# Напишете програма, която въвежда броя почивни дни и отпечатва дали Том може да се наспи добре и колко е разликата от нормата за текущата година
# като приемем че годината има 365 дни.
# Пример: 20 почивни дни -> работните дни са 345 (365 – 20 = 345). Реалното време за игра е 24 275 минути (345 * 63 + 20 *127).
# Разликата от нормата е 5 725 минути (30 000 – 24 275 = 5 725) или 95 часа и 25 минути.
# Вход
# Входът се чете от конзолата и се състои от едно число – броят почивни дни – цяло число в интервала [0...365]
# Изход
# На конзолата трябва да се отпечатат два реда.
# •	Ако времето за игра на Том е над нормата за текущата година:
# o	 На първия ред отпечатайте: “Tom will run away”
# o	 На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes more for play”
# •	Ако времето за игра на Том е под нормата за текущата година:
# o	На първия ред отпечатайте: “Tom sleeps well”
# o	 На втория ред отпечатайте разликата от нормата във формат:
# “{H} hours and {M} minutes less for play”
import math

holydays = int(input())

wd_play = 63
hd_play = 127
workdays = 365 - holydays
norm = 30000

play_time = workdays * wd_play + holydays * hd_play
diff = math.fabs(norm - play_time)
dif_hour = math.floor(diff / 60)
dif_minutes = (diff % 60)

if (dif_minutes < 10):
    dif_minutes = f'0{dif_minutes}'

if (play_time > norm):
    print(f'Tom will run away')
    print(f'{dif_hour} hours and {dif_minutes:.0f} minutes more for play')

else:
    print(f'Tom sleeps well')
    print(f'{dif_hour} hours and {dif_minutes:.0f} minutes less for play')
