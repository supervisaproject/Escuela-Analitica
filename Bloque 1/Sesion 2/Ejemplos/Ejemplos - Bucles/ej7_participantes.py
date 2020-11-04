# - *- coding: utf- 8 - *-
#Ejemplo 7
 
print("Número de participantes de los cuatro primeros trimestres")
a = 1
for numero in [32, 35, 14, 16]:
 print("En el "+ str(a) + "º trimestre tenemos "+ str(numero) + " participantes")
 a += 1
 
 
print("¿En que paises tenemos oficinas?")
for pais in ["Chile", "Ecuador", "Peru", "Argentina", "España", "Brasil"]:
 print("Tenemos oficina en: "+ str(pais))
 
print("¿En que paises tenemos oficinas?")
paises = ["Chile", "Ecuador", "Peru", "Argentina", "España", "Brasil"]
for i in range(len(paises)):
 print("Tenemos oficina en: "+ str(paises[i]))