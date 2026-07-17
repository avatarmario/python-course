add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Error: Division by zero"

print(f"Result addition: {add(2, 3)}")
print(f"Result subtraction: {subtract(5, 2)}")
print(f"Result multiplication: {multiply(3, 4)}")
print(f"Result division: {divide(10, 2)}")
print(f"Result division: {divide(10, 0)}")

#map() and list()
numbers = range(11)
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")    

#filter() and list()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
