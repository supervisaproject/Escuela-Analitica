# Siendo a y b parametros de entrada
# crea las funciones de suma, resta, divide, multiplica y raiz en un modulo aparte llamado calculadora
# Si creas correctamente este módulo y sus funciones el ejercicio imprime un valor numérico de resultado

# Where a and b are input parameters
# create the addition, subtraction, divide, multiply and root functions in a separate module called calculadora
# If you correctly create this module and its functions, the exercise prints a numerical result value


import calculadora 
 
 
a = 8
b = 2
 
##### 
############ VERIFICADOR DEL EJERCICIO ############################
############ EXERCISE VERIFIER ############################

resultado = math.lgamma(calculadora.suma(a, b) + calculadora.resta(a, b) + calculadora.multiplica(a, b) + calculadora.divide(a, b) + calculadora.raiz(a))
 
##### INTRODUCIR EN EL FORMULARIO DEL EXAMEN EL VALOR QUE APARECE AL EJECUTAR 
##### SOLO CON 3 DIGITOS DECIMALES!!!!!
##### ENTER IN THE EXAM FORM THE VALUE THAT APPEARS WHEN EXECUTING
##### ONLY WITH 3 DECIMAL DIGITS !!!!!
#####
##### Ejemplo:
##### Example:
##### RESULTADO -> 222.21535184  VALOR A INTRODUCIR EN EL FORMULARIO DEL EXAMEN -> 222.215
##### RESULT -> 222.21535184 VALUE TO ENTER IN THE EXAM FORM -> 222.215
#####
print(resultado)

### NO TOCAR FIN