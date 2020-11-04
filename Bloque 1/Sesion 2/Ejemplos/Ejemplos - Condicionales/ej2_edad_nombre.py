# - *- coding: utf- 8 - *-
    
#Ejemplo 2
#Comprobacion acceso por edad al contenido B
edad = int(raw_input("Escriba su edad: "))
nombre = raw_input("Escriba su nombre: ")
if nombre == "Juan" and edad >= 18:
    print ("Ha accedido correctamente al contenido 'A'")

#Comprobacion acceso por edad al contenido C

if nombre == "John" or nombre == "Ana":
    print ("Ha accedido correctamente al contenido 'B'")

 