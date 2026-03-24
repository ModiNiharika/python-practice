#program for obtaining the DIvision of two numbers
from div import divop
from Ex1 import DivisionByZeroError
try : 
    a = int(input("Enter first value:"))
    b = int(input("ENter second value:"))
    try:
        res = divop(a,b)
    except DivisionByZeroError: 
        print("Don't enter zero in the denominator")
    else : 
        print("Div({},{})={}".format(a,b,res))
except ValueError:
    print("Don't enter alnums , strs and symbols")
finally : 
    print("I am from finally Block")
    print("Program Excecution completed")

#Phase-3 : We develop a specific program and handling the exception if it occurs otherwise we displayed the result

