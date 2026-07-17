def greet(name, last_name = "No tiene apellido"):
    if last_name == "No tiene apellido":
        print("No last name provided.")
    else:
        print("Hello,", name, last_name)

greet("Mario")
greet("Mario", "Ramos")

greet(last_name = "Ramos", name = "Mario")