from shapes.serializer import *
from shapes.randomizer import *


def run_prog():
    """our main logic module"""
    dir_path = 'C:/Users/123/PycharmProjects/geo_random/var'
    point1 = Point()
    point2 = Point()
    point3 = Point()
    point4 = Point()
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    square = SquareShape(line1, line2)
    triangle = TriangleShape(line1, line2)
    circle = CircleShape(line1)
    randomizer = RandoMizer()
    print("Choose mode\n"
          "1.one figure\n"
          "2.figures with random points\n"
          "3.to store\n"
          "4.to restore")
    user_input = int(input("your answer is: "))

    if user_input == 1:
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

    elif user_input == 2:
        user_ask = int(input("How much figures you wish to add?: "))
        figures = randomizer.generate_figures(user_ask)
        return randomizer.define_fig(figures)

    elif user_input == 3:
        user_ask = int(input("How much figures you wish to add?: "))
        figures = randomizer.generate_figures(user_ask)
        serializer = Serializer(dir_path, [figures])
        serializer.store()
    else:
        figures = CircleShape, TriangleShape, SquareShape
        serializer = Serializer(dir_path, [figures])
        serializer.restore()