# Program for reading the records from the file (emp.data ) where it contains the employee records

import pickle
def readrecord():
    with open('emp.data','rb') as fp:
        print('---------------------------------------')
        while(True):

            try:
                record = pickle.load(fp)
                print(record,type(record))
            except EOFError:
                print('---------------------------------------')
                break