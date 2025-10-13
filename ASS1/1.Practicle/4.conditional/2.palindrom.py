#  Practical Example 6: Write a Python program to check if a number is prime using if_else.

num = int(input('enter number : '))
is_palindrome = True

for i in range(2,num):
    if num % i == 0:
        is_palindrome = False
        break
if is_palindrome == True:
    print(f'{num} is Palindrom')
else:
    print(f'{num} is not Palindrom')
