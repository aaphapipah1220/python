# len berfungsi untuk menghitung panjang (jumlah elemen) dari suatu object

# array declaration
myPets = ["dog", "cat", "rabbit", "hamster", "porcupine", "sheep"]
myLuckyNumber = [3, 17, 22, 35, 40]

# concatenation
print("Hi, there! my favorite pet is a " + myPets[1])
print(f"And some of my lucky numbers are {str(myLuckyNumber[0])} and {str(myLuckyNumber[2])}")

# length of array
totalPets = len(myPets)

print(f"currently I have {str(totalPets)} pets")