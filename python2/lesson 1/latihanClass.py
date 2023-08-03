class Hp:
    def __init__(self):
        self.nama = ""
        self.warna = ""

    def screen(self):
        print(f"Hp saya adalah {self.nama} dan berwarna {self.warna}")

HpSaya = Hp()
HpSaya.nama = "samsung"
HpSaya.warna = "hitam"

HpSaya.screen()
