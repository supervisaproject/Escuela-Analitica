
#Ejemplo 10
#limpiar una lista
#clean a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#el metodo index() busca el indice de un elemento en la lista
#the index () method looks for the index of an element in the list
my_list = ['a','b','c']
index = my_list.index('b')
print(index)

#imprimir el tamanio de una lista
#print the size of a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#contar cuanto se repite un determinado elemento de una lista
#count how much a certain element of a list repeats
fruits = ['cherry', 'apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

#ordenar una lista
#ordenar creciente
# sort a list
# ascending order

x = [4, 6, 3, -5]
x.sort()
print(x)

#ordenar decreciente
# decreasing order
x = [4, 6, 3, -5] 
x.sort(reverse = True)
print(x)