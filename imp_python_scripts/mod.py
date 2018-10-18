class fistclass:
    "This is first test class we are creating"
    empcount=0
    def __init__(self,name,salary):
        self.name=name,
        self.salary=salary
        fistclass.empcount += 1
    def displaycount(self):
        print("total count is %d" %fistclass.empcount)
    def dname(self):
        print(f"name is -->",{self.name},"salary is --->",{self.salary})
emp1=fistclass('chintu',2000)
emp1.displaycount()
emp1.dname()
emp2=fistclass('chintu',2000)
emp2.displaycount()
emp2.dname()
print(f"value of empcount is %d" %fistclass.empcount)