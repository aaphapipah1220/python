# make_archive digunakan untuk membuat arsip berkas

# import
from shutil import make_archive
import random

filename_zip = random.randrange(1, 5)

arsip = input("Input your file: ")
make_archive(f"{filename_zip}", "zip", arsip)