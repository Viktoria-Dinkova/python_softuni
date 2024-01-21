# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines.
# Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one.
# The resulting coordinates must be formatted to the lower integer.

def closest_point(x_1: float, y_1:float, x_2: float, y_2:float) -> tuple:
    import math
    '''
    Find the point which is closest to the center of the coordinate system

    :param user_coordinates: list
    :return point: list
    '''

    first_distance = math.sqrt(x_1 ** 2 + y_1 ** 2)
    second_distance = math.sqrt(x_2 ** 2 + y_2 ** 2)

    if first_distance <= second_distance:
        point = (math.floor(x_1), math.floor(y_1))
    else:
        point = (math.floor(x_2), math.floor(y_2))

    print(point)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
closest_point(x1, y1, x2 ,y2)

