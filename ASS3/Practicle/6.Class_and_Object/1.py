# Write a Python program to create a class and access the properties of the class using an object.
class Student:
    name = 'pradyum'
    age = 20
    def display(self):
        print(f'Name : {self.name}\nAge : {self.age}')

a=Student()
a.display()