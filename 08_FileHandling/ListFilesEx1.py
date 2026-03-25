#Program for listing the files

import os
try: 
    filenames = os.listdir("/home/user/Desktop/python-practice")
    print('-'*50)
    for filename in filenames :
        print(filename)
    print("Number of files in the folder are : ",len(filenames))
    print('-'*50)
except FileNotFoundError:
    print("Folder not Found")