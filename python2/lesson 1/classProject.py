# class merupakan tempat untuk objek, atribut, variabel, fungsi dll
# def digunakan untuk mendefinisikan sebuah fungsi


class house:
    def __init__(self):
        self.owner = ""
        self.color = ""
        self.material = ""
        self.width = 0
        self.length = 0
        self.height = 0
        self.bedroom = 0
        self.bathroom = 0

    def show(self):
        print("Hi my name is ", self.owner)
        print("My house has ", self.color, " color")
        print("With width : ", self.width, "Length", self.length, "Height:", self.height)
        print("It has :", self.bedroom, " bed room", self.bathroom, " bathroom")

# house type A
# input value
typeA = house()
typeA.owner = "Budi"
typeA.color = "Blue"
typeA.width = 100
typeA.length = 150
typeA.height = 200
typeA.bedroom = 4
typeA.bathroom = 2

# call method show
typeA.show()

# house type B
# input value
typeB = house()
typeB.owner = "Raisa"
typeB.color = "Red"
typeB.width = 250
typeB.length = 350
typeB.height = 450
typeB.bedroom = 6
typeB.bathroom = 1

# call method show
typeB.show()

"""
Project tambahan
"""

# calculate the area using square formula
AreaA = typeA.width * typeA.length * typeA.height
AreaB = typeB.width * typeB.length * typeB.height

def compare():
    if AreaA < AreaB:
        print(typeA.owner, "'s House is smaller than ", typeB.owner, " House")
    else:
        print(typeB.owner, "'s House is smaller than ", typeA.owner, " House")

compare()