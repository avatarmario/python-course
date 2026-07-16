def odds(limit):
    for n in range(1, limit + 1, 2):
        yield n

def evens(limit):
    for n in range(2, limit + 1, 2):
        yield n

print("Odd numbers:")
for odd in odds(10):
    print(odd) 

print("Even numbers:")
for even in evens(10):
    print(even) 