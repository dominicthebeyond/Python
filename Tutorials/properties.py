# @property = Decorator used to define a method as a property (it can be accessed like an attribute
# Benefit: Add additional logic when read, write, or delete attributes.
# Gives you getter, setter, and deleter method.

class Rectangle:
  def __init__(self, width, height):
    self._width = width
    self._height = height # Protected Attributes. Shouldn't access attributes outside class.

    @property
    def width(self):
      return f"{self._width:.1f}cm"
    
    @property
    def height(self):
      return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
      if new_width > 0:
        self._width = new_width
      else: 
        print(f"Width must be greater than zero")

    @height.setter
    def height(self, new_height):
      if new_height > 0:
        self._height = new_height
      else: 
        print(f"height must be greater than zero")

    @width.deleter
    def width(self):
      del self._width
      print("Width has been deleted")

    @height.deleter
    def height(self):
      del self._height
      print("height has been deleted")

rectangle = Rectangle(10, 20)

rectangle.width = 30
rectangle.height = 15

del rectangle.height
del rectangle.width

