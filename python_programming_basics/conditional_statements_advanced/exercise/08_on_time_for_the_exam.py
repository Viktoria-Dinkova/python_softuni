# Студент трябва да отиде на изпит в определен час (например в 9:30 часа).
# Той идва в изпитната зала в даден час на пристигане (например 9:40).
# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това.
# Ако е пристигнал по-рано повече от 30 минути, той е подранил.
# Ако е дошъл след часа на изпита, той е закъснял.
# Вход
# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# •	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.
# Изход
# На първия ред отпечатайте:
# •	"Late", ако студентът пристига по-късно от часа на изпита;
# •	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# •	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# •	"mm minutes before the start" за идване по-рано с по-малко от час;
# •	"hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:05”;
# •	 "mm minutes after the start" за закъснение под час;
# •	"hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:03”.
import math

hour_ex = int(input())
min_ex  = int(input())
hour_st = int(input())
min_st  = int(input())
hour = 0
min = 0

time_ex = hour_ex * 60 + min_ex
time_st = hour_st * 60 + min_st

if (time_st - time_ex) > 0 and (time_st - time_ex) < 60:
   min = (time_st - time_ex) % 60
   if min < 10:
       print('Late')
       print(f'0{min} minutes after the start')
   else:
       print('Late')
       print(f'{min} minutes after the start')

if (time_st - time_ex) >= 60:
    hour = math.floor((time_st - time_ex) / 60)
    min = (time_st - time_ex) % 60
    if min < 10:
           print('Late')
           print(f'{hour}:0{min} hours after the start')
    else:
        print('Late')
        print(f'{hour}:{min} hours after the start')

if (time_ex - time_st) > 30 and (time_ex - time_st) < 60:
    min = (time_ex - time_st) % 60
    if min < 10:
           print('Early')
           print(f'0{min} minutes before the start')
    else:
        print('Early')
        print(f'{min} minutes before the start')

if (time_ex - time_st) >= 60:
    hour = math.floor((time_ex - time_st) / 60)
    min = (time_ex - time_st) % 60
    if min < 10:
        print('Early')
        print(f'{hour}:0{min} hours before the start')
    else:
        print('Early')
        print(f'{hour}:{min} hours before the start')


if (time_ex == time_st) :
    print('On time')
    print('')

if (time_ex - time_st) <= 30:
    min = (time_ex - time_st) % 60
    print('On time')
    print(f'{min} minutes before the start')
