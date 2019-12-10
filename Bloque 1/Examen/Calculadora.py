# Siendo a y b parametros de entrada
# crea las funciones de suma, resta, divide, multiplica y raiz en un modulo aparte llamado calculadora
# Si creas correctamente este módulo y sus funciones el ejercicio imprime un valor numérico de resultado


### NO TOCAR INICIO

import calculadora 
 
 
a = 8
b = 2
 
##### 
############ VERIFICADOR DEL EJERCICIO ############################

resultado = math.lgamma(calculadora.suma(a, b) + calculadora.resta(a, b) + calculadora.multiplica(a, b) + calculadora.divide(a, b) + calculadora.raiz(a))
 
##### INTRODUCIR EN EL FORMULARIO DEL EXAMEN EL VALOR QUE APARECE AL EJECUTAR 
##### SOLO CON 3 DIGITOS DECIMALES!!!!!
#####
##### Ejemplo:
#####
##### RESULTADO -> 222.21535184  VALOR A INTRODUCIR EN EL FORMULARIO DEL EXAMEN -> 222.215
#####
#####
print(resultado)

### NO TOCAR FIN