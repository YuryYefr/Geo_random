from Shapes.shapes_class import *

if __name__ == "__main__":
    point1 = Point()
    point2 = Point()
    point3 = Point()
    point4 = Point()
    line1 = Line(point1, point2)
    line2 = Line(point3, point4)
    square = SquareShape(line1, line2)
    triangle = TriangleShape(line1, line2)
    circle = CircleShape(line1)
    user_ask = input("Would you like to proceed with one figure or join the darkside with random? Y or N: ").lower()
    if user_ask == "n":
        print("1.Circle\n"
              "2.Triangle\n"
              "3.Square\n")
    user_input = int(input("choose figure"))
    if user_input == 1:
        print(circle.get_square())
    elif user_input == 2:
        print(triangle.get_square())
    elif user_input == 3:
        print(square.get_square())
    else:
        exit("shutting down the program")