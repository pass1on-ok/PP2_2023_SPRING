my_list = ["apple", "banana", "orange", "pear"]
filename = "C:/Users/User/Desktop/KBTU/1st Year/2nd semester/School of Information Technologies/Principles of Programming II/Savoskin Roman/TSIS/tsis6/File Directories/Task5.txt"

with open(filename, "w") as file:
    for item in my_list:
        file.write(item + "\n")
rev_filename = filename[::-1]
ind = rev_filename.index('/')
index = len(filename)-ind
filenm = filename[index:]
print("List written to file", filenm)
