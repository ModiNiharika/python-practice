#Program for reading the data from CSV file by using csv module

import csv
with open("08_FileHandling/WorkingWithCSVFiles/Csv1.csv","r") as fp:
    csvr=csv.reader(fp)  #Here csvr is an object of <class _csv.reader>
    print(type(csvr))
    for record in csvr:
        for val in record:
            print("{}".format(val),end='\t')
        print()