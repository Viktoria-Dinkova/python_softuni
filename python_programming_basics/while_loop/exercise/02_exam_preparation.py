# Програмата трябва да приключи прочитането на данни при команда "Enough" или ако Марин получи определения брой незадоволителни оценки.
# Незадоволителна е всяка оценка, която е по-малка или равна на 4.
# Вход
# •	На първи ред - брой незадоволителни оценки - цяло число;
# •	След това многократно се четат по два реда:
# o	Име на задача – текст;
# o	Оценка - цяло число в интервала [2…6]
# Изход
# •	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o	"Average score: {средна оценка}"
# o	"Number of problems: {броя на всички задачи}"
# o	"Last problem: {името на последната задача}"
# •	Ако получи определеният брой незадоволителни оценки:
# o	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.

poor_marks = int(input())
tasks_name = input()
fails = 0
score = 0
tasks_count = 0
last_task=''

while tasks_name != 'Enough':
    curr_rate = int(input())

    if curr_rate <= 4:
        fails += 1
        if fails == poor_marks:
            print(f'You need a break, {fails} poor grades.')
            break

    score += curr_rate
    tasks_count += 1
    last_task = tasks_name
    tasks_name = input()

av_score = score / tasks_count
if fails != poor_marks:
    print(f'Average score: {av_score:.2f}')
    print(f'Number of problems: {tasks_count}')
    print(f'Last problem: {last_task}')