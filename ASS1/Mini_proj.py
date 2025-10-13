def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

def mul(num1,num2):
    return num1*num2

def mod(num1,num2):
    return num1%num2

print('-'*50)
print('*'*20,'Calculator','*'*20)

def cal():
    while True:
        print()
        print('-'*50)
        print('Enter 1 For Addition')
        print('Enter 2 For Subtraction')
        print('Enter 3 For Division')
        print('Enter 4 For Multiplication')
        print('Enter 5 For Module')
        print('Enter 6 For Exit')

        chioce = input('Enter Your Choice : ')

        if chioce == '6':
            print('*'*20,'ThankYou Visit Again','*'*20)
            break
        
        if chioce in ['1','2','3','4','5']:
            try:
                num1=float(input('Enter First Number : '))
                num2=float(input('Enter Second Number : '))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

                
            if chioce == '1':
                print(add(num1,num2))
            elif chioce == '2':
                print(sub(num1,num2))
            elif chioce == '3':
                print(div(num1,num2))
            elif chioce == '4':
                print(mul(num1,num2))
            elif chioce == '5':
                print(mod(num1,num2))
        else:
            print("Invalid choice! Please enter 1-5.")
cal()