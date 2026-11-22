from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    # Removes white space from operation
    Oper = operation.strip()

    # Ensures a and b vars are floats to reduce errors within calc
    a = float(a_text.strip())
    b = float(b_text.strip())

    # Checks list of operaters and validates them
    if Oper not in ("add", "subtract", "multiply", "divide"):
        return ("ERROR", "", "UNKNOWN_OPERATION")

    # Same logic but for the numbers
    if a_text.strip() == "" or b_text.strip() == "":
        return("ERROR", "", "INVALID_NUMBER")

    #Similar logic but checks for division by zero
    if Oper == "divide" and b == 0:
        return ("ERROR", "", "DIVISION_BY_ZERO")

    # Logic for the calculator such as adding and return
    if Oper == "add":
        return ("OK", add(a, b), "")

    if Oper == "subtract":
        return ("OK", subtract(a, b), "")

    if Oper == "multiply":
        return ("OK", multiply(a, b), "")

    if Oper == "divide":
        return ("OK", divide(a, b), "")
    
    
    
