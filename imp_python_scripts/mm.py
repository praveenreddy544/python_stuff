'''class data:
    "this is testing class"
    number=22
    print(f"test data")
    def a(self,num):
        return self.number
d=data()
b=d.a(10)
print(b)'''

'''class test:
    def __init__(self,n):
        self.name=n
    def change_name(self,var):
        self.name=var
        return self.name

a=test('chintu')
print(a.name)
b=a.change_name('reddy')
print(b)
'''

'''class demo:
    value_given=False
    def __init__(self,name,salary,list_passed):
        self.name=name
        self.salary=salary
        self.list_passed=list_passed
    def testing(self,a,b):
        self.name=a
        self.value=b
        print(f"Calling for testing function")
        return (self.name,self.value)
    def split_string(self):
        string_choosen=self.name
        for i in string_choosen:
            print(i)
    def square_num(self,num):
        return num*num
    def list_convertion(self):
        lc=self.list_passed
        print(f"Before replacing list provided is {lc}")
        lc.reverse()
        return lc
        print(f"after replacing list provided is {lc}")

test1=demo('praveen',1000,[1,2,3,4])
print(test1.name)
print(test1.salary)
function_returned_value1,function_returned_value2=test1.testing('chintu',2000)
c=test1.split_string()
d=test1.square_num(12)
e=test1.list_convertion()
print(f"name is ----------> {function_returned_value1}\n with salary is ----------> {function_returned_value2}")
print(f"square_num value returned is {d}")
print(e)
'''

'''class parent:
    vol=20
    a=12
    def fun(self):
        print(f"this is ----------> parent")

class child(parent):
    def fun(self):
        print(f"Yo! this is child")
        print(parent.vol)
        print(parent.a)
c=child()
c.fun()
'''

class test:
    def __init__(self,a):
        self.name=a
        print(f"{self.name}")
instance1=test('chintu')
instance2=test('praveen')



