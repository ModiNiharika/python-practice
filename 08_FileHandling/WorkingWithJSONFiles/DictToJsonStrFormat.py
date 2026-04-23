#Program for converting Dict object into Json string format

d1 = {"ENO":100 , "Name":"Rossum","Sal":10213}
print(d1,type(d1))
print('-----------------------------------------------')
# Convert Dict object data into jason str format
jsonfmt = str(d1)
print("Json Data = ",jsonfmt)
print(type(jsonfmt))
print('-----------------------------------------------')
