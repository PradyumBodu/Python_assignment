# Practical Example 1: How does the Python code structure work?

# python run line by line top to bottom
# here a=10 and b=20 and print(a+b), code run line by line and print addition of number that is 30

a=10
b=20
print(a+b)


# --------------------------------------------------------------------------------------------------------------------------------

# Practical Example 2: How to create variables in Python?

# simply we take name for any data and store that data in the varible 
# like here we take num as a variable and store value in num variable

num=20
print(num)

# --------------------------------------------------------------------------------------------------------------------------------


# Practical Example 3: How to take user input using the input() function.

# Just use input() function to take input for ex,

num = input('Enter Anything : ')

# here we take input and store in num variable and always input come in str by default so if we change in type of input we do type conversion.

# ------------------------------------------------------------------------------------------------------------------------------------------------

#  Practical Example 4: How to check the type of a variable dynamically using type().

# use type() function

a=10
print(type(a))
print(type(10.5))
print(type(True))
print(type('hello'))
print(type([10,20]))