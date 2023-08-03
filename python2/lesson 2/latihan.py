
class tanggal:
    def __init__(self, tgl, bulan, tahun):
        self.tgl = tgl
        self.bulan = bulan
        self.tahun = tahun

class waktu:
    def __init__(self, jam, menit, detik):
        self.jam = jam
        self.menit = menit
        self.detik = detik

class tanggal_waktu(tanggal, waktu):
    def __init__(self, tgl, bulan, tahun, jam, menit, detik):
        tanggal.__init__(self, tgl, bulan, tahun)
        waktu.__init__(self, jam, menit, detik)

    def screen(self):
        print(f"sekarang sudah {self.tgl} {self.bulan} {self.tahun} {self.jam} {self.menit} {self.detik}")

time = tanggal_waktu(15, "juni", 2023, 11, 53, 00)
time.screen()