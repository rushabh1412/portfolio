class Customer:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("We are out of stock!")
        else:
            print("We don't have that product!")

    def print_purchases(self):
        print("The customer has purchased:")
        for item in self.purchases:
            print(item.name)


class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.inventory = {}
    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity
    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + ':' + str(value))
        print()

customer = Customer('RJ','rj@gmail.com')
# print(customer.name)
# print(customer.email)

mouse = Product('Mouse',290)
# print(mouse.name)
# print(mouse.price)

keyboard = Product('keyboard',399)
print(keyboard.name)
print(keyboard.price)

inventory = Inventory()
inventory.add_product(mouse,100)
# inventory.print_inventory()
inventory.add_product(keyboard,289)

inventory.print_inventory()
customer.purchase(inventory, mouse)
customer.purchase(inventory, keyboard)
inventory.print_inventory()
customer.print_purchases()
