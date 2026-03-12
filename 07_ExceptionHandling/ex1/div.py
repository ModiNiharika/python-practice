#program for division of two numbers
#Here two Number are coming from different program
from Ex1 import DivisionByZeroError
def divop(a,b):
    if(b==0):
        raise DivisionByZeroError
    else:
        return(a/b)
    
#Phase -2 : We Develop problem solving logic and we hit exception if possible in the case of wrong input we give output in the case of valid input
