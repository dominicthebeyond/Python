class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def display_info(self):
    print(f'Name - {self.name}, Price - ${self.price}')

p1 = Product("Laptop", 1200)
p2 = Product("Mouse", 50)

p1.display_info()
p2.display_info()