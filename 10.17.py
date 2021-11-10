#zachary blackwell 1941472

class ItemToPurchase:
    def __init__(self,name = "none", price= 0, quantity = 0 ):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@', "${}".format(self.item_price), '=', "${}".format(self.get_total_price()))

    def get_total_price(self):
        total = self.item_price * self.item_quantity
        return total
if __name__ == "__main__":
    item_1 = ItemToPurchase()
    print('Item 1')
    name = input("Enter the item name:\n")
    price = int(input("Enter the item price:\n"))
    quantity = int(input('Enter the item quantity:\n'))

    print()
    item_1.item_name = name
    item_1.item_price = price
    item_1.item_quantity = quantity

    item_2 = ItemToPurchase()
    print('Item 2')
    name = input("Enter the item name:\n")
    price = int(input("Enter the item price:\n"))
    quantity = int(input('Enter the item quantity:\n'))
    print()

    item_2.item_name = name
    item_2.item_price = price
    item_2.item_quantity = quantity

    print('TOTAL COST')
    total_price = item_1.get_total_price()
    info = item_1.print_item_cost()
    total_price2 = item_2.get_total_price()
    info2 = item_2.print_item_cost()

    print()

    total = item_1.get_total_price() + item_2.get_total_price()

    print('Total:', '${}'.format(total))