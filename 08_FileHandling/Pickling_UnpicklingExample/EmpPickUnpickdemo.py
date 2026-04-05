
from EmpPickUnPickMenu import menu
from EmpPickEx2 import saverecord
from EmpUnPicklingEx1 import readrecord
while(True):
    try:
        menu()
        ch = int(input("Enter your choice : "))
        match(ch):
            case 1 : 
                saverecord()
            case 2 : 
                readrecord()
            case 3 :
                print("Thank you for using")
                break
            case _:
                print("Your selection of operation is wrong -- Try again")
    except ValueError:
        print("Don't enter alnums ,str, symbols and float values ")