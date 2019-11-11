#Ejemplo 13
#operadores de identidad
#is.
#si dos variables son dienticas devuelve True si no devuelve False
x = "hola"
y = "hola"

resultado = x is y
print(resultado)

#diferencia entre is y ==
x = 2
y = 2.0

resultado = x==y
print(resultado)

resultado = x is y
print(resultado)

#operador de membresia
#in 
#Comprueba si un valor se encuentra en un listado
pets=['dog','cat','ferret']
resultado = 'fox' in pets
print(resultado)

#operadores logicos
#si las condiciones de ambos lados son True, entonces la expresión completa es True
x = 6
y = 2
resultado = (x>7)and(y>-1)
print(resultado) 

#Si las condiciones de uno de los dos lados es True, entonces la expresión completa es True

x = 6
y = 2
resultado = (x>7)or(y>-1)
print(resultado) 


#not combierte True a False y viceversa
resultado=not(True)
print(resultado)
