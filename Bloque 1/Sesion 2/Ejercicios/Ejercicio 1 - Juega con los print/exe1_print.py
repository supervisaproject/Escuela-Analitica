#cambia los textos para que se muestre el mensaje de acceder al contenido solo si es mayor de edad o es un menor que esta con sus padres


edad = int(input("¿Cuántos años tiene? "))
if edad < 18:
    padres = input("¿Estan tus padres contigo(S/N)? ")
    if padres == "S":
      print("No puedes acceder al contenido")
    else:
      print("Puedes acceder al contenido")  
else:
    print("No puedes acceder al contenido")