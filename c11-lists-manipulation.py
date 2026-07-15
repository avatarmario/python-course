to_do = ["Dirigirnos al hotel",
         "Ir almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)

numbers = [1, 2, 3, 4, "cinco"]
print(numbers)

print(type(numbers))

print(numbers[0])
print(numbers[4])

print(type(numbers[0]))
print(type(numbers[4]))

mix = [1, "dos", 3.0, True]
print(mix)
print(len(mix))

string = "Hola mundo"

print("los dos primeros elementos de la lista mix:",mix[0:2])
print("los cuatro primeros caracteres de la cadena string:",string[0:4])

print("desde el inicio hasta el cuarto caracter:",string[:4])
print("desde el quinto caracter hasta el final:", string[5:])
print("toda la cadena:", string[:])
print("cada dos caracteres empezando desde el primero:", string[::2])
print("cada dos caracteres empezando desde el segundo:", string[1::2])
print("cadena invertida:", string[::-1])

mix.append("nuevo elemento")
print("lista mix después de agregar un nuevo elemento:", mix)

mix.remove("nuevo elemento")
print("lista mix después de eliminar el nuevo elemento:", mix)

mix.append([1, 2, 3])
print("lista mix después de agregar una lista :", mix)

mix.insert(1, "elemento insertado")
print("lista mix después de insertar un elemento en la posición 1:", mix)

numbers = [1,2,100, 90.45, 3, 4, 5]
print("Lista de números:", numbers)
print("Mayor", max(numbers))
print("Menor", min(numbers))

del numbers[-1]
print("Lista de números después de eliminar el último elemento:", numbers)

numbers.pop(0)
print("Lista de números después de eliminar el primer elemento:", numbers)

numbers.remove(100)
print("Lista de números después de eliminar el elemento 100:", numbers)

del numbers[:2]
print("Lista de números después de eliminar los dos primeros elementos:", numbers)

del numbers
print("Lista de números después de eliminar la lista completa:", numbers)