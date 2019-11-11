
#Ejemplo 10
#limpiar una lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#el metodo index() busca el indice de un elemento en la lista
my_list = ['a','b','c']
index = my_list.index('b')
print(index)

#imprimir el tamanio de una lista
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#contar cuanto se repite un determinado elemento de una lista
fruits = ['cherry', 'apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

#ordenar una lista
#ordenar decreciente

x = [4, 6, 3, -5]
x.sort()
print(x)

#ordenar creciente

x = [4, 6, 3, -5]
x.sort(reverse = True)
print(x)