dictionary_database={'praveen':'dec 23','naveen':'july 1'}
#print(dictionary_database)
while True:
    input_name=input("enter your name: ")
    if input_name == '':
        break
    if input_name in dictionary_database:
        print(f"your birthday information is -----> {dictionary_database[input_name]}")
    else:
        date_input=input("enter date of your birthday: ")
        dictionary_database[input_name]=date_input
        print("Database updated accordingly")
        print(f"your new dictionary is {dictionary_database}")