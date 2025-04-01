class BankAccount:
  def __init__(self, balance):
    self.__balance = balance

  def deposit(self, amount):
    self.__balance += amount
    print(f"Deposited {amount}. New balance {self.__balance}")

  def withdraw(self, amount):
    if amount > self.__balance:
      print("Not enough money!")

    else:
      self.__balance -= amount
      print(f"Withdrew {amount}. New balance: {self.__balance}")

my_account = BankAccount(100)
my_account.deposit(50)
my_account.withdraw(30)