def add(a, b):
    result = a + b
    print(f"Addition of {a} and {b} is {result}")

def sub(a, b):
    result = a - b
    print(f"Subtraction of {a} and {b} is {result}")

def mult(a, b):
    result = a * b
    print(f"Multiplication of {a} and {b} is {result}")

def div(a, b):
    if b == 0:
        print("Division by zero is not allowed.")
    else:
        result = a / b
        print(f"Division of {a} by {b} is {result}")