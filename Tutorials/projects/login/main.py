userNameInput = input("Username: ")
passwordInput = input("Password: ")

def loginScreen(username, password):
  
  username = "yourmom"
  password = "123"

  if username == userNameInput and password == passwordInput:
    print("Login Successful")
    print("Heading to the next page right away.")

  else: 
    print('Login Unsuccessful')

loginScreen(userNameInput, passwordInput)