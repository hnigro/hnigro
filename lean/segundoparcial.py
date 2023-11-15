vectormodelo = []
vectorprecio = []
def cargar(vectormodelo ,vectorprecio):
    modelo = (input("Ingrese el nombre del modelo: ")).upper()
    while modelo != "FIN":
        vectormodelo.append(modelo)
        precio = int(input("Ingrese el precio: "))
        while precio <= 0:
            print("El precio no puede ser ni menor ni igual a 0")
            precio = int(input("Ingrese el precio: "))
        vectorprecio.append(precio)
        modelo = (input("Ingrese el nombre del modelo: ")).upper()
def mostrar(vectormodelo,vectorprecio):
    print("MODELO \t\t PRECIO")
    for i in range(len(vectormodelo)):
        print((vectormodelo[i]) ,"\t\t", (vectorprecio[i]))
def preciobajo(vectorprecio):
    min = vectorprecio[0]
    pos = 0
    for i in range (len(vectorprecio)):
        if vectorprecio[i] < min:
            min = vectorprecio[i]
            pos = vectorprecio[i]
    return pos
def calcpromedio(vectorprecio):
    suma = 0
    pos = 0
    for i in range(len(vectorprecio)):
        if vectorprecio[i] > 10000:
            suma = suma + vectorprecio[i]
            pos = pos + 1
        promedio = suma / pos
    return promedio
def eliminar(vectorprecio):
    i = 0
    while i < len(vectorprecio):
        if vectorprecio[i] > calcpromedio(vectorprecio):
            vectorprecio.pop(i)
            vectormodelo.pop(i)
        i = i + 1
    return vectorprecio
def ordenar(vectorprecio,vectormodelo):
    i = 0
    while i < len(0,vectorprecio)-1:
        if vectorprecio[i] < vectorprecio [i + 1]:
            aux = vectorprecio[i]
            vectorprecio[i] = vectorprecio[i + 1]
            vectorprecio[i + 1] = aux
            aux2 = vectormodelo[i]
            vectormodelo[1] = vectormodelo[i + 1]
            vectormodelo[i + 1] = aux2
    i = i + 1
    return

cargar(vectormodelo,vectorprecio)

mostrar(vectormodelo,vectorprecio)

print("El modelo de menor precio es:" ,preciobajo(vectorprecio))

print("El promedio de los precios mayores 10.000 es: ",calcpromedio(vectorprecio))

print(eliminar(vectorprecio))

print("Despues de eliminar numeros")

mostrar(vectormodelo,vectorprecio)

ordenar(vectorprecio,vectormodelo)