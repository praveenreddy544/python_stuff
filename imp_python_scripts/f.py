'''def calc(num):
    try:
        if num > 9:
            print(f"you provided num as ---->{num}")
    except:
        print("you provided not an int type")

a=calc(10)
b=calc('this')
'''
'''import json
import os
a=float(input("enter no"))
print(a)

with open('test_pra','w') as f:
    json.dump(a,f)

path_of_file=os.path.abspath("test_pra")
print(path_of_file)
with open('test_pra','r') as j:
    m=j.read()

print(f"you supplied data is {m}")
'''

#num=int(input("enter your desired number"))
"""try:
    raise ValueError('x should not be less than 10!')
except ValueError:
    print('There was an exception.')
"""
x=int(input("enter number"))
if x < 10:
    raise ValueError('x should not be less than 10!')