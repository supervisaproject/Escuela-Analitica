# Crea un bucle que recorra todos los elementos de la sieguiente lista de importes, en cada iteración se debe ejecutar el cuerpo 1 o el cuerpo 2. 
# El "cuerpo 1" se ejecutara si el importe del elemento que estamos iterando, es menor que la raiz cuadrada de la variable "importe_referencia" en caso contrario se ejecutara el "cuerpo 2". 
# Create a loop that goes through all the elements of the following list of amounts, in each iteration body 1 or body 2 must be executed.
# The "body 1" will be executed if the amount of the element that we are iterating, is less than the square root of the variable "amount_reference", otherwise "body 2" will be executed.

### NO TOCAR DATOS INICIALES 
### DO NOT INICIAL DATA
resultado= 0
lista_importes = [10, 25, 13, 15, 17, 17, 11]
importe_referencia = 144


#Escribe tu código a partir de aqui:

  #Cuerpo 1
  resultado_aux = abs(math.sin(importe_referencia))
  resultado = resultado + resultado_aux 

  #Cuerpo 2
  resultado_aux = abs(math.cos(importe_referencia))
  resultado = resultado + resultado_aux 


##### INTRODUCIR EN EL FORMULARIO DEL EXAMEN EL VALOR QUE APARECE AL EJECUTAR 
##### ENTER IN THE EXAM FORM THE VALUE THAT APPEARS WHEN EXECUTING
##### SOLO CON 3 DIGITOS DECIMALES!!!!!
##### ONLY WITH 3 DECIMAL DIGITS !!!!!
##### Ejemplo/Example:
#####
##### RESULTADO -> 2.21535184  VALOR A INTRODUCIR EN EL FORMULARIO DEL EXAMEN -> 2.215
##### RESULT -> 2.21535184 VALUE TO ENTER IN THE EXAM FORM -> 2.215
#####

#Imprime la variable resultado, para rellenar en forms
#Print the result variable, to fill in forms
print(resultado)