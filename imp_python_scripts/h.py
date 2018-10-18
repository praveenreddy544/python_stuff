def fun(num):
    if num < 0:
        print("Blaw")
    else:
        print(num)
        fun(num-1)
a=int(input("enter your number: "))
fun(a)

