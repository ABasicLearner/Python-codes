from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()


"""
def add(n1, n2):
    return n1 + n1

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    '+': add, 
    '-': subtract, 
    '*': multiply, 
    '/': divide
    }

num1 = int(input("Enter first number: "))
for operator in operation:
    print(operator)

operation_symbol = input("Pick an operation from the line above:  ")
num2 = int(input("Enter second number: "))
calculation_function = operation[operation_symbol]
first_answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")


operation_symbol = input("Pick an operation: ") 
num3 = int(input("What's the next number?: "))
calculation_function = operation[operation_symbol] 
second_answer = calculation_function(calculation_function(num1, num2), num3)
second_answer = calculation_function(first_answer, num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
"""