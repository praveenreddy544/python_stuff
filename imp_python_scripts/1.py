def rt():
    a=int(input("enter your a value "))
    b=int(input("enter your b value"))
    c=int(input("enter your c value"))
    return (a,b,c)
def sub(va,vl,vc=13):
    if vc == 13:
        valuecode=0
    else:
        valuecode=1
    return valuecode
while True:
    print("you are testing")
    x,y,z=rt()
    print("x value you got is ----------> ",x)
    print("y value you got  is ------->",y)
    print("z value you got is ----->",z)
    if x != 0 and y != 0 and z != 0:
        vc=sub(x,y,z)
        print("valuecode is ",vc)
    elif x == 0 or y ==0 or z == 0:
        print("you entered 0 value in x and hence exiting")
        break





