import os

path = "C:/Users/User/Desktop/KBTU/1st Year/2nd semester/School of Information Technologies/Principles of Programming II/Savoskin Roman/TSIS/tsis6/File Directories/"


items = [name for name in os.listdir(path)]

print("Items in {}:".format(path))
for item in items:
    print(item)
