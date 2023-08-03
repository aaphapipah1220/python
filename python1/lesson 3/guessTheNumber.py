# fungsi random untuk menghasilkan bilangan acak
# fungsi randrange untuk menghasilkan bilangan bulat acak sesuai dengan argumen yang diberikan
# print untuk memunculkan/menampilkan
# input untuk memasukan nilai

# sample for import
import random

# sample for variables
myNumber = random.randrange(1, 10)

# print statement
print("Hmm.. I am thinking of a number between 1 to 10..")
print("Saya lapar sekali..")

# input
answer = input("can you guess what that number is? ")
nama = input("Tuliskan nama anda.. ")

# output and comparison
print("That answer isss...")
print(myNumber == int(answer))
print("Sorry "+str(nama) + " the answer is: "+str(myNumber))