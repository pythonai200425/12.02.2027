import math


class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"name: {self.name}"

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__('Triangle')
        self.a = a
        self.b = b
        self.c = c

    def get_hekef(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"{super().__str__()}, a: {self.a}, b: {self.b}, c: {self.c} hekef: {self.get_hekef()}"

class TriangeEqualSides(Triangle):
    def __init__(self, a, c):
        super().__init__(a, c)
        self.name += ' Equal Sides'

    def get_hekef(self):
        return self.a * 2 + self.c

class TriangleEquilateral:
    pass

class Rectangle:  # malben
    pass

class Square:  # ribua
    pass

class Circle(Shape):
    def __init__(self, r):
        super().__init__('Circle')
        self.r = r

    def get_hekef(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return f"{super().__str__()}, r: {self.r} hekef: {self.get_hekef()}"

tr1 = Triangle(7, 7, 8)
print(tr1)
circle1 = Circle(8.77)
print(circle1)
