import math


class Circle():
    def __init__(self,diameter):
        self.diameter = diameter
        print("circle is generated. daimeter = " + str(self.diameter))

    def area(self):
        s = math.pi * (self.diameter / 2) ** 2 
        print("area of this circle = " + str(s))


circle1 = Circle(10)
circle1.area()
