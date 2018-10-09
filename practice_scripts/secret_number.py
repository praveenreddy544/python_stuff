import random
secret_number=random.randint(1,10)
#print(f"secret number generated is ------> {secret_number}")
for i in range(3):
    guess_number=int(input("enter your guess number"))
    if guess_number == secret_number :
        print("your guessed number matched with secret number")
    elif guess_number < secret_number:
        print("your guessed number is less than secret number")
    elif guess_number > secret_number:
        print("your guessed number is more than secret number")

