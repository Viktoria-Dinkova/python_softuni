# В зависимост от вида на ваканцията (пролетна, лятна или зимна) и вида на групата (момчета/момичета или смесена) цената на нощувката в хотела е различна, както и спортът, който ще практикуват учениците.
# 	                Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момчета/момичета	9.60	        7.20	                15
# смесена група	    10	            9.50	                20
# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка
# В таблицата по-долу са дадени спортовете, които ще се практикуват в зависимост от вида на ваканцията и групата:
# 	            Зимна ваканция	    Пролетна ваканция	    Лятна ваканция
# момичета	    Gymnastics	        Athletics	            Volleyball
# момчета	    Judo	            Tennis	                Football
# смесена група	Ski	                Cycling	                Swimming
# Да се напише програма, която пресмята цената, която ще заплати училището за нощувките и принтира спорта, който ще се практикува от учениците.
# Вход
# От конзолата се четат 4 реда:
# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].
# Изход
# На конзолата се отпечатва 1 ред:
# •	Спортът, който са практикували учениците и цената за нощувките, която е заплатило училището, форматирана до втория знак след десетичната запетая, в следния формат:
# "{спортът} {цената} lv.“

season = input()
gender = input()
students = int(input())
nights = int(input())

sport = ''
tax = 0
check = 0


if gender == 'girls':
    if season == 'Winter':
        sport = 'Gymnastics'
    elif season == 'Spring':
        sport = 'Athletics'
    elif season == 'Summer':
        sport = 'Volleyball'

if gender == 'boys':
    if season == 'Winter':
        sport = 'Judo'
    elif season == 'Spring':
        sport = 'Tennis'
    elif season == 'Summer':
        sport = 'Football'

if gender == 'mixed':
    if season == 'Winter':
        sport = 'Ski'
    elif season == 'Spring':
        sport = 'Cycling'
    elif season == 'Summer':
        sport = 'Swimming'

if gender == 'boys' or gender == 'girls':
    if season == 'Winter':
        tax = 9.6
    elif season == 'Spring':
        tax = 7.2
    elif season == 'Summer':
        tax = 15

if gender == 'mixed':
    if season == 'Winter':
        tax = 10
    elif season == 'Spring':
        tax = 9.5
    elif season == 'Summer':
        tax = 20

check = nights * students * tax

if students >= 50:
    check = nights * students * tax * 0.5
elif students >= 20:
    check = nights * students * tax * 0.85
elif students >= 10:
    check = nights * students * tax * 0.95

print(f'{sport} {check:.2f} lv.')