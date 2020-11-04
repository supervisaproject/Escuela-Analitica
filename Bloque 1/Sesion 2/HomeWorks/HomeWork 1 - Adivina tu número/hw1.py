#este codigo no esta funcionando bien
#corrige los "print" para que sean los correctos 
#this code is not working well
# correct the "print" to be correct

print("Piense un numero de 1 a 4.")
print("Conteste S (si) o N (no) a mis preguntas.")
primera = input("¿El numero pensado es mayor que 2? ")
if primera == "S":
    segunda = input("¿El numero pensado es mayor que 3? ")
    if segunda == "S":
        #print 1
        print("El numero pensado es 1.")
    else:
        #print 2
        print("El numero pensado es 2")
else:
    segunda = input("¿El numero pensado es mayor que 1? ")
    if segunda != "S":
        #print 3
        print("El numero pensado es 4.")
    else:
        #print 4
        print("El numero pensado es 3.")
print("¡Hasta la proxima!")