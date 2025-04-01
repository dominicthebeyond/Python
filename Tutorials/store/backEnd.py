class Product:
  def __init__(self, name, price):
    self.name = name
    self._price = price

  @property # Getter
  def price(self):
    # Accesses the price
    return self._price
  
  @price.setter
  def price(self, value):
    # Setter method to modify with validation.
    if value < 0:
      raise ValueError("Price cannot be negative!")
    self._price = value

  @price.deleter
  def price(self):
    # Deleter method to remove the price
    print("Deleting price...")
    del self._price

p = Product("Laptop", 1000)
p2 = Product("Iphone", 500)

print(f"Getter - {p.price}") # Getter method
print(f"Getter - {p2.price}") # Gets the original price

p.price = 1200 # Setter 
p2.price = 750 # setter

# p.price = -500 # Raises error from setter method.
# p2.price = -250

print(f"Setter after assigning value to getter = {p.price}") # 1200
print(f"Setter after assigning value to getter = {p2.price}")

del p.price # Deleter method
del p2.price # Delets ALL the price attribute (Including zero).
print("Price Deleted") # Prints once deleted
print("Price Deleted!")