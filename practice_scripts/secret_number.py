import random
secret_number=random.randint(1,10)
#print(a)
while True:
    inputted_number=int(input("enter your number: "))
    if inputted_number == secret_number:
        print("Yay! your number matched secret number")
    elif inputted_number > secret_number:
        print("huh! Looks like your inputted number is greater than secret number")
    elif inputted_number < secret_number:
        print("aww! Your input number is less than input number")

