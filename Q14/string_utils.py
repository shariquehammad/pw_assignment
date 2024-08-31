def reverse_string(input_string):
    """
    Reverses the input string.
    Args:
        input_string (str): The string to reverse.
    Returns:
        str: The reversed string.
    """
    return input_string[::-1]

def capitalize_string(input_string):
    """
    Capitalizes the first letter of each word in the input string.
    Args:
        input_string (str): The string to capitalize.
    Returns:
        str: The capitalized string.
    """
    return ' '.join(word.capitalize() for word in input_string.split())