import csv

class Admin:
    
    def __init__(self):
        self.username = 'Hotel@123'
        self.password = 'hotel@123'
        self.foodId = '1000'
        self.fields = ['Food_ID', 'Name', 'Quantity', 'Price', 'Discount', 'Stock']
        self.filename = 'food_data.csv'

        with open(self.filename, 'r+') as reader:
            read = csv.reader(reader)
            if self.fields != next(read, []):
                writer = csv.DictWriter(reader, self.fields)
                writer.writeheader()

    def admin_login(self, username, password):
        if username == self.username and password == self.password:
            return True
        else:
            return False
        

    def addFood(self):
        name = input("Please enter the item you would like to add: ")
        quantity = input("Please enter the quantity you would like to add: ")
        price = input("Please enter the price of item: ")
        discount = input("Enter discount for item: ")
        stock = input("Enter stock available for item: ")
        with open(self.filename) as fr:
            r = csv.reader(fr)
            self.foodId = 0
            for i in r:
                if len(i) > 0:
                    self.foodId = i[0]
        
        with open(self.filename, 'a', newline='') as file:
            food_item = [str(int(self.foodId)+1), name, quantity, price, discount, stock]
            writer = csv.writer(file)
            writer.writerow(food_item)
            print('Food Added Successfully')
            
    def displayList(self):
        with open(self.filename) as file:
            reader = csv.DictReader(file)
            print('Food_ID\t\tName\t\t\tQuantity\tPrice\t\tDiscount\tStock')
            for row in reader:
                print(row['Food_ID'],end='\t\t'),print(row['Name'],end='\t\t'),print(row['Quantity'],end='\t\t')
                print(row['Price'],end='\t\t'),print(row['Discount'],end='\t\t'),print(row['Stock'])

    def removeFood(self):
        foodid = input('Please enter the Food ID which you would like to remove :')
    
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader if row['Food_ID'] != foodid]

        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(rows)
    
        print(f"Food with ID {foodid} has been removed from the list.")

    def editFood(self):
        self.displayList()

        foodid = input('Please enter the Food ID which you would like to edit :')
        value = input('Choose what would you like to edit(i.e Name, Quantity, Price, Discount, Stock) :')
        new_value = input('Please enter the new value :')
        with open(self.filename, 'r+') as file:
            reader = csv.DictReader(file)
            rows = []
            for row in reader:
                if row['Food_ID'] == foodid:
                    row[value] = new_value
                rows.append(row)

        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(rows)
            print('Items updated successfully')
                
# obj = Admin()
# obj.addFood()
# obj.removeFood()
# obj.displayList()
# obj.editFood()