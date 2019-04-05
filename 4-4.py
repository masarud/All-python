def first(x):
    if type(x) == int:
        y = x / 2
        return y
    else:
        print("x must be integer")

def second(x):
    if type(x) == int:
        y = x * 4
        return y
    else:
        print("x muxt be integer")
        
a = first(100.1)
print(second(a))