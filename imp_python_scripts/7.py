class emp:
    "this is first class in python"
    count=1
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        emp.count+=1
    def printcount(self):
        print "value of empcount is %d" % emp.count

    def pfl(self):
        print "firstname is", self.fname , "and lastname is", self.lname

a=emp("chintu","reddy")
a.printcount()
a.pfl()
b=emp("praveen","poredd")
b.printcount()
b.pfl()
print "value of emp count is %d" %emp.count
print "value of emp count is %d" %emp.count


