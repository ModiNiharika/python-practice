#Program for displaying the content of any file by accepting the file name
try:
    filename = input("Enter the file name: ")
    fp = open(filename,'r')
except FileNotFoundError:
    print("File does not exist")
else :
    filedata = fp.read()
    print('-'*50)
    print("Content of : {}".format(fp.name))
    print('-'*50)
    print(filedata)
    print('-'*50)