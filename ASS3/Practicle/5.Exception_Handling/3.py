# Write a Python program to handle file exceptions and use the finally block for closing the file.


try:
    with open('test.txt','r') as f:
        print(f.read())
except FileNotFoundError:
    print('File Not Found')
finally:
    print('Thank you!')