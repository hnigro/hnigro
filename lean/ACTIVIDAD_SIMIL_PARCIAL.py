vectorprodu = []
vectorprecio = []
def cargar (vectorprodu , vectorprecio):
    producto = input("Decime el nombre del producto").upper()
    while producto != 'FIN':
        vectorprodu.append(producto)
        precio = int(input("Decime el valor del producto"))
        while precio < 0:
            precio= int(input("El precio del producto debe ser positivo"))
        vectorprecio.append(precio)
        producto = input("Decime el nombre del producto").upper()

def mostrar (vectorprodu,vectorprecio):
    print("PRODUCTOS \t\t PRECIOS")
    for i in range(0,len(vectorprodu)):
        print(f"{vectorprodu[i]}\t\t      {vectorprecio[i]}")

def mayorprecio (vectorprecio):
    max = 0
    model = 0
    for i in range (0,len(vectorprecio)):
        if vectorprecio[i] > max:
            max = vectorprecio[i]
            model = vectorprodu[i]
    return model

def calcpromedio (vectorprecio):
    suma = 0
    for i in range (0,len(vectorprecio)):
        suma = suma + vectorprecio[i]
    promedio = suma/len(vectorprecio)
    return promedio

def eliminarprodu(vectorprecio):
    i = 0
    while i < len(vectorprecio):
        if vectorprecio[i] > calcpromedio(vectorprecio):
            vectorprecio.pop(i)
            vectorprodu.pop(i)
        i = i + 1
    return

def ordenar(vectorprecio,vectorprodu):
    x = 0
    while x < len(vectorprecio):
        for i in range(len(vectorprecio)-1):
            if vectorprecio[i] < vectorprecio[i + 1]:
                auxprecio = vectorprecio[i]
                vectorprecio[i] = vectorprecio[i+1]
                vectorprecio[i + 1] = auxprecio

                auxprodu = vectorprodu[i]
                vectorprodu[i] = vectorprodu[i + 1]
                vectorprodu[i + 1] = auxprodu
        x = x + 1
    return vectorprecio

cargar(vectorprodu,vectorprecio)

if len(vectorprodu) == 0:
    print("No puede no ingresar nada")

else:
    mostrar(vectorprodu,vectorprecio)

    print("El mayor precio es ",mayorprecio(vectorprecio))

    print("El promedio es:",calcpromedio(vectorprecio))

    print("Despues de eliminar")

    eliminarprodu(vectorprecio)

    mostrar(vectorprodu,vectorprecio)

    print("Los vectores ordenados quedan asi")
    ordenar(vectorprecio,vectorprodu)

    mostrar(vectorprodu,vectorprecio)