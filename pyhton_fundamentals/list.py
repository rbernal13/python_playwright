a = [10, 1, 2, 3, 4, 3.56, "Hello"]

search_result = a.index(10)  ##Devuelve el indice del elemento indicado
print(search_result)
print(a[5])

a.reverse()  ##Invierte la lista
print(a)

a.append(99)
a.append(2)
print(a)

ocurrencias = a.count(2) ##Numero de ocurrencias del numero '2'
print(ocurrencias)

a.pop()
a.pop()
print(a) ## Elimina el elemento en el indice definido (por defecto, el ultimo)

a += ["World", 50, 51]
print(a)

a += "Python", 80, 81
print(a)

if 80 in a:
    print("80 esta en la lista")




