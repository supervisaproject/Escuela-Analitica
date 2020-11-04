# - *- coding: utf- 8 - *-
#cambia los textos para que se muestre el mensaje de acceder al contenido solo si es mayor de edad o es un menor que esta con sus padres


edad = int(raw_input("¿Cuántos años tiene? "))
if edad < 18:
    padres = raw_input("¿Estan tus padres contigo(S/N)? ")
    if padres == "S":
      raw_input("No puedes acceder al contenido")
    else:
      raw_input("Puedes acceder al contenido")  
else:
    raw_input("No puedes acceder al contenido")