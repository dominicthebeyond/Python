class Country:
  def __init__(self, country):
    self.country = country

class Car: 
  def __init__(self, brand, year):
    self.brand = brand
    self.year = year

  def drive(self):
    return f"{self.brand} says vbroom VROOM!"

class Honda(Car, Country):

  def __init__(self, licenseNum, model, engine):
    self.licenseNum = licenseNum
    self.model = model
    self.engine = engine
    Car.brand = "Honda"
    Car.year = 2012
    Country.country = "America"

  def drive(self):
    print(f"{self.brand} {self.model} goes vroom vroom!")
    print(f"Made in {self.country}")