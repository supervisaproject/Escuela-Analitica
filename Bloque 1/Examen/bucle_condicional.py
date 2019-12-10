# Crea un bucle que recorra todos los elementos de la sieguiente lista de importes, en cada iteración se debe ejecutar el cuerpo 1 o el cuerpo 2. 
# El "cuerpo 1" se ejecutara si el importe del elemento que estamos iterando, es mayor que la raiz cuadrada de la variable "importe_referencia" en caso contrario se ejecutara el "cuerpo 2". 

### NO TOCAR INICIO
resultado= 0
lista_importes = [10, 25, 13, 15, 17, 17, 11]
importe_referencia = 144

### NO TOCAR File


#Escribe tu código a partir de aqui:

  #Cuerpo 1
  resultado_aux = abs(math.sin(importe_referencia))
  resultado = resultado + resultado_aux 

  #Cuerpo 2
  resultado_aux = abs(math.cos(importe_referencia))
  resultado = resultado + resultado_aux 


##### INTRODUCIR EN EL FORMULARIO DEL EXAMEN EL VALOR QUE APARECE AL EJECUTAR 
##### SOLO CON 3 DIGITOS DECIMALES!!!!!
#####
##### Ejemplo:
#####
##### RESULTADO -> 2.21535184  VALOR A INTRODUCIR EN EL FORMULARIO DEL EXAMEN -> 2.215
#####
#####

#Imprime la variable resultado, para rellenar en forms
print(resultado)