# append digunakan untuk menambahkan elemen baru
# del untuk menghapus value dari array = panggil nomor arraynya
# remove untuk menghapus nilai array dengan memanggil nama value nya

# array declaration
cars = ["volvo", "mazda", "toyota"]

# initial cars
print("Below are the initial cars:")
print(cars)

# array addition
print("Below are the arrays after adding a new car to the array: ")
cars.append("Honda mobil punya gabriel")
print(cars)

# array deletion with del
print("Below are the arrays after deleting the car inside index 0: ")
del cars[0]
print(cars)

# # array deleting with remove
print("Below are the arrays after deleting the car called mazda")
cars.remove("mazda")
print(cars)