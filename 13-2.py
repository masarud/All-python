class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, x):
        self.s1 = self.s1 + x
        print("s1 was changed to " + str(self.s1))

a_square = Square(30)
print(a_square.calculate_perimeter())
a_square.change_size(10)
print(a_square.calculate_perimeter())