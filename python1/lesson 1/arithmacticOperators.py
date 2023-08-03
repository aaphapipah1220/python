#Macam-macam operator aritmatika pada python

num1 = 50
num2 = 100

tambah = num1 + num2
hasil = tambah
print(hasil)

kurang = num2 - num1
hasilKurang = kurang
print(hasilKurang)

kali = num1 * num2
hasilKali = kali
print(hasilKali)

bagi = num2 / num1
hasilBagi = bagi
print(hasilBagi)

#{:.2f} digunakan untuk memformat angka menjadi desimal dengan 2 digit angka dibelakang koma
division = "{:.2f}".format(num2 / num1)
print(division)

# modulus mengembalikan sisa operasi pembagian dari dua bilangan
num3 = 100
num4 = 90
modulus = num3 % num4
hasilModulus = modulus
print(hasilModulus)

# exponent - pemangkatan
num5 = 2
num6 = 4
exponent = num5 ** num6
hasilExponent = exponent
print(hasilExponent)

#round float - membulatkan bilangan desimal
decimals = 5.7643
print(f"angka desimal sebelum menggunakan round yaitu: {decimals}")

roundDecimals = round(decimals)
print(f"setelah menggunakan round yaitu: {roundDecimals}")