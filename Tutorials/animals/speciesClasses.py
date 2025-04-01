class Animal:
  def __init__(self, species, soundOfAnimal):
    self.species = species
    self.soundOfAnimal = soundOfAnimal

  def sound(self):
    print(f"The {self.species} goes {self.soundOfAnimal}")

class Sheep(Animal):
  def __init__(self, name, race):
    super().__init__("Sheep", "Baa")
    self.name = name
    self.race = race

  def sound(self):
    print(f"The {self.species} goes {self.soundOfAnimal}")

class Dog(Animal):
  def __init__(self, name, race):
    super().__init__("Dog", "Woof!")
    self.name = name
    self.race = race