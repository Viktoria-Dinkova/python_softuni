'''
Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и котки.  Храната се пазарува от зоомагазин,
като една опаковка храна за кучета е на цена 2.50 лв, а опаковка храна за котки струва 4 лв.
Вход
От конзолата се четат 2 реда:
1.	Броят на опаковките храна за кучета – цяло число в интервала [0… 100]
2.	Броят на опаковките храна за котки –  цяло число в интервала [0… 100]
Изход
На конзолата се отпечатва:
"{крайната сума} lv."

'''
dogfood_num= int(input())
catfood_num= int(input())

dogfood_price = 2.50
catfood_price= 4.00

total_price = (dogfood_num * dogfood_price) + (catfood_num * catfood_price)

print(f'{total_price} lv.')
