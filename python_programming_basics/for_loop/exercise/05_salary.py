# Шеф на компания забелязва че все повече служители прекарват  време в сайтове, които ги разсейват.
# За да предотврати това, той въвежда изненадващи проверки на отворените табове на браузъра на служителите си.
# Според отворения сайт в таба се налагат следните глоби:
# •	"Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.
# От конзолата се четат два реда:
# •	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# •	Заплата - число в интервала [500...1500]
# След това n – на брой пъти се чете име на уебсайт – текст
# Изход
# •	Ако по време на проверката заплатата стане по-малка или равна на 0 лева, на конзолата се изписва
# "You have lost your salary." и програмата приключва.
# •	В противен случай след проверката на конзолата се изписва остатъкът от заплатата (да се изпише като цяло число).

browsers_count = int(input())
salary = float(input())

browser_name = ''

for browser in range(browsers_count):
    browser_name = input()

    if browser_name == 'Facebook':
        salary -= 150
    elif browser_name == 'Instagram':
        salary -= 100
    elif browser_name == 'Reddit':
        salary -= 50

if salary <= 0:
    print(f'You have lost your salary.')

else:
    print(f'{int(salary)}')
