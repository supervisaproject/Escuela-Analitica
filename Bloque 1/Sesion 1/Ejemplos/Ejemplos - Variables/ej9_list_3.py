
#Ejemplo 9 asignar, anadir y eliminar valores
#cambiar el valor del segundo elemento de una lista
#change the value of the second element of a list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#append nos permite anadir valores consecutivos a nuestra lista
#append allows us to add consecutive values ​​to our list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#mediante insert podemos anadir un elemento una lista en una posicion concreta
#by means of insert we can add an element to a list in a specific position
thislist.insert(2, 'grapes')
print(thislist)

#eliminar un elemento de la lista
#remove an item from the list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#eliminar un elemento de la lista mediante el indice
# remove an item from the list using the index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)