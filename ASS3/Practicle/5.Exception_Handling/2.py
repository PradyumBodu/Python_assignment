# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

try:
    # a=10
    # b=0
    # print(a/b)
    with open('test.txt','r') as f:
        print(f.read())
except FileNotFoundError:
    print('File Not Found')
except ZeroDivisionError:
    print('Not Divide By Zero')