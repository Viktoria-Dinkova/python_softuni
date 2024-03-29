# Напишете програма, която чете две цели числа (N1 и N2) и оператор, с който да се извърши дадена математическа операция.
# Възможните операции са: Събиране(+), Изваждане(-), Умножение(*),  Деление(/) и Модулно деление(%).
# При събиране, изваждане и умножение на конзолата трябва да се отпечатат резултата и дали той е четен или нечетен.
# При обикновеното деление - резултата.
# При модулното деление - остатъка.
# Трябва да се има предвид, че делителят може да е равен на 0 (нула), а на нула не се дели и се отпечата специално съобщениe.
# Вход
# От конзолата се прочитат 3 реда, въведени от потребителя:
# •	N1 - цяло число;
# •	N2 - цяло число;
# •	Оператор - един символ измежду: "+", "-", "*", "/", "%".
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако операцията е събиране, изваждане или умножение:
# o	 "{N1} {оператор} {N2} = {резултат} - {even/odd}"
# •	Ако операцията е деление:
# o	"{N1} / {N2} = {резултат}" - резултат, форматиран до втория знак след десетичната запетая
# •	Ако операцията е модулно деление:
# o	"{N1} % {N2} = {остатък}"
# •	В случай на деление с 0 (нула):
# o	"Cannot divide {N1} by zero"

numb1 = int(input())
numb2 = int(input())
oper = input()

result = 0
even_odd = ''

if (oper == '+' or oper == '-' or oper == '*'):

    if oper == '+':
        result = numb1 + numb2
    elif oper == '-':
        result = numb1 - numb2
    elif oper == '*':
        result = numb1 * numb2

    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'

    print(f'{numb1} {oper} {numb2} = {result} - {even_odd}')

elif (oper == '/' and numb2 != 0):
    result = numb1 / numb2
    print(f'{numb1} {oper} {numb2} = {result:.2f}')

elif (oper == '%' and numb2 != 0):
    result = numb1 % numb2
    print(f'{numb1} {oper} {numb2} = {result}')

elif ((oper == '/' or oper == '%') and numb2 == 0):
    print(f'Cannot divide {numb1} by zero')
