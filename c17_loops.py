numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(f"i = {i}")

for i in range(3, 10):
    print(f"i = {i}")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"fruit = {fruit}")
    if fruit == "banana":
        print("Found a banana!")
        break;

x = 0
while x < 5:
    if x == 3:
        print("Found a 3!")
        break
    print(f"x = {x}")
    x += 1