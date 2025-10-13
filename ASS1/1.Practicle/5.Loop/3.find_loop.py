# Practical Example 3: Write a Python program to find a specific string in the list using a simple
# for loop and if condition.

List1 = ['apple', 'banana', 'mango']
fruit = 'Mango'
is_exciest=False

for i in List1:
    if fruit == i:
        is_exciest=True
if is_exciest == True:
    print(f'{fruit} is in List')
else:
    print(f'{fruit} is not in List')