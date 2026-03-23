
from atmexcept import DepositError,WithDrawError,InSufficientError
from atmenu import menu
from atmoperations import deposit,withdraw,balenq
import sys
while(True):
    try:
        menu()
        ch = int(input("Enter Ur choice "))
        match(ch):
            case 1 : 
                try:
                    deposit()
                except ValueError:
                    print("Don't try to deposit alnums and str and symbols and Try again")
                except DepositError:
                    print("Don't try to deposit zero or nagative ")

            case 2 : 
                try :
                    withdraw()
                except ValueError:
                    print("Invalid Withdraw---Try again")
                except WithDrawError:
                    print("Don't try to withdraw negative values ---Try again")
                except InSufficientError:
                    print("Insufficient Balance --- Try again")
                    
            case 3 : 
                balenq()
            case 4 : 
                print("Thanks for using this program")
                sys.exit()
            case _:
                print("Try again")
    except ValueError:
        print("Don't enter alnums , symbols ,strs and floats")