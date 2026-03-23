
from multable import table
from Mutiexcept import ZeroError,NegNumError
while(True):
    try:
        n = int(input("ENTER VALUE FOR TABLE "))
        table(n)
    except ValueError:
        print("Don't enter alnums,strs,symbols and float value")
    except ZeroError:
        print("Don't enter zero")
    except NegNumError:
        print("Don't enter negative number")
    except:
        print("Try again")
    else:
        print("Thank you")
        break