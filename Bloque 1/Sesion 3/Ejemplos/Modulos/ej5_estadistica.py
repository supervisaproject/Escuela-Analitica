#Ejemplo 5
import statistics

importes = [10,201,345,123,345.56,32.3,19.3,235,98,78]

media = statistics.mean(importes)
mediana = statistics.median(importes)
desviacion_estandar = statistics.stdev(importes)

print("Media: "+ str(media)  +" Mediana: " + str(mediana) + " Desviacion estandar: " + str(desviacion_estandar))