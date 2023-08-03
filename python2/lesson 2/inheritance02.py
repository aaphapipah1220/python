# dapat membuat banyak kelas turunan / child class

"""

class example1(parent):
    pass

class example2(parent):
    pass

class example(parent):
    pass

"""

# ================================

# class
class mobil:

    # fungsi
    def __init__(self, warna, jumlahBan, merk, tahunKeluaran):
        self.warna = warna
        self.jumlahBan = jumlahBan
        self.merk = merk
        self.tahunKeluaran = tahunKeluaran


class motor(mobil):
    def __init__(self, harga, warna, jumlahBan, merk, tahunKeluaran):
        self.harga = harga
        mobil.__init__(self, warna, jumlahBan, merk, tahunKeluaran)

    # fungsi menampilkanBREAK
    def showMotor(self):
        print(f"saya memiliki motor berwarna {self.warna} {self.merk} {self.tahunKeluaran} {self.jumlahBan} dan saya"
              f"membeli dengan harga {self.harga}")

motorSaya = motor("merah", "vario", "2023", 2, 15000000)
motorSaya.showMotor()

