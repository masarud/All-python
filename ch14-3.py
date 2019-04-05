def my_compare(x, y):
    if x is y:
        return True
    else:
        return False

class Square:
    def __init__(self, s1):
        self.s1 = s1


r1 = Square(10)
r2 = Square(10)
r3 = r1
print(my_compare(r1, r3))
