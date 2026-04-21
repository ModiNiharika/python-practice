# Program for saving dict data into json file

import json
#Take dict object data
d1 = {"Sno":100,"Name":"Niharika","Marks":9.8}

#Save the dict data into Json file
with open("std.json",'a') as fp:
    json.dump(d1,fp)
    print("Dict data written to the json file")