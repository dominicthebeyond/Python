def semGrades():

  for i in range(3):

    gradeInput = input("What was your grade this semester?: ").upper()

    if gradeInput == "A":
      print("You got an A! ")
      break
    elif gradeInput == "B":
      print("You got a B! ")
      break
    elif gradeInput == "C":
      print("You got a C! ")
      print("We can do better.. ")
      break
    elif gradeInput == "D":
      print("You got a D! ")
      print("We really need to do better! ")
      break
    elif gradeInput == "F":
      print("You got a F!!!!!! ")
      print("We definetly need to do better!! ")
      break
    else:
      print("Enter a letter. ")

semGrades()