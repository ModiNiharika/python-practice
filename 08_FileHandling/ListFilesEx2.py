#Program for listing the files with extension only .ipynb

import os
try: 
    filenames = os.listdir("/home/user/Desktop/python-practice")
    print('-'*50)
    for filename in filenames :
        print(filename)
    print("Number of files in the folder are : ",len(filenames))
    print('-'*50)
    nop=0
    for filename in filenames:
        if(filename.endswith('.ipynb')):
            print(filename)
            nop=nop+1
    print("Number of ipynb files are ",nop)
except FileNotFoundError:
    print("Folder not Found") 