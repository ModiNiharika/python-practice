#Program for creating dynamic csv file --- Dictionary

import csv
noc = int(input("Enter no of columns you want in csv file "))
if(noc <= 0):
    print("Invalid number of columns")
else :
    hnames = list()
    for i in range(1,noc+1):
        colname = input("Enter {} column name ".format(i))
        hnames.append(colname)
    else:
        nor = int(input("Enter how many records you want to enter "))
        if(nor <=0):
            print("Invalid number of records")
        else:
            records = [] #For storing multiplerecords 
            for i in range(1,nor+1):
                print("Enter {} record data ".format(i))
                print("-"*50)
                record = {} #For storing single records
                for colname in hnames:
                    val = input("Enter value for {} ".format(colname))
                    #Add (colname,val)
                    record[colname]=val
                records.append(record)
                print('-'*50)
            else :
                #Choose the CSV file and open it into write mode
                csvfilename = input("Enter the csv file name :")
                if(not csvfilename.endswith(".csv")):
                    print("Please enter correct file name")
                else : 
                    with open("08_FileHandling/WorkingWithCSVFiles/"+csvfilename,"w") as fp:
                        csvwr = csv.writer(fp)
                        csvwr.writerow(hnames)
                        csvwr.writerows(records)
                        print("CSV File created")
                        print(hnames)
                        print(records)




