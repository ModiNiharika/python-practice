from aopMenu import aopMenu
import sys
from operations import addop,subop,mulop,divop,modop,expop
aopMenu()
ch = int(input("Enter your choice "))
match(ch):
    case 1 :
        addop()
    case 2 : 
        subop()
    case 3 : 
        mulop()
    case 4 :
        divop()
    case 5 : 
        modop()
    case 6 :
        expop()
    case 7 :
        sys.exit()
