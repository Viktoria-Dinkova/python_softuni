# You will be given the coordinates of four points. The first and the second pair of points form two different lines.
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})"
# starting from the point which is closer to the center of the coordinate system (0, 0).
# You can reuse the method that you wrote for the previous problem. If the lines are of equal length, print only the first one.
# The resulting coordinates must be formatted to the lower integer.

def longer_line(x_1: float, y_1:float, x_2: float, y_2: float, x_3: float, y_3: float, x_4: float, y_4: float) -> tuple:
    import math
    '''
    Find the point which is closest to the center of the coordinate system

    :param user_coordinates: list
    :return point: list
    '''

    first_line = math.sqrt(x_1 ** 2 + y_1 ** 2) + math.sqrt(x_2 ** 2 + y_2 ** 2)
    second_line = math.sqrt(x_3 ** 2 + y_3 ** 2) + math.sqrt(x_4 ** 2 + y_4 ** 2)

    if first_line > second_line:
        point1 = (math.floor(x_1), math.floor(y_1))
        point2 = (math.floor(x_2), math.floor(y_2))
        if math.sqrt(x_1 ** 2 + y_1 ** 2) < math.sqrt(x_2 ** 2 + y_2 ** 2):
            print(f'{point1}{point2}')
        else:
            print(f'{point2}{point1}')

    else:
        point1 = (math.floor(x_3), math.floor(y_3))
        point2 = (math.floor(x_4), math.floor(y_4))
        if math.sqrt(x_3 ** 2 + y_3 ** 2) < math.sqrt(x_4 ** 2 + y_4 ** 2):
            print(f'{point1}{point2}')
        else:
            print(f'{point2}{point1}')

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
longer_line(x1, y1, x2 ,y2, x3, y3, x4, y4)
