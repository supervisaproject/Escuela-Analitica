#Ejemplo 13
#operadores de identidad
#is.
#si dos variables son dienticas devuelve True si no devuelve False
#identity operators
#is.
#if two variables are scientific it returns True if it does not return False
x = "hola"
y = "hola"

resultado = x is y
print(resultado)

#diferencia entre is y ==
#difference between is and ==
x = 2
y = 2.0

resultado = x==y
print(resultado)

resultado = x is y
print(resultado)

#operador de membresia
#in 
#Comprueba si un valor se encuentra en un listado
#membership operator
#in
#Check if a value is in a list
pets=['dog','cat','ferret']
resultado = 'fox' in pets
print(resultado)

#operadores logicos
#si las condiciones de ambos lados son True, entonces la expresión completa es True
#logical operators
#if the conditions on both sides are True, then the entire expression is True
x = 6
y = 2
resultado = (x>7)and(y>-1)
print(resultado) 

#Si las condiciones de uno de los dos lados es True, entonces la expresión completa es True
#If the conditions of one of the two sides is True, then the entire expression is True

x = 6
y = 2
resultado = (x>7)or(y>-1)
print(resultado) 


#not combierte True a False y viceversa
#not change True to False and vice versa
resultado=not(True)
print(resultado)
