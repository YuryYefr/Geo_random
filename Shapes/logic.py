from Shapes.shapes_class import *


def run_prog():
    point1 = Point()
    point2 = Point()
    point3 = Point()
    point4 = Point()
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    square = SquareShape(line1, line2)
    triangle = TriangleShape(line1, line2)
    circle = CircleShape(line1)
    user_ask = input(
        "Would you like to proceed with one figure(""choose no"") or join the darkside(""choose yes"") \nwith random? Y or N: ").lower()
    if user_ask == "n":
        print("1.Circle\n"
              "2.Triangle\n"
              "3.Square\n")
        user_input = int(input("choose figure"))
        if user_input == 1:
            print(circle.get_square())
            exit()
        elif user_input == 2:
            print(triangle.get_square())
            exit()
        elif user_input == 3:
            print(square.get_square())
            exit()
        else:
            exit("shutting down the program")
    elif user_ask == "y":
        user_ask = int(input("How much figures you wish to add?: "))
        return user_ask
