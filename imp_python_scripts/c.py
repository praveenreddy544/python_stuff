'''import random
secret_number=random.randint(1, 10)
#for i in range(1,5):
while True:
    input_given_number=int(input("Enter your number "))
    if input_given_number == secret_number:
        print(f"You entered input as ---> {input_given_number} that is matching secretnumber which is ----> {secret_number}")
        break
    elif input_given_number <secret_number:
        print(f"Your entered input is less that secret number")
    elif input_given_number>secret_number:
        print(f"Your entered input is greater than secret number")
    else:
        print(f"Sorry! no input entered Yo")
'''

class test:
    def __init__(self,name,value):
        self.val=name
        self.dem=value
    def fun(self,param):
       # self.val=param
        drr=param
        #return self.val
        return drr
    @classmethod
    def classa(cls):
        print(f'class method')
te=test('chintu',2000)
te.classa()
a=te.fun('praveen reddy')
print(a)