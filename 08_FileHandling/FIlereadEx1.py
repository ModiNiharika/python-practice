#Program for reading the data from the file
try:
    with open("file1.data") as fp:
        filedata=fp.read()
        print('-'*50)
        print(str(filedata))
        print('-'*50)
        print(type(filedata))
        print('-'*50)
except FileNotFoundError:
    print("File does not Exist")