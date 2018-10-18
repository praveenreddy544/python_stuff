class first_class(object):
    value_mine = 0
    def __init__(self,name,value):
        self.name_value=name
        self.val_value=value
        #print('calling class first_class')
        first_class.value_mine+=1

    def dispval(self):
        print(f"value_mine is {first_class.value_mine}")
    def rva(self):
        return (self.name_value,self.val_value)
    def avr(self,num_giv):
        self.gcd=num_giv
        return self.gcd
a=first_class('pravee',1)
print(f"name givne ----> {a.name_value}")
a.dispval()
b=a.rva()
print(a.avr(3))


d=first_class('chintu',22)
d.dispval()
c=d.rva()
print(c)
#print(type(c))
