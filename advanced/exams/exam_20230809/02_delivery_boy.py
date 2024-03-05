'''
You are a pizza delivery boy with a motorized vehicle that delivers pizza in a neighborhood. The neighborhood is represented by a matrix - field.
Each cell in the field represents a part of the neighborhood, and it can contain one of the following elements:
•	'B' - Represents the starting position of the delivery boy.
•	'A' - Represents an address where a pizza needs to be delivered.
•	'*' - Represents an obstacle or an area where the delivery boy cannot drive.
•	'P' - Represents the pizza restaurant.
•	'-' – Represents the road, the delivery boy can drive over it.
In the beginning, you will be given N and M – integers, separated by a single space - " ", indicating the field’s dimensions.
On the next N lines, you will receive strings, representing the rows of the area, with M columns.
The delivery boy must carefully navigate through the streets, following the commands that will be received on each of the following lines- "up", "down", "right", and "left", moving one position at a time.
In this pizza delivery adventure, the delivery boy starts his journey from the position marked as 'B' on the neighborhood field.
His first task is to make his way to the pizza restaurant marked as 'P' and collect the delicious pizza. Once he collects the pizza, the position 'P' is marked as 'R'
and a message is displayed on the Console: "Pizza is collected. 10 minutes for delivery."
However, the neighborhood is not without obstacles. Whenever the delivery boy encounters a cell marked with '*', it signifies an obstacle,
and he cannot make a move in that direction. He must remain in his current position and find an alternative route. The delivery boy should wait for the next command.
If, at any point during his journey, the delivery boy steps out of the neighborhood field (matrix boundaries), it means he has ventured beyond the streets of the neighborhood.
 In such a case, the delivery boy will be considered late for the delivery, and unfortunately, the delivery will be canceled.
 The following message should be displayed on the Console: "The delivery is late. Order is canceled."
 Once the delivery boy successfully reaches an address marked as 'A', he joyfully delivers the pizza, completing his mission.
The position 'A' is marked as 'P'. A message will be displayed on the Console: "Pizza is delivered on time! Next order..."
With each step he takes, the '-'(dash) cells he passes (road) through become '.' (dot) to indicate his path.
Remember, the delivery boy must follow the commands, avoid obstacles, and ensure timely pizza deliveries to the addresses. Good luck!
In the end, print the final state of the matrix (neighborhood area) with the delivery boy in its starting position.
If the boy has been out of the field, mark his starting position with an empty space. Each row is on a new line.
Input
•	On the first line, you will get the number of rows and columns of the matrix, separated by a single space.
•	On the next N lines, you will receive strings, representing each row of the matrix.
•	On each of the following lines, you will receive the possible directions for the delivery boy to move - "up", "down", "right", and "left".
Output
•	On the first line:
o	When the boy collects the pizza:
"Pizza is collected. 10 minutes for delivery."

o	If the pizza is delivered successfully:
"Pizza is delivered on time! Next order..."

o	If the boy leaves the field boundaries:
"The delivery is late. Order is canceled."
•	On the next lines, print the final state of the matrix with the delivery boy in its starting position. If the boy has been out of the field, mark his starting position with an empty space. Each row - on a new line.
'''

def movement(position, to_where):
    mov_row, mov_col = position
    next_row, next_col = mov_row + directions[to_where][0], mov_col + directions[to_where][1]
    if 0 <= next_row < rows and 0 <= next_col < cols:
        if neighborhood[next_row][next_col] != "*":
            return [next_row, next_col]
        else:
            return position

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

rows, cols = [int(s) for s in input().split()]

neighborhood = []
boy_position = []

for r in range(rows):
    curr_row = [c for c in input()]
    if "B" in curr_row:
        boy_position = [r, curr_row.index("B")]
    neighborhood.append(curr_row)

collected = False
curr_row, curr_col = boy_position
while True:
    command = input()
    if neighborhood[curr_row][curr_col] not in ["B", "R"]:
        neighborhood[curr_row][curr_col] = "."

    if not movement([curr_row, curr_col], command):
        neighborhood[boy_position[0]][boy_position[1]] = " "
        print("The delivery is late. Order is canceled.")
        break
    else:
        curr_row, curr_col = movement([curr_row, curr_col], command)

        if neighborhood[curr_row][curr_col] == "P":
            neighborhood[curr_row][curr_col] = "R"
            collected = True
            print("Pizza is collected. 10 minutes for delivery.")
        if collected and neighborhood[curr_row][curr_col] == "A":
            neighborhood[curr_row][curr_col] = "P"
            print("Pizza is delivered on time! Next order...")
            break

[print(*row, sep='') for row in neighborhood]