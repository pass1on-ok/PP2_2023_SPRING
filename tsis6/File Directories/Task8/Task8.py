import os


file_path = "C:/Users/User/Desktop/KBTU/1st Year/2nd semester/School of Information Technologies/Principles of Programming II/Savoskin Roman/TSIS/tsis6/File Directories/Task8/Target.txt"


if os.path.exists(file_path):
    
    
    if os.access(file_path, os.R_OK):
        
       
        os.remove(file_path)
        print("File {file_path} has been deleted successfully.".format(file_path=file_path))
        
    else:
        print("You do not have access to the file {file_path}.".format(file_path=file_path))
        
else:
    print("The file {file_path} does not exist.".format(file_path=file_path))
