 import csv


class Item:
    @classmethod
    def instantiate_from_csv(cls):
        with open('C:/Users/gabri/OneDrive/Desktop/CODING/PYTHON_docs/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            
            #Strip leading and trailing spaces from keys
            item = {k.strip(): v for k, v in item.items()}
            print(f"Raw item data: {item}") #print raw item data

        
            name = item.get('name')
            if name is None:
                name = "Unknown"  # or some default value~

            quantity = item.get('quantity')
            if quantity is not None:
                quantity = int(quantity)
            else:
                quantity = 0  # or some default value
            print(f"Processed quantity: {quantity}") # print processed quantity

            price = item.get('price')
            if price is not None:
                price = float(price)
            else:
                price = 0.0  # or some default value
            print(f"Processed price: {price}") # print processed price
            Item(
                name = name,
                price = price,
                quantity = quantity,
            )
    
    @staticmethod
    def is_integer(num):
        '''We will count out the floats that are point zero
           For i.e: 5.0, 10.0
        '''
        
        if isinstance(num, float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    pay_rate = 0.8 #The pay rate after 20% discount
    all = []

    #Object construction
    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to  zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
    

    
        
    #Calculations   
    def calculate_total_price (self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    

#INSTANCES





#OUTPUTS
Item.instantiate_from_csv()
print(Item.all)
