#Program for counting number of lines word and chars in the file 

try :
    filename = input("Enter file name : ") 
    with open(filename,'r') as fp:
        nol = 0
        now = 0
        noc = 0
        lines = fp.readlines()
        for line in lines:
            nol+=1
            now = now + len(line.split())
            noc = noc + len(line)
        else : 
            print('----------------------')
            print("Number of lines = ",nol)
            print('Number of words = ',now)
            print('Number of chars :',noc)
            print('----------------------')
except FileNotFoundError:
    print('File does not exist')
