#Program for reading the data from CSV file by using csv module --- in the form of Dictionary --- DictReader()

import csv
with open("08_FileHandling/WorkingWithCSVFiles/Csv1.csv","r") as fp:
    csvr=csv.DictReader(fp)  #Here csvr is an object of <class _csv.DictReader>
    print(type(csvr))
    for record in csvr:
        for k,val in record.items():
            print("{}---->{}".format(k,val) )
        print()
        print('-'*50)