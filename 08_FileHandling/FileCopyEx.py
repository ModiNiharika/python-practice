#Program for copying the content of one file into another file

try: 
    srcfile = input("Enter the source file : ")
    with open (srcfile,'r') as rp:
        dstfile=input("Enter Destination file: ")
        with open(dstfile,'a') as wp:
            srcdata=rp.read()
            wp.write(srcdata)
            print("File copied")

except FileNotFoundError:
    print("Source file does not exist")