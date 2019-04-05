class Square:
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def print_size(self):
        print("{} by {}".format(self.s1, self.s1))


r1 = Square(10)
r2 = Square(20)
r3 = Square(30)
r1.print_size()
r2.print_size()
r3.print_size()
print(Square.square_list)
