"""
this is text that was referenced actually
"""
class testclass:
    "defining test class for test"
    count=22
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
       # testclass.count+=1
    def fname(self):
        #self.count += 1
        testclass.count+=1
        #print "count is %d" % testclass.count
        print "count is %d" %self.count
nc=testclass('chintu','reddy')
nc.fname()
nc.fname()
nc.fname()