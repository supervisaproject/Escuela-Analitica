#ejemplo 3

def media(listado_valores):
  importe_total = 0
  for importe in listado_valores:
    importe_total = importe + importe_total

  media = importe_total/len(listado_valores)
  return media


importes = [10, 20, 50, 35]
resultado = media(importes)
print("La media de nuestros importes es: " + str(resultado))