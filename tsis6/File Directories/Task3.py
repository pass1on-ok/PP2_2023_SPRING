'''
import os

path = "C:/Users/User/Desktop/KBTU/1st Year/2nd semester/School of Information Technologies/Principles of Programming II/Savoskin Roman/TSIS/tsis6/File Directories"

if os.path.exists(path):
    print("Path exists")

    directory = os.path.dirname(path)
    print("Directory: ", directory)

    
    filename = os.path.basename(path)
    print("Filename: ", filename)

else:
    print("Path does not exist")
'''

import os
print("Test a path exists or not:")
path = r'C:/Users/User/Desktop/KBTU/1st Year/2nd semester/School of Information Technologies/Principles of Programming II/Savoskin Roman/TSIS/tsis6/File Directories/'
print(os.path.exists(path))
path = r'C:/Users/User/Desktop/KBTU/1st Year/2nd semester/School of Information Technologies/Principles of Programming II/Savoskin Roman/TSIS/tsis6/File Directories/'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))
