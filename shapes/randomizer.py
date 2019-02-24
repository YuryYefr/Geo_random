from shapes.shapes_class import *
import random
import datetime as dt


class RandoMizer:
    """new class for working with user choice in logic module"""

    def __init__(self):
        pass

    def generate_figures(self, some_num):
        """here we input some random numbers and creating a figures """
        figures = []
        while some_num > 0:
            shapes = (CircleShape, SquareShape, TriangleShape)
            figure = random.choice(shapes)
            if figure is TriangleShape:
                line1 = Line(Point(), Point())
                line2 = Line(Point(), Point())
                figures.append(TriangleShape(line1, line2))
            elif figure is SquareShape:
                line1 = Line(Point(), Point())
                line2 = Line(Point(), Point())
                figures.append(SquareShape(line1, line2))
            else:
                line = Line(Point(), Point())
                figures.append(CircleShape(line))
            some_num -= 1
        return figures

    def define_fig(self, figures):
        """this method defines figures and count them"""
        start_now = dt.datetime.now()
        triangle_counter = 0
        inval_triangle_counter = 0
        squareshape_counter = 0
        inval_squareshape_counter = 0
        circleshape_counter = 0
        inval_circleshape_counter = 0
        for val in figures:
            if isinstance(val, TriangleShape):
                if val.is_valid():
                    triangle_counter += 1
                else:
                    inval_triangle_counter += 1
            if isinstance(val, SquareShape):
                if val.is_valid():
                    squareshape_counter += 1
                else:
                    inval_squareshape_counter += 1
            if isinstance(val, CircleShape):
                if val.is_valid():
                    circleshape_counter += 1
                else:
                    inval_circleshape_counter += 1

        total = {"total": len(figures),
                 "valid Triangleshape": triangle_counter,
                 "invalid Tiangleshape": inval_triangle_counter,
                 "valid Squareshape": squareshape_counter,
                 "invalid Squareshape": inval_squareshape_counter,
                 "valid Circleshape": circleshape_counter,
                 "invalid Circleshape": inval_circleshape_counter
                 }
        end_prog = dt.datetime.now()
        elapsed_time = (end_prog - start_now).microseconds
        print("Starting program at \t\t\t", start_now)
        print(total)
        print("Program finished in \t\t\t", end_prog)
        print("Time needed to execute \t\t\t", elapsed_time)
