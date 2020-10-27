#ejercicio 1

#anade a la lista "frutas" las palabras "orange", "apple" y "banana" en este orden y elimina el elmento "audi"

frutas = ["lemon","audi"]



'''
NO TOCAR !!!!!
'''
#Codigo de comprobacion
a = 20
if (frutas[0] == "lemon")and(frutas[1]=="orange")and(frutas[2]=="apple")and(frutas[3]=="banana"):
  a = 4
elif(frutas[0] == "lemon")and(frutas[1]=="orange")and(frutas[2]=="apple")and(frutas[3]=="banana"):
  a = 3
elif(frutas[0] == "lemon")and(frutas[1]=="orange")and(frutas[2]=="apple")and(frutas[3]=="banana"):
  a = 2
elif(frutas[0] == "lemon")and(frutas[1]=="orange")and(frutas[0]=="apple")and(frutas[3]=="banana"):
  a = 1

print("El resultado final para el formulario es: " + str(a))
