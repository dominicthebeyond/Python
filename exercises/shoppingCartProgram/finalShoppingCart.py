class ShoppingCart: 
  def __init__(self):
    self.items = []

  def add_items(self, name, price):
    self.items.append({"name": name, "price": price})
    print(f"Name - {name}, price - ${price}")

  def remove_items(self, name):
    for item in self.items:
      if item["name"] == name:
        self.items.remove(item)
        print("Removed item successfully.")

  def view_items(self):
    for item in self.items:
      print(item)
  
  def calculate_total_price(self):
    total = 0
    for item in self.items:
      total += item["price"]
    print(total)

c1 = ShoppingCart()

c1.add_items("Laptop", 1200) # Name - Laptop, price - $1200
c1.add_items("Mouse", 50) # Name - Mouse, price - $50

c1.view_items() # both items

c1.calculate_total_price() # $1250

c1.remove_items("Mouse") # Laptop is only one left in cart