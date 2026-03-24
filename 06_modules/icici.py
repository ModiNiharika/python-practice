bname = 'ICICI'
addr = 'Sklm'
def simpleint():
    p = float(input("Enter principle amount "))
    t = float(input("Entr time "))
    r = float(input("Enter rate of Interest "))
    si = (p*t*r)/100
    totamt = p + si
    print('-'*50)
    print("Principle amount : ",p)
    print("Time : ",t)
    print("Rate of interest : ",r)
    print("Interest : ",si)
    print("Total amount to be paid ",totamt)
    print('-'*50)
