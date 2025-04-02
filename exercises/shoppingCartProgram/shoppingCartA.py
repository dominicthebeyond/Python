class ShoppingCart:
  def __init__(self):
    self.items = []

  def add_product(self, productName, price):
    self.items.append({"Name": productName, "price": price})
    print(f"{productName} added to the cart! It costs ${price}.") # Debugging purposes
    return
  
  def view_cart(self):
    for item in self.items:
      print(str(item))

c1 = ShoppingCart()

c1.add_product("Laptop", 1200)
c1.add_product("Mouse", 50)
c1.view_cart()