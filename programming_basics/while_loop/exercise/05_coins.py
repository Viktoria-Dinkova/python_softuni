# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети може да стане това.

suma = float(input()) * 100
coin200 = 0
coin100 = 0
coin50 = 0
coin20 = 0
coin10 = 0
coin5 = 0
coin2 = 0
coin1 = 0

while suma != 0:
    if suma >= 200:
        coin200 = suma // 200
        suma = suma % 200
    elif suma >= 100:
        coin100 = suma // 100
        suma = suma % 100
    elif suma >= 50:
        coin50 = suma // 50
        suma = suma % 50
    elif suma >= 20:
        coin20 = suma // 20
        suma = suma % 20
    elif suma >= 10:
        coin10 = suma // 10
        suma = suma % 10
    elif suma >= 5:
        coin5 = suma // 5
        suma = suma % 5
    elif suma >= 2:
        coin2 = suma // 2
        suma = suma % 2
    elif suma >= 1:
        coin1 = suma // 1
        suma = suma % 1

coin = coin200 + coin100 + coin50 + coin20 + coin10 + coin5 + coin2 + coin1
print(f'{int(coin)}')
