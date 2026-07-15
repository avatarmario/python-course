numbers = {1:"uno", 2: "dos", 3: "tres"}
print("Diccionario de números:", numbers)
print("Valor asociado a la clave 2:", numbers[2])
print("Valor asociado a la clave 3:", numbers[3])

information = {"nombre": "Mario",
               "apellido": "García",
               "altura": 1.75,
               "edad": 30}
print("Información personal:", information)

del information["edad"]
print("Información personal después de eliminar la edad:", information)

claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
print(type(values))

pairs = information.items()
print("pairs:", pairs)
print("type(pairs):", type(pairs))

contacts = {"Mario": { "Apellido": "García", "Altura": 1.75, "Edad": 30},
            "Ana": { "Apellido": "Pérez", "Altura": 1.65, "Edad": 28}
            }
print("Contacts:", contacts)
print("Información de Mario:", contacts["Mario"])
print("Información de Ana:", contacts["Ana"])

print("Apellido de Mario:", contacts["Mario"]["Apellido"])
print("Altura de Ana:", contacts["Ana"]["Altura"])