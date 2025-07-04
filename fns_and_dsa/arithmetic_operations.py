def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract',
                         'multiply', 'divide').

    Returns:
        The result of the operation. If division by zero, returns a
        specific string message.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    else:
        # It's good practice to handle unknown operations.
        return "Invalid operation specified."
