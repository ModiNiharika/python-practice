#Program for reading the data from CSV files
try:    
    with open("08_FileHandling/WorkingWithCSVFiles/Csv1.csv","r") as fp:
        csvdata = fp.read()
        print("CSV file data")
        print("-"*50)
        print(csvdata)
except FileNotFoundError:
    print("FIle does not exist")
