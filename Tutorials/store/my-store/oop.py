class Product:
  def __init__(self, name, price):
    self.name = name
    self._price = price

  @property
  def price(self):
    # Getter
    return self._price
  
  @price.setter
  def price(self, value):
    # Setter checks for error
    if value < 0:
      raise ValueError("Value CANNOT be negative on a product!")
    self._price = value

  @price.deleter
  def price(self):
    print("Deleting price")
    del p._price

p = Product("iPad", 200) # instance

print(p.price) # Getter

p.price = 400 # Setter

print(p.price) # Setter new price

print("Sold out... Deleting product from shelf")

del p.price
print("Product Deleted")



