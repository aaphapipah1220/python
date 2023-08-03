class parent:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def showParent(self):
        print(f"Hai my name is {self.firstName} {self.lastName}")

class child(parent):
    def __init__(self):
        super().__init__()

    def show(self):
        super().showParent()
        print("Ini contoh yang menggunakan super")
        print("Ini bersifat opsional yaa")

print = child()
print.show()
