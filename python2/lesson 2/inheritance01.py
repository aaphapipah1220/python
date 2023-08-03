# buat kelas terlebih dahulu = class
# lalu buat fungsi = def __init__(self) // wajibb
# buat fungsi untuk menampilkan = def
# buat variable untuk menampung penggabungannya
# perhatikan spasi

class example:
    def __init__(self, exampleOne, exampleTwo):
        self.exampleOne = exampleOne
        self.exampleTwo = exampleTwo

    def printExample(self):
        print(f"Ini merupakan contoh dari inheritance : {self.exampleOne} dan {self.exampleTwo}" )

inheritanceShow = example("Ini merupakan contoh 1", "inheritance merupakan pewarisan atau turunan")
inheritanceShow.printExample()
