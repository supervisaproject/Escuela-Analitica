#este codigo no esta funcionando bien
#corrige los "print" para que sean los correctos 


print("Piense un número de 1 a 4.")
print("Conteste S (sí) o N (no) a mis preguntas.")
primera = input("¿El número pensado es mayor que 2? ")
if primera == "S":
    segunda = input("¿El número pensado es mayor que 3? ")
    if segunda == "S":
        #print 1
        print("El número pensado es 1.")
    else:
        #print 2
        print("El número pensado es 2")
else:
    segunda = input("¿El número pensado es mayor que 1? ")
    if segunda != "S":
        #print 3
        print("El número pensado es 4.")
    else:
        #print 4
        print("El número pensado es 3.")
print("¡Hasta la próxima!")