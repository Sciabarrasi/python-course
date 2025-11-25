#triangle display

base1 = int(input("Enter the length of side 1: "))
height = int(input("Enter the height: "))

def triangle_area(base1, height):
    area = base1 * height
    return print(area)

triangle_area(base1, height)