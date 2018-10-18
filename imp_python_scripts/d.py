#main_dicitonary={'praveen':'dec 23rd','fluty':'april 16th','naveen':'july 1'}
main_dicitonary={}
#print(main_dicitonary['praveen'])
#input_entered=input("Please enter name of:  ")
while True:
    input_entered = input("Please enter name of:  ")
    if input_entered == '':
        print("no inputer entered bro")
        break
    #for i in main_dicitonary:
    if input_entered in main_dicitonary:
        print(f"You entered {input_entered} and his birthday is -------------> {main_dicitonary[input_entered]}")
    else:
        birthday_date=input("Pls enter your birthday data: ")
        main_dicitonary[input_entered] = birthday_date
        print(f"Main dicitonary updated successfully")
        break
print(f"In overall , dictionary is -----> {main_dicitonary}")
#print(f"{main_dicitonary['praveen']}")


