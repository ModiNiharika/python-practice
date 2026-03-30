#Program for reading the data from the file using readlines
try:
    with open("file1.data") as fp:
        filedata=fp.readlines()
        print('-'*50)
        print(str(filedata))
        print('-'*50)
        print(type(filedata))
        print('-'*50)
        for line in filedata:
            print(line,end=' ')
        print('-'*50) 
except FileNotFoundError:
    print("File does not Exist")