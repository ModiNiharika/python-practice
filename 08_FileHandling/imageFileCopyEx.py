# Program for copying an image
try: 
    with open ('sample1.png','rb') as rp:
        with open('img.png','ab') as wp:
            srcdata=rp.read()
            wp.write(srcdata)
            print("File copied")

except FileNotFoundError:
    print("Source file does not exist")