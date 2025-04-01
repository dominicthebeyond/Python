# class Dunders:
#   def __init__(self, name, book, pages):
#     self.name = name
#     self.book = book
#     self.pages = pages

#   def __str__(self): # String Dunder - Returns a string in the terminal.
#     return f"'{self.book}' - {self.pages}" # Returns book and it's page amount.
  
#   def __eq__(self, other): # == dunder. Tests to see if defined attributes are equal in the books.
#     return self.book == other.book and self.name == other.name
  
#   def __lt__(self, other): # less than dunder (<) - Tests to see if first argument is less than second argument.
#     return self.pages < other.pages
  
#   def __gt__(self, other): # greater than dunder (>) - Tests to see if first argument is greater than second argument.
#     return self.pages > other.pages
  
#   def __add__(self, other): # Adds two arguments for different instances
#     return self.pages + other.pages
  
#   def __contains__(self, keyword): # Looks for if the keyword is in a book (or whatever attribute that was defined earlier in the initializer)
#     return keyword in self.book
  
#   def __getitem__(self, key):
#     if key == "book":
#       return self.book
#     elif key == "author":
#       return self.name
#     elif key == "Number of Pages":
#       return self.pages

  
# book1 = Dunders("J.K Rowling", "Harry Potter", 280)
# book2 = Dunders("J.R.R Tolkien", "The Hobbit", 310)
# book3 = Dunders("C.S Lewis", "The Lion, The Witch, The Wardrobe", 170)

# print(book3["Number of Pages"])

if __name__ == "__main__": # Tests to see if the files being runned directly. Else: It's not being runned directly.
  print("This is being runned on the dunders file.")
else:
  print("This is not being runned on the dunders file.")