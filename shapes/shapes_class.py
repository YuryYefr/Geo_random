from random import randint
from string import ascii_uppercase


class Point:
    """basic coordinates for classes"""

    def __init__(self, x=None, y=None):
        self.x = x if x else randint(0, 1000)
        self.y = y if y else randint(0, 1000)

    def __eq__(self, other):
        assert isinstance(other, Point)
        result = (self.x == other.x and self.y == other.y)
        return result

    def __str__(self):
        """formatting our inbound numbers"""
        return f'{self.x}, {self.y}'


class Line:
    """activates when two points created"""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        """formatting our inbound numbers"""
        return f'A({self.p1}), B({self.p2})'

    def isValid(self):
        # return self.p1.x != self.p2.x and self.p1.y != self.p2.y
        if self.p1 == self.p2:
            raise Exception('invalid point')


class BaseShape:
    """parent class for our program"""

    def __init__(self, *args):
        self.points = [i for i in args]
        self.lines = []

    def __str__(self):
        """formatting our inbound numbers"""
        point_strings = [str(p) for p in self.points]
        points_with_letter = []
        for idx, p in enumerate(point_strings):
            points_with_letter.append((ascii_uppercase[idx] + p))
        result = ','.join(points_with_letter)
        return result

    def add_point(self, point):
        self.points.append(point)

    def is_valid(self):
        for i in self.lines:
            return i.isValid()

    def get_square(self):
        pass


class TriangleShape(BaseShape):
    """creating first class"""

    def __init__(self, a, h):
        super().__init__()
        self.a = a
        self.h = h
        self.lines = [a, h]

    def get_square(self):
        return 1 / 2 * (self.a.p1.x + self.a.p2.x) + (self.h.p2.y + self.h.p2.y)


class CircleShape(BaseShape):
    """creating second class"""

    def __init__(self, a):
        super().__init__()
        self.a = a
        self.lines = [a]

    def get_square(self):
        v = (self.a.p1.x + self.a.p2.y) / 2
        return 3.14 * (v ** 2)


class SquareShape(BaseShape):
    """creating third class"""

    def __init__(self, a, b):
        super().__init__()
        self.b = b
        self.a = a
        self.lines = [a, b]

    def get_square(self):
        return abs((self.b.p1.x - self.a.p1.x) * (self.b.p2.y - self.a.p2.y))
