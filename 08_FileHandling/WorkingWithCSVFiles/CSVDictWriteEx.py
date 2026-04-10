#Program for creating csv file by using Dict Data

import csv
hname = ['eno','name','sal']
records = [{'eno':100,'name':'RS','sal':4.5},
          {'eno':110,'name':'TR','sal':9.5},
          {'eno':120,'name':'ES','sal':3.5},
          {'eno':130,'name':'TB','sal':4.5}]
with open("08_FileHandling/WorkingWithCSVFiles/Emp.csv","w") as fp:
    csvdwr = csv.DictWriter(fp,fieldnames=hname)
    csvdwr.writeheader()
    csvdwr.writerows(records)
    print("CSV File Created --- Verify")

