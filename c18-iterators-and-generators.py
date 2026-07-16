#Ejemplo de iterador

#Crear una lista
my_list = [1, 2, 3, 4]

#Obtener el iterador
my_iter = iter(my_list)

#Using the next() function to iterate through the elements
print(f"Valor: {next(my_iter)}")  # Output: 1
print(f"Valor: {next(my_iter)}")  # Output: 2
print(f"Valor: {next(my_iter)}")  # Output: 3
print(f"Valor: {next(my_iter)}")  # Output: 4
print(f"Valor: {next(my_iter)}")  # Raises StopIteration

