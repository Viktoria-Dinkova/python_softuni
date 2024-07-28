# чете ден от седмицата (текст), на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend".
# Ако се въведе текст различен от ден от седмицата да се отпечата - "Error".

day = input()
comment = ''

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    comment = f'Working day'
elif day == 'Saturday' or day == 'Sunday':
    comment = f'Weekend'
else:
    comment = 'Error'

print(f'{comment}')
