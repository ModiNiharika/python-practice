# 90) Write a python program which will validate the name of the person or product or place which must be purely alphabets


from namevalid import validation
from names import InvalidNameError,ZeroLengthNameError
try : 
    name = input("Enter name/place/product: ")
    res = validation(name)
except ZeroLengthNameError :
    print("Invalid Input--Enter your name/place/product")
except InvalidNameError:
    print("Invalid name Try again")
else : 
    print(name)

