a = [1,2,3,4,5]
b = a 
print("Lista a:", a)
print("Lista b:", b)

del a [0]
print("Lista a después de eliminar el primer elemento:", a)
print("Lista b después de eliminar el primer elemento de a:", b)

# Esto demuestra que al modificar la lista a, la lista b también se ve afectada porque ambas referencias apuntan a la misma lista.
print("ID de la lista a:", id(a))
print("ID de la lista b:", id(b))

# Si queremos que b sea una copia independiente de a, podemos usar slicing
c = a[:] 
print("Lista c (copia independiente de a):", c)
print("ID de la lista c:", id(c))

# Modificamos a para demostrar que c no se ve afectada
del a[0]
print("Lista a después de eliminar el primer elemento:", a)
print("Lista c después de eliminar el primer elemento de a:", c)

print("ID de la lista a:", id(a))
print("ID de la lista c:", id(c))