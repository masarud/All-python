import math


class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        s = (self.base * self.height / 2)
        print("area of this triangle = " + str(s))


triangle1 = Triangle(base = 5 , height = 8)
triangle1.area()

