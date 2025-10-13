# Practical Example 4: Print this pattern using nested for loop:

# *
# **
# ***
# ****
# *****

num = int(input('Enter Row : '))
for i in range(1,num+1):
    for j in range(i):
        print('*',end=' ')
    print()