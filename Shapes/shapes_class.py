from random import randint


class Point:
    def __init__(self, x=None, y=None):
        self.x = x if x else randint(0, 1000)
        self.y = y if y else randint(0, 1000)


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def is_valid(self):
        if self.p1.x == self.p2.x and self.p1.y == self.p2.y:
            raise Exception("this points cannot be equal")


class BaseShape:
    def __init__(self, *args):
        self.points = [i for i in args]
        self.lines = [(a, b) for a, b in self.points]

    def add_point(self, point):
        self.points.append(point)

    def is_valid(self):
        pass

    def get_square(self):
        pass


class TriangleShape(BaseShape):
    def __init__(self, a, h):
        self.a = a
        self.h = h
        super().__init__()

    def get_square(self):
        return 1 / 2 * (self.a.p1.x + self.a.p2.x) + (self.h.p2.y + self.h.p2.y)


class CircleShape(BaseShape):
    def __init__(self, a):
        self.a = a
        super().__init__()

    def get_square(self):
        v = (self.a.p1.x + self.a.p2.y) / 2
        return 3.14 * (v ** 2)


class SquareShape(BaseShape):
    def __init__(self, a, b):
        self.b = b
        self.a = a
        super().__init__()

    def get_square(self):
        return abs((self.b.p1.x - self.a.p1.x) * (self.b.p2.y - self.a.p2.y))
