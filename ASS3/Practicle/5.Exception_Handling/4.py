# Write a Python program to print custom exceptions.


class Custom_Error(Exception):
    pass

def age_check(age):
    if age < 18 :
        raise Custom_Error('Age is Must be Grater then 18')
    else:
        print('Access Granted')


try:
    age=int(input('Enter your age : '))
    age_check(age)
except Custom_Error as e:
    print('custome Error :',e)

