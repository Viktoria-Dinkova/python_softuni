'''
In the beginning, you will be given N and M – integers, separated by a comma - ",", indicating the cupboard’s area dimensions.
On the next N lines, you will receive strings, representing the rows of the area, with M columns.
After that, on each line, until the command "danger" appears as an input string, you will receive the possible directions for the mouse to move - "up", "down", "right", and "left".
If the mouse steps outside the cupboard area, the cat will attack, and the cheese hunt is over. In that case, the program ends, keep the last known position of the mouse,
 before it steps outside the cupboard area and the following message is printed on the Console: "No more cheese for tonight!"
Possible characters in the matrix are:
•	M - represents the mouse's position.
•	C – represents a piece of cheese.
•	* – represents an empty position, nothing happens if the mouse steps on it.
•	@ – represents a wall in the cupboard, cannot step on or go through it.
•	T – represents a trap.
The mouse starts from the M - position.
•	If the mouse steps on C – position, it eats the cheese from the field, and the position is marked with "*".
o	If this is the last cheese in the cupboard area, the mouse goes to sleep. Remember that this will be the last known position of the mouse.
The program ends and the following message is printed on the Console: "Happy mouse! All the cheese is eaten, good night!"
•	If the mouse steps into a trap (T -position), it will be trapped. Remember that this will be the last known position of the mouse.
In that case, the program ends, and the following message is printed on the Console: "Mouse is trapped!"
•	If the given direction leads the mouse towards @ - position, this is a wall in the cupboard area. Do not make the move and skip the command.
•	If the "danger" command is received before the mouse manages to eat all the cheese, the mouse disappears. Remember that this will be the last known position of the mouse
and you will need it for the final state of the matrix. In that case, the program ends, and the following message is printed on the Console: "Mouse will come back later!"
In the end, print the final state of the matrix (cupboard area) with the last known position of the mouse in it. Each row on a new line.
Input
•	On the first line you will get the number of rows and columns of the matrix, separated by a comma.
•	On the next N lines, you will receive strings, representing each row of the matrix.
•	On each of the following lines, until the command "danger" appears as an input string, you will receive the possible directions for the mouse to move - "up", "down", "right", and "left".
•	"danger" command – The mouse spots danger and disappears… for now!
Output
•	On the first line:
o	If the mouse steps outside the cupboard
"No more cheese for tonight!"

o	If the mouse manages to eat all the cheese
"Happy mouse! All the cheese is eaten, good night!"

o	If the mouse steps into a trap (T -position)
"Mouse is trapped!"

o	If the "danger" command is received before the mouse manages to eat all the cheese –
"Mouse will come back later!"

•	On the next lines, print the final state of the matrix with the last known position of the mouse in it. Each row - on a new line, each row position with NO separator.
'''
def valid_position(position, to_where):
    m_row, m_col = position
    next_row, next_col = m_row + directions[to_where][0], m_col + directions[to_where][1]

    if 0 <= next_row < rows and 0 <= next_col < cols:
        return [next_row, next_col]


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

rows, cols = [int(x) for x in input().split(",")]

cheese = 0
mouse = []
kitchen = []
trapped = False

for r in range(rows):
    line = [x for x in input()]
    kitchen.append(line)
    if "M" in line:
        mouse = [r, line.index("M")]
    if "C" in line:
        cheese += line.count("C")
kitchen[mouse[0]][mouse[1]] = "*"

while True:
    command = input()
    old_position = mouse

    if command == 'danger' and cheese:
        print("Mouse will come back later!")
        break

    else:
        if not valid_position(mouse, command):
            print("No more cheese for tonight!")
            break
        else:
            mouse = valid_position(mouse, command)
            if kitchen[mouse[0]][mouse[1]] == '@':
                mouse = old_position

            elif kitchen[mouse[0]][mouse[1]] == 'C':
                cheese -= 1

            elif kitchen[mouse[0]][mouse[1]] == 'T':
                trapped = True

            kitchen[mouse[0]][mouse[1]] = '*'

            if cheese == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break
            if trapped:
                print("Mouse is trapped!")
                break

kitchen[mouse[0]][mouse[1]] = "M"
[print(*k_r, sep='') for k_r in kitchen]

