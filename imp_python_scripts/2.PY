class testing:
    "This is for testing class concepts"
    a=3
    def __init__(self,firstname,lastname): ############# These is main class deinfition. Here, i am declaring two params to be needed and then will make use of those params
        self.name_given_firstname=firstname ################ You can re-use these params anywhere in ur code
        self.name_given_lastname=lastname   ################### You can re-use these params anywhere in ur code
        testing.a += 1
    def fun_a(self,number=12):
        print(f"fistname is ----> {self.name_given_firstname} and lastname is ---> {self.name_given_lastname}")
        #return number*number
    def fun_b(self,c,d):
        return c*d

test=testing('chintu','reddy')
test.fun_a()
#z=test.fun_a(10)
#print(z)
y=test.fun_b(25,25)
print(y)
print(f"value of  value is  ---> {testing.a}")
test1=testing('chintu','reddy')
print(f"value of  value is  ---> {testing.a}")

