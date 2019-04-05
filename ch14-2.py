class Square:
    def __init__(self, s1):
        self.s1 = s1
    def __repr__(self):
        return ("{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1))

r1 = Square(29)
print(r1)
