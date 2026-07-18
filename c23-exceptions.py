try:
    divisor = int(input("Enter a divisor: "))
    result = 10 / divisor
    print("Result:", result)
except ZeroDivisionError as e:
    print("Divisor cannot be zero. Cannot divide by zero")
    print("Ha ocurrido un error: ", e)
except ValueError as e:
    print("Invalid input. Please enter an integer.")
    print("Ha ocurrido un error: ", e)
