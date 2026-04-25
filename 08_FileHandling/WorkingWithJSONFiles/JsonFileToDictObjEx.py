#Program for reading json file data into dict object
import json
try :
    with open("/home/user/Desktop/python-practice/std.json",'r') as fp:
        d = json.load(fp)
        print(d,type(d))
except FileNotFoundError:
    print("Json file does not exist")