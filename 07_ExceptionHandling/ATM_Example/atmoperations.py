
from atmexcept import DepositError,WithDrawError,InSufficientError
bal = 500.00
def deposit():
    global bal
    damt = float(input("Enter the deposit amount ")) #implicitly raises ValueError in the case alnums ,strs
    if(damt<=0):
        raise DepositError
    else : 
        global bal
        bal = bal + damt
        print("Your account xxxxx123 credited with INR : {}".format(damt))
        print("Current Balance {}".format(bal))
                 
def withdraw():
    global bal
    wamt = float(input("Enter the withdraw amount "))
    if(wamt<=0):
        raise WithDrawError
    elif(wamt>bal):
        raise InSufficientError
    else :
        bal = bal-wamt
        print("Your account xxxxx123 debited  with INR : {}".format(wamt))
        print("Current Balance {}".format(bal))
def balenq():
    print("Current Balance : {}".format(bal))
