#Ejemplo 11
#operadores aritmeticos
#suma, multiplicacion y division pueden usarse con numeros
#arithmetic operators
#sum, multiplication and division can be used with numbers
number = 3 + 2 * 3 / 4.0
print(number)

#se pueden anadir parentesis para que unas operaciones se realicen antes que otras
# parentheses can be added so that some operations are performed before others
number = (3 + 2) * 3 / 4.0
print(number)


#operador modulo devuelve la parte entera de una division
#Module operator returns the integer part of a division
remainder = 11 % 3
print(remainder)

#el uso de la doble multiplicacion nos permite calcular potentcias
# the use of double multiplication allows us to calculate potentials
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

#Operar con cadenas
#Podemos usar el caracter + para anadir una cadena a otra:
#Operate with chains
# We can use the + character to add one string to another:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

#Tambien podemos usarlo para juntar variables y cadenas:
# We can also use it to join variables and strings:
x = "awesome"
print("Python is " + x)

#Mezclando operadores entre los numeros y cadenas que no son soportadas:
# Esto no funcionará!
#Mixing operators between numbers and strings that are not supported:
# This will not work!
x=1
y=3
print (x + y + "hola")

#juntar listas
#append lists
list1 = [4,5,7]
list2 = [45, 9]
list_total = list1 + list2
print(list_total)

#anadir y asignar
#add and assign
a=2
a+=2
print(a)

#lo mismo que esto
# same as this
a=2
a=a+2
print(a)