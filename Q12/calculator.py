# calculator.py

def add(a, b):
    """
    Function to add two numbers.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Function to subtract one number from another.
    
    Parameters:
    a (float): The number to be subtracted from.
    b (float): The number to subtract.
    
    Returns:
    float: The difference of the two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Function to multiply two numbers.
    
    Parameters:
    a (float): The first number.
    b (float): The second number.
    
    Returns:
    float: The product of the two numbers.
    """
    return a * b

def divide(a, b):
    """
    Function to divide one number by another.
    
    Parameters:
    a (float): The dividend.
    b (float): The divisor.
    
    Returns:
    float: The quotient of the division.
    
    Raises:
    ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
