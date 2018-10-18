import sys
def fun():
    a=int(input("enter number: "))
    if a<10:
        raise ValueError('you entered less than 10 value')
    else:
        print(f"you entered --->{a}")
while True:
    fun()