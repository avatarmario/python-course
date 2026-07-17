squares = [x**2 for x in range(1,11)]

celsius = [0 , 10, 20, 30, 40]
fahrenheit = [temp * 9/5 + 32 for temp in celsius]
print("Temperature inFahrenheit:", fahrenheit)

#Numeros pares
evens = [x for x in range(1,20) if x %2 == 0]
print("Even numbers:", evens)

#transpose
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed matrix:", transpose)
