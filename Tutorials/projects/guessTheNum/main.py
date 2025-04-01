import random

def guessTheNum():

  randomNum = random.randint(1, 10) 
  for g in range(3):
    try: 
      userInput = int(input("Guess The Num: "))
    except ValueError:
      print("Enter a num bro! ")
      continue

    if userInput > randomNum: 
      print(f"TOO HIGH!! Guesses left: {3 - (g + 1)}")
    elif userInput == randomNum:
      print("YOU GOT THE NUM! LETS GOO! ")
      break
    else: 
      print(f"TOO LOW! Guesses Left: {3 - (g + 1)}")
guessTheNum()


  