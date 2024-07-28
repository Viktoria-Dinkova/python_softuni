# Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# •	Пари, нужни за екскурзията - реално число;
# •	Налични пари - реално число.
# След това многократно се четат по два реда:
# •	Вид действие – текст с две възможности: "spend" или "save";
# •	Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
# •	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# o	"You can't save the money."
# o	"{Общ брой изминали дни}"
# •	Ако Джеси събере парите за почивката, на конзолата се изписва:
# o	"You saved the money for {общ брой изминали дни} days."

needed_for_excursion = float(input())
cash_available = float(input())

spend_days = 0
all_days = 0

while (cash_available < needed_for_excursion) and (spend_days < 5):
    operation = input()
    curr_sum = float(input())
    all_days += 1

    if operation == 'spend':
        spend_days += 1
        cash_available -= curr_sum

        if spend_days == 5:
            print(f"You can't save the money.")
            print(f'{all_days}')

        if cash_available < 0:
            cash_available = 0

    elif operation == 'save':
        cash_available += curr_sum
        spend_days = 0



if cash_available >= needed_for_excursion:
    print(f"You saved the money for {all_days} days.")


