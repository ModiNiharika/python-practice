#Program for reading employee values and save them as record in file

import pickle
def saverecord():
    with open("emp.data",'ab') as fp:
        while(True):
            #Accept the employee values from keyboard
            print('---------------------------------------')
            eno = int(input("Enter employee Number : "))
            ename = input("Enter the employee name : ")
            sal = float(input("Enter employee salary : "))
            dsg = input("Enter employee designation :")
            print('---------------------------------------')
            
            #Create an empty list and place employee details
            lst =list()
            lst.append(eno)
            lst.append(ename)
            lst.append(sal)
            lst.append(dsg)

            #Save or transfer lst data into the file
            pickle.dump(lst,fp)
            print("Employee Record saved in file sucessfully")
            print('---------------------------------------')
            ch = input("Do you want to insert another employee value(Yes/No) ")
            if(ch.lower()=='no'):
                print("Thanks for using this program")
                break