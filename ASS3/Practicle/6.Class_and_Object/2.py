# Write a Python program to demonstrate the use of local and global variables in a class.

class Student:
    name = 'pradyum' #Global Variable
    age = 20   #Global Variable

    def collage(self):
        clg='XYZ'  #Local Variable
        print(self.name,self.age,clg)

    def display(self):
        print(f'Name : {self.name}\nAge : {self.age}')

a=Student()
a.display()
a.collage()