from datetime import datetime

class Meditrack:
    def __init__(self):
        self.medicine_stock = {
                "Paracetamol": {"price": 20, "stock": 50},
                "Amoxicillin": {"price": 35, "stock": 30},
                "Cetirizine": {"price": 15, "stock": 40},
                "Dolo650": {"price": 25, "stock": 60},
                "Azithromycin": {"price": 50, "stock": 20}
            }
        self.customer_data = []
        
        
    def update(self):
        medi_name = input('Enter Medicine Name : ')
        if medi_name in self.medicine_stock:          
            print('1.Update price ')
            print('2.Update stock ')
            print('3.Update Both ')
            choice = input('Enter Your choice: ')
            if choice == '1':
                price = int(input('Enter new price : '))
                self.medicine_stock[medi_name]['price']=price
                
            elif choice == '2':
                stock = int(input('Enter new stock : '))
                old_stock = self.medicine_stock[medi_name]['stock']
                self.medicine_stock[medi_name]['stock'] = stock + old_stock
                
            elif choice == '3':
                price = int(input('Enter new price : '))
                stock = int(input('Enter new stock : '))
                old_stock = self.medicine_stock[medi_name]['stock']
                self.medicine_stock[medi_name]= {"price": price, "stock": stock+old_stock}
                
            else:
                 print('----- Invalid Number --------\n')
        else:
            print('--- Medicine is Not available for update please add medicine ----')
            
        
    
    
    def add(self):
        medi_name = input('Enter medicine name : ') 
        price = int(input('Enter Medicine price: '))  
        stock = int(input('Enter Medicine stock: '))
        
        self.medicine_stock[medi_name] = {'price':price,'stock':stock}
        
    def customer(self):
        c_name = input('Enter your Name : ')
        medi_name = input('Enter Medicine Name : ')
        
        if medi_name in self.medicine_stock:  
            stock = int(input('Enter Quantity : '))
            price = stock * self.medicine_stock[medi_name]['price']
            sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if stock <= self.medicine_stock[medi_name]['stock']:
                self.customer_data.append({
                    'name' : c_name,
                    'medicine_name' : medi_name,
                    'stock' : stock,
                    'price' : price, 
                    'date' : sale_date
                    
                })
                self.medicine_stock[medi_name]['stock'] -= stock
                # print('\n---------- Customer History ----------\n')
                # for key,value in self.customer_data.items():
                #     print(key,'-',value)
            elif stock == 0:
                print('\n--------- Stock is Not Available --------')
            else:
                print(f'\n------ only {self.medicine_stock[medi_name]['stock']} stock is Available -----')
        else:
            print('------- Medicine is Not Available -------')
            
        
    def persone_data(self):
        for data in self.customer_data:
            for key,value in data.items():
                print(key,'-',value)
                print()
                
            
        


m = Meditrack()

while True:
    print('\n------ Welcome to MediTrack Store -------\n')
    print('1. Enter 1 for Buy Medicine')
    print('2. Enter 2 for View Medicine')
    print('3. Enter 3 for Add Medicine')
    print('4. Enter 4 for See Customer History')
    print('5. Enter 5 for Exit')
    
    ch = input('Enter your choice : ')
    
    if ch == '1':
        print('---------------- Buying Medicine -------------------\n')
        m.customer()
    
    
    elif ch == '2':
        print('---------------- View Medicine -------------------\n')
        for key,value in m.medicine_stock.items():         
            print(key,'- Price : ',value['price'],'- Stock : ',value['stock'])
    
    elif ch == '3':
        print('---------------- Add Medicine -------------------\n')
        print('1.Add Medicine')
        print('2.Update Medicine')
        choice = input("Enter Your choice: ")
        if choice == '1':
            m.add()
        elif choice == '2':
            print('---------------- Update Medicine -------------------\n')
            m.update()

        else:
             print('----- Invalid Number --------\n')
    
    elif ch == '4':
        print('---------- Customer History ----------')
        m.persone_data()
        
    elif ch == '5':
        print('---------- Thank you For Visite ----------')
        break
    else:
        print('----- Invalid Number --------\n')