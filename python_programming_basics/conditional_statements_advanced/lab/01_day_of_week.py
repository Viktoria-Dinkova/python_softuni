# Напишете програма, която чете цяло число, въведено от потребителя, и отпечатва ден от седмицата (на английски език), в граници [1...7] или отпечатва "Error" в случай, че въведеното число е невалидно.
# Примерен вход и изход
# Вход	Изход
# 1	Monday
# 2	Tuesday
# 3	Wednesday
# 4	Thursday
# 5	Friday
# 6	Saturday
# 7	Sunday
# -1	Error

number_day = int(input())
day = ''

if number_day == 1:
    day = 'Monday'
elif number_day == 2:
    day = 'Tuesday'
elif number_day == 3:
    day = 'Wednesday'
elif number_day == 4:
    day = 'Thursday'
elif number_day == 5:
    day = 'Friday'
elif number_day == 6:
    day = 'Saturday'
elif number_day == 7:
    day = 'Sunday'

else:
    day = 'Error'

print(f'{day}')
