
#Ejemplo 4
#You can have if statements inside if statements, this is called nested if statements.
x = int(input("Cuantos años tienes: "))
if x > 10:
  print("Más de 10")
  if x > 20:
    print("Más de 20")
  else:
    print("Entre 10 y 20")
