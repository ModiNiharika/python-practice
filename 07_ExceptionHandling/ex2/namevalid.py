from names import InvalidNameError,ZeroLengthNameError

def validation(name:str): #name = Guido Va2n Rossum
    if(len(name)==0):
        raise ZeroLengthNameError
    else:
        words = name.split() #words = [Guido ,Va2n , Rossum]
        res = False
        for word in words : 
            if(not word.isalpha()):
                res= True
                break
        if(res):
            raise InvalidNameError