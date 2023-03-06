filename = "C:/Users/User/Desktop/KBTU/1st Year/2nd semester/School of Information Technologies/Principles of Programming II/Savoskin Roman/TSIS/tsis6/File Directories/Task4.py"
line_count = 0

with open(filename, "r") as file:
    for line in file:
        line_count += 1
rev_filename = filename[::-1]
ind = rev_filename.index('/')
index = len(filename)-ind
filenm = filename[index:]
print("The file", filenm, "contains", line_count, "lines.")
