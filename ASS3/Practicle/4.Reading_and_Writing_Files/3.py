# Write a Python program to check the current position of the file cursor using tell().

with open('test1.txt','r') as f:
    print(f.tell())
    print(f.read())
    print(f.tell())