'''
Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50). Да се напише програма,
която чете времената на състезателите в секунди, въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").
'''

import math

racer1 = int(input())
racer2 = int(input())
racer3 = int(input())

total_time = racer1 + racer2 + racer3

total_time_min = math.floor(total_time / 60)
total_time_sec = total_time % 60

if total_time_sec < 10:
    print(f'{total_time_min}:0{total_time_sec}')

else:
    print(f'{total_time_min}:{total_time_sec}')

