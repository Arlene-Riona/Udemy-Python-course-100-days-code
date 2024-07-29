#calculator 

def add(n1, n2):
  '''Adds num1 and num2 and returns the value.'''
  return n1+n2

def subtract(n1, n2):
  '''Subtracts num1 and num2 and returns the value.'''
  return n1-n2

def multiply(n1, n2):
  '''Multiplies num1 and num2 and returns the value.'''
  return n1*n2

def divide(n1, n2):
  '''Divides num1 and num2 and returns the value.'''
  return n1/n2

def exponent(x, y):
  '''Calculates x^y and returns the value.'''

  if y == 1:
      return x
  else:
      y -= 1
      return x * exponent(x, y)
    
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "^":exponent
}


result = 0.0
process = "n"
choice = " "

while process != "exit":
  if process.lower() == "n":
    n1 = float(input("Enter number1: "))
    n2 = float(input("Enter number2: "))
  elif process.lower() == "c":
    n1 = result
    n2 = float(input("Enter number2: "))


  print("The possible operations are:")
  for symbols in operations:
    print(symbols)
  operation_user = input(f"Enter the operation for {n1} and {n2} ")
  calc_function = operations[operation_user]
  result = calc_function(n1, n2)
  print(f"{n1} {operation_user} {n2} = {result}")
  process = input("Do you wish to c/n/exit? ").strip().lower()
print("Thank you :)")
