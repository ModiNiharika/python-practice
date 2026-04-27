#Program for converting JSON string format into Dict object

import json
jsonfmt = '{"ENO":"100","Name":"Rossum","Sal":"5.6"}'
print("Type of jsonfmt = ",type(jsonfmt)) #str type

#Convert json str format into dict object using loads() of json module
d1 = json.loads(jsonfmt)
print(d1,type(d1))
print('-------------------------------------------')
print("Dict Data converted from json str format")
print('-------------------------------------------')

for fn,fv in d1.items():
    print("{} -- {}".format(fn,fv))