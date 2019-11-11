
#Ejemplo 9 asignar, anadir y eliminar valores
#cambiar el valor del segundo elemento de una lista
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#append nos permite anadir valores consecutivos a nuestra lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#mediante insert podemos anadir un elemento una lista en una posicion concreta
thislist.insert(2, 'grapes')
print(thislist)

#eliminar un elemento de la lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#eliminar un elemento de la lista mediante el indice
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)