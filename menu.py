
class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
       self.items = [] # stores a list of MenuItems
    
    def find(self, name: str):
        for item in self.items:
            if item.name == name:
                return item
    
    def add(self, name: str, price: float):
        for item in self.items:
            if name == item.name:
                item.price = price
                break
        else:
            self.items.append(MenuItem(name, price))  

    def print(self):
        print('TODAY\'S MENU:', end = '\n')
        for item in self.items:
            print(f"  {item.name:<24}  {f'${item.price:.2f}':>8}", end='\n')