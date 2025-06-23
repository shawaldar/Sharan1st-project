def custom_sum(a, b):
    """
    Returns the sum of two integers.
    If the sum is between 15 and 20 (inclusive), returns 20 instead.
    """
    total = a + b
    if 15 <= total <= 20:
        return 20
    return total


# Get input from the user
try:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    result = custom_sum(num1, num2)
    print("Result:", result)

except ValueError:
    print("Please enter valid integers.")
