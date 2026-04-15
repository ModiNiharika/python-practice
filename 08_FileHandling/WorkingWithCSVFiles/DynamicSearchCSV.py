#Program for finding details about those people who are living in AP
#Use data.csv file
import csv
with open("08_FileHandling/WorkingWithCSVFiles/data.csv",'r') as fp:
    csvr=csv.reader(fp)
    hname = next(csvr)
    for name in hname:
        print(name,end='\t\t')
    print()
    print('-'*50)
    for record in csvr:
        if(record):
            for val in record:
                print(val,end='\t\t')
            print()
    print('-'*50)
    ano = input("Enter your sid ")
    fp.seek(0)
    csvr = csv.reader(fp)
    res = False
    for record in csvr:
        if(record):
            if(ano == record[0]):
                res = True
                break
    if(res):
        print("Your details are")
        print(record)
    else:
        print("Invalid sid")