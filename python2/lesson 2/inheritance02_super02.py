class Parent:
    def __init__(self):
        self.name = "Parent"

    def greet(self):
        print("Hello from", self.name)


class Child(Parent):
    def __init__(self):
        super().__init__()  # Memanggil __init__() dari kelas induk

    def greet(self):
        super().greet()  # Memanggil metode greet() dari kelas induk
        print("Hello from Child")


child = Child()
child.greet()