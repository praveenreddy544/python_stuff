def input_info():
    name=str(input("enter your name: "))
    age=float(input("enter your age: "))
    weight=float(input("enter your weight: "))
    system=str(input("enter your desired metrics: "))
    return (name,age,weight,system)

def calculate_bmi(weight,age,system='metrics'):
    if system.startswith('m'):
        bmi=(weight*age)
    else:
        bmi=(weight*age)/2
    return bmi

while True:
    (name_inputted,age_inputted,weight_inputted,system_inputted)=input_info()
    print(f"your name give is ----> {name_inputted}")
    print(f"your age given is ---> {age_inputted}")
    print(f"your weight given is ---> {weight_inputted}")
    print("\n")
    if name_inputted == 'chintu':
        break
    bmi_returned_value=calculate_bmi(weight=weight_inputted,age=age_inputted,system=system_inputted)
    print(f" bmi value given is ---->{bmi_returned_value}")
