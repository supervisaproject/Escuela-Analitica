
#Ejemplo 8 acceder elementos de una lista
#print the second item in a list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#imprimir el ultimo elemento de una lista
#print the last item in a list
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#imprimir el tercero, cuarto y quinto elemento de una lista
#print the third, fourth and fifth elements of a list
thislist = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(thislist[2:5])

#Accediendo un indice que no exista generara un error.
#Accessing an index that does not exist will generate an error.
mylist = [1,2,3]
print (mylist[10])