import os

path = "C:\Users\User\Desktop\Example\Hello.py"

# List all directories in the path
print("Directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

# List all files in the path
print("Files:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)

# List all directories and files in the path
print("Directories and Files:")
for name in os.listdir(path):
    print(name)
