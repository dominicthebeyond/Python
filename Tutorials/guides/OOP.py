class Item:
  pay_rate = 0.8
  all = []
  def __init__(self, name, price, quantity):

    assert price >= 0, f"Price {price} is not greater than 0"
    assert quantity >= 0, f"Quantity {quantity} is not greater than 0"

    self.name = name
    self.price = price
    self.quantity = quantity

    # Appends all instances (items) to the all list.
    Item.all.append(self)

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * Item.pay_rate
  
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
