matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print("Matriz:", matrix)
numbers = (1,2,3,4,5)
print("Tupla de números:", numbers)
print(type(numbers))

print(numbers[0])
numbers[0] = 10
print("Tupla de números después de intentar modificar el primer elemento:", numbers)

# Esto demostrará que las tuplas son inmutables, ya que intentar modificar un elemento genera un error.
# Al ejecutar este código, se generará un TypeError indicando que las tuplas no permiten la asignación de elementos. 