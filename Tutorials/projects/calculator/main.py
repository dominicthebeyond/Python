while True:
  try:
    op = input('What operation would you like to perform in the calculation? (add (a), subtract (s), multiply (m), divide (d), remainder (r)) ')
    x = float(input("Num 1: "))
    z = float(input("Num 2: "))
    break
  except ValueError:
    print("Enter the right num and operation you want to perform.")

def calculator(x, z, op):


  match op: 

    case "a":
      return x + z
    case "s":
      return x - z
    case "m":
      return x * z
    case "d":
      return x / z
    case "r":
      return x % z
    
result = calculator(x, z, op)
print(f'Result: {result}')