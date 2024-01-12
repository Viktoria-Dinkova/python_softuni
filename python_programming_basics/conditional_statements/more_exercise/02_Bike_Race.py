# Предстои Вело състезание за благотворителност в което участниците са разпределени в младша("juniors") и старша("seniors") група.
# Парите се набавят от таксата за участие на велосипедистите. Според възрастовата група и вида на трасето на което ще се провежда състезанието, таксата е различна.
# Група	    trail	cross-country	downhill	road
# juniors	5.50	8	            12.25	    20
# seniors	7	    9.50	        13.75	    21.50
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши), таксата  намалява с 25%.
# Организаторите отделят 5% процента от събраната сума за разходи.
# Вход
# От конзолата се четат 2 числа и един стринг, всяко на отделен ред:
# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.

juniors_count = int(input())
seniors_count = int(input())
runway = input()

discount = 0.25
cost = 0.05
juniors_tax = 0
seniors_tax = 0
donation = 0

if runway == 'trail':
    juniors_tax = 5.5
    seniors_tax = 7

if runway == 'cross-country':
    juniors_tax = 8
    seniors_tax = 9.5

if runway == 'downhill':
    juniors_tax = 12.25
    seniors_tax = 13.75

if runway == 'road':
    juniors_tax = 20
    seniors_tax = 21.5

if runway == 'cross-country' and (juniors_count + seniors_count) > 50:
    juniors_tax -= juniors_tax * discount
    seniors_tax -= seniors_tax * discount

donation = juniors_tax * juniors_count + seniors_tax * seniors_count
donation -= donation * cost

print(f'{donation:.2f}')
