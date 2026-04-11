#Program for creating CSV File through python language

import csv
hname = ['EmpNo','Name','Sal']
records = [[100,'Rossum',4.5],
            [200,'Travis',5.6],
            [300,'Dennies',3.4]]
#Choose the file name and open it into write mode

with open("08_FileHandling/WorkingWithCSVFiles/Emp.csv",'w') as fp:
    csvwr = csv.writer(fp)
    csvwr.writerow(hname)
    #Write the records
    csvwr.writerows(records)
    print("CSV file created dynamically through code -- Verify")
