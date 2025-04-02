class ShoppingCart:
  def __init__(self):
    self.items = []

  def add_product(self, name, price):
    self.items.append({"Name": name, "price": price})
    print(f"{name} added to the cart! It costs ${price}.") # Debugging purposes
    return
  
  def view_cart(self):
    for item in self.items:
      print(str(item))

  def remove_product(self, name):
    print('Removing items...')
    for item in self.items:
        if item["Name"] == name:
            self.items.remove(item)
            print(f"{name} removed from the cart!")
            break
    else:
        print(f"{name} not found in the cart.")
    
    self.view_cart()


c1 = ShoppingCart()

c1.add_product("Laptop", 1200)
c1.add_product("Mouse", 50)

c1.view_cart()

c1.remove_product("Jimmy Carter")
