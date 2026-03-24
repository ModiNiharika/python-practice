# Program for demonstrating how to access the data randomly from the file

#FilePointerObj tell()  --- Gives index of file pointer
#FilePointer.seek(Index)---will set file pointer to point to specified index
with open("sample.data",'r') as fp:
    print('---------------------------------')
    print("Initially,fp points to : ",fp.tell())
    filedata = fp.read(3)
    print("File Data = ",filedata)
    print("Now fp data points to : {}".format(fp.tell()))
    print('---------------------------------')
    filedata = fp.read(4)
    print("File Data = ",filedata.strip())
    print("Now fp points to : {}".format(fp.tell()))
    print('----------------------------------')
    filedata = fp.read(4)
    print("File Data = ",filedata.strip())
    print("Now fp points to : {}".format(fp.tell()))
    print('----------------------------------')

    #To reset the file pointer , we use seek()

    fp.seek(0)
    print("Now fp points to : {}".format(fp.tell()))
    print('-----------------------------------')
    
    #Read complete data from file

    filedata = fp.read()
    print("File Data : ",filedata)
    print("Now fp points after seek() to : {}".format(fp.tell()))

