class Slime():
    def __init__(self, hp, mp, color, status):
        self.hp = hp
        self.mp = mp
        self.color = color
        self.status = status
        print("Status of this slime is " + self.status + ".")

    def get_angry(self):
        self.status = "angry"
        print("Status of this slime is " + self.status + ".")


surarin = Slime(100, 30, "blue", "normal")
surarin.get_angry()

surataro = Slime(200, 50, "red", "normal")
surataro.get_angry()