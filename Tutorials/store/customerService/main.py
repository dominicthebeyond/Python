class CustomerService:
  def __init__(self, nameOfRepresentitive):
    self.nameOfRep = nameOfRepresentitive
    self.user_query = None

  def get_user_query(self):
    self.userQuery = input("What do you need help with? (a product, bad experience, service, or other)")

  def response_to_query(self): # Self = instance || cls = class
    
    print(f"Hello my names {self.nameOfRep}")

    if self.userQuery == "a product":
      print("Fowarding to product team!")
    elif self.userQuery == "bad experience":
      print("Im sorry to hear that. Would you be open to telling us more details?")
    elif self.userQuery == "service":
      print("What kind of service? ")
    elif self.userQuery == "other":
      print("Tell us more.... ")
    else:
      print("Im sorry we don't understand")


Abby = CustomerService("Abby")

Abby.responseToQuery()