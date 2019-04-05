class Shape():
    def __init__(self):
        self.type = "shape"

    def what_am_i(self):
        print("I am a " + self.type)

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.type = "Rectangle"

s = Shape()
s.what_am_i()

ss = Rectangle(10, 20)
ss.what_am_i()