# Car rental system
# Disply available cars
# Request a car for rent (1000 Rs --> 1 Qty)
# Exit

class CarShop:
    def __init__(self, stock):
        self.stock = stock
        print(id(self.stock))

    def rent_for_cars1(self, quan1):
        if quan1 < 1:
            print("Enter positive value/Greater than zero!")
        elif quan1 > self.stock:
            print("Enter value less than stock")
        else:
            self.stock -= quan1            
            print("Total Price:", quan1*1000)
            print("Total cars left:", self.stock)
        print(id(self.stock))


    def display_cars1(self):
        print("Total cars is:", self.stock)
        print(id(self.stock))

ob1 = CarShop(120)

while True:
    uc1 = int(input('''
1. Display Stock
2. Rent a car
3. Exit

Enter your choice:- '''))
    if uc1 == 1:
        ob1.display_cars1()
    elif uc1 == 2:
        n1 = int(input("Enter the number of cars: "))
        ob1.rent_for_cars1(n1)
    elif uc1 == 3:
        break
    else:
        print("Invalid choice........................!")