#Program for saving Dict data into the Json file

import json
nor = int(input("Enter how many dict object values u have : "))
if(nor<=0):
    print("Invalid Data")
else:
    with open("emp1.json",'a') as fp:
        print("----------------------------------")
        for i in range(1,nor+1):
            print("Enter {} Dict object data ".format(i))
            empno = int(input('Enter employee number '))
            ename = input("Enter employee name ")
            sal = float(input("Enter employee salary "))
            print('--------------------------------------')
            #Place the above values in dict 
            d = {}
            d['ENO'] = empno
            d['Name'] = ename
            d['Sal'] = sal

            #Dump object d into json file
            json.dump(d,fp)
            fp.write('\n')
            print("{} Emp Record saved in json file".format(i))