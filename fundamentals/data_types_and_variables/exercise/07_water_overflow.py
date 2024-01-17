# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.

number_of_lines = int(input())

tank_capacity = 255

message = ''

for current_line in range(number_of_lines):
    line_capacity = int(input())
    if line_capacity > tank_capacity:
        print('Insufficient capacity!')
        continue

    tank_capacity -= line_capacity
else:
    print(f'{255 - tank_capacity}')
