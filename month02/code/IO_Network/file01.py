import time
import os
import sys

with open("file01.txt", "r") as f:
    str = f.read()
    print(len(str))

print(sys.path)
print(os.path.getsize("file01.txt"))
print(os.listdir("../Data_structure"))
print(os.path.isfile("file01.txt"))

