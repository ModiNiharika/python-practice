#Program for adding Record to the existing file through python language
import csv
record = [400,'KVR',10.2]
with open("08_FileHandling/WorkingWithCSVFiles/Emp.csv",'a') as fp:
    csvwr = csv.writer(fp)
    csvwr.writerow(record)
    print("Record added to Emp.csv file")
    