import random

choices = ["rock", "paper", "scissors"]

def rockPaperScissors():
  
  userChoice = input("Rock, paper, or scissors? ").lower()
  computerChoice = random.choice(choices)

  print(f"Player - {userChoice}")
  print(f"Computer - {computerChoice}")

  if userChoice == "rock" and computerChoice == "paper":
    print("Computer Wins! ")
  elif userChoice == "paper" and computerChoice == "scissors":
    print("Computer Wins! ")
  elif userChoice == "scissors" and computerChoice == "rock":
    print("Computer Wins! ")
  elif userChoice == "rock" and computerChoice == "scissors":
    print("Player Wins")
  elif userChoice == "paper" and computerChoice == "rock":
    print("Player Wins")
  elif userChoice == "scissors" and computerChoice == "paper":
      print("Player Wins")
  elif userChoice == computerChoice:
    print(" TIE! ")
  else:
    print("Error. Enter one of the right choices.")
  

rockPaperScissors()