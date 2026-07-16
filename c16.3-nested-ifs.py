is_member = True
age = 14

if is_member:
    if age >= 15:
        print("You have access since you are a member and your age is 15 or older.")
    else:
        print("No access since you are a member but your age is less than 15.")
else:
    print("No eres miembro, por lo que no tienes acceso.")