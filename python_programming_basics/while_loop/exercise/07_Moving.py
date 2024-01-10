# Всеки кашон е с точни размери:  1m x 1m x 1m.
# Вход
# Потребителят въвежда следните данни на отделни редове:
# 1.	Широчина на свободното пространство - цяло число;
# 2.	Дължина на свободното пространство - цяло число;
# 3.	Височина на свободното пространство - цяло число;
# 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
# Програмата трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.
# Изход
# Да се отпечата на конзолата един от следните редове:
# -	Ако стигнете до командата "Done" и има още свободно място:
# "{брой свободни куб. метри} Cubic meters left."
# -	Ако свободното място свърши преди да е дошла команда "Done":
# "No more free space! You need {брой недостигащи куб. метри} Cubic meters more."

width_free = int(input())
length_free = int(input())
height_free = int(input())

box_area = 1
room_area = width_free * length_free *height_free
free_area = room_area
all_boxes = 0

while free_area > 0:
    command = input()

    if command == 'Done':
        break

    else:
        count_of_boxes = int(command)
        if free_area >= count_of_boxes:
            free_area -= count_of_boxes
            all_boxes += count_of_boxes
        else:
            all_boxes += count_of_boxes
            break

if command == 'Done':
    print(f'{free_area} Cubic meters left.')
else:
    print(f'No more free space! You need {all_boxes - room_area} Cubic meters more.')