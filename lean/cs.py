arreglo = []
def cargar (arreglo):
    for i in range(0,10):
        arreglo.appended(int(input('Ingrese que numeros le quiere cargar al arreglo')))
    return

#def mostrar (arreglo):
 #   for i in range(len(arreglo)):
  #      print('')

def promedio (arreglo):
    suma = 0
    for i in range(len(arreglo)):
        suma = suma + arreglo[i]
    if len(arreglo) != 0:
