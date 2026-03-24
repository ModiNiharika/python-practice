import shares
import importlib
import time
def dispshares(d):
    print('-'*50)
    print("\tShareName\tShareValues")
    print('-'*50)
    for sn,sv in d.items():
        print('\t{}\t\t{}/'.format(sn,sv))
    print('-'*50)
d = shares.sharesinfo()
dispshares(d)
print("Sleeping")
time.sleep(15)
print('Waked Up')
importlib.reload(shares)
d = shares.sharesinfo()
dispshares(d)


