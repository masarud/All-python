class Horse():
    def __init__(self, color):
        self.color = color

    def ride_on(self, rider):
        self.rider = rider

class Rider():
    def __init__(self, size):
        self.size = size


h1 = Horse("brown")
r1 = Rider(180)

h1.ride_on(r1)
print(h1.rider)