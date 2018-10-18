class test:
    '''var="checking at class level"
    def call_back(self,msg):
        di={}
        for character in msg:
            di.setdefault(character,0)
            di[character]+=1
        print(di)
ins=test()
ins.call_back('praveen poreddy')
    '''
    def define_values(self):
        length=int(input("enter lenght of your laptop: "))
        width=int(input("enter width of your laptop: "))
        height=int(input("enter height of your laptop: "))
        return (length,width,height)
    def cal_value(self,length,width,height=12):
        if height==12:
            return (length*width*height)
        else:
            return (length*width*height*100)

ins=test()
(i,j,k)=ins.define_values()
print(f"you got ---> {i} and value is ---> {j} and k is ---> {k}")
m=ins.cal_value(i,j,k)
print(m)

ins2=test()
(i,j,k)=ins2.define_values()
print(f"you got ---> {i} and value is ---> {j} and k is ---> {k}")
n=ins2.cal_value(i,width=j,height=k)
print(n)