import os

path = "C:/Users/User/Desktop/KBTU/1st Year/2nd semester/School of Information Technologies/Principles of Programming II/Savoskin Roman/TSIS/tsis6/File Directories/"

if os.path.exists(path):
    print("Path exists")

    if os.access(path, os.R_OK):
        print("Path is readable")
    else:
        print("Path is not readable")

    if os.access(path, os.W_OK):
        print("Path is writable")
    else:
        print("Path is not writable")

    if os.access(path, os.X_OK):
        print("Path is executable")
    else:
        print("Path is not executable")

else:
    print("Path does not exist")
