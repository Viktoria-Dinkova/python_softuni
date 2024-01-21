# Create a function that calculates and returns the area of a rectangle by given width and height. Print the result on the console.

width = int(input())
height = int(input())


def area_of_rectangle(a: int, b: int) -> int:
    '''
    function that calculates and returns the area of a rectangle
    param a:
        width - int
        height - int
    return:
        s - int
    '''

    s = a * b
    return s


print(area_of_rectangle(width, height))
