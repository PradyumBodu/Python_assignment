#  Practical Example 8: Write a Python program to check if a person is eligible to donate blood
# using a nested if.

age = int(input('Enter Age :- '))

if age>18:
    weight = int(input('Enter Weight :- '))
    if weight>=50:
        print('Eligible to donate blood')
    else:
        print('Not Eligible to donate blood')
else:
    print('Not Eligible to donate blood')