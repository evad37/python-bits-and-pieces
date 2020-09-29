"""
Calculator.py

A calculator that takes input as a string from the user, and recursively solves
the given problem. Reports "divide by zero" errors and bracket mismatch errors.
"""

def add(a,b):
    if a is None or b is None:
        return None
    return a + b
def minus(a,b):
    if a is None or b is None:
        return None
    return a - b
def times(a,b):
    if a is None or b is None:
        return None
    return a * b
def divide(a,b):
    if b == 0:
        print("Divide by zero error!")
        return None
    elif a is None or b is None:
        return None
    return a / b
def power(a,b):
    if a is None or b is None:
        return None
    return pow(a, b)

def calculator(problem):
    if problem.count("(") != problem.count(")"):
        print("Bracket count mismatch error!")
        return None
    elif "(" in problem:
        lastOpenBracket = problem.rindex("(")
        nextCloseBracket = problem.find(")", lastOpenBracket)
        if nextCloseBracket == -1:
            print("Bracket order mismatch error!")
            return None
        innerTotal = calculator(problem[lastOpenBracket+1:nextCloseBracket])
        if innerTotal is None:
            return None
        # Convert to string as a float (not exponential for small numbers)
        innerPart = format(innerTotal, 'f')
        leftPart = problem[0:lastOpenBracket]
        if len(leftPart) > 0 and not leftPart[-1] in "+-*/^(":
            leftPart += "*"
        rightPart = problem[nextCloseBracket+1:]
        if len(rightPart) > 0 and  not rightPart[0] in "+-*/^)":
            rightPart = "*" + rightPart
        return calculator(leftPart+innerPart+rightPart)
    elif "+" in problem:
        parts = problem.split("+")
        subtotal = calculator(parts[0])
        for i in range(1, len(parts)):
            subtotal = add(subtotal, calculator(parts[i]))
        return subtotal
    elif "-" in problem:
        parts = problem.split("-")
        subtotal = calculator(parts[0])
        for i in range(1, len(parts)):
            subtotal = minus(subtotal, calculator(parts[i]))
        return subtotal
    elif "*" in problem:
        parts = problem.split("*")
        subtotal = calculator(parts[0])
        for i in range(1, len(parts)):
            subtotal = times(subtotal, calculator(parts[i]))
        return subtotal
    elif "/" in problem:
        parts = problem.split("/")
        subtotal = calculator(parts[0])
        for i in range(1, len(parts)):
            subtotal = divide(subtotal, calculator(parts[i]))
        return subtotal
    elif "^" in problem:
        parts = problem.split("^")
        subtotal = calculator(parts[0])
        for i in range(1, len(parts)):
            subtotal = power(subtotal, calculator(parts[i]))
        return subtotal
    elif problem == "":
        print("Error! Operators must be used between numbers.")
    else:
        return float(problem)

result = None
print("Enter problem(s), or 'Q' to quit. Use numbers and the symbols + - * / ^ ( ) only.")
while True:
    calculation = input("> ")
    if calculation.upper() == 'Q':
        break
    if not(result is None) and calculation[0] in "+-*/^":
        calculation = format(result, 'f') + calculation
    result = calculator(calculation)
    if not(result is None):
        print("=", result)
