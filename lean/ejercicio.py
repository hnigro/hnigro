arregloA = []
arregloB = []
def cargar(arregloA):
    for i in range(5):
        datos = int(input("Carga 10 numeros enteros:"))
        arregloA.append(datos)
    return arregloA

mensaje = 'Los datos cargados son:'

def calcularpromedio(arregloA):
    suma= 0
    for i in range(len(arregloA)):
        suma = suma + arregloA[i]
    if len(arregloA):
        promedio = suma / len(arregloA)
    return promedio

    suma(arregloA)/len(arregloA)
    return sumar(arregloA)/len(arregloA)
def intercambiar(arregloA):
    aux = arregloA[0]
    arregloA[0] = arregloA[len(arregloA)-1]
    arregloA[len(arregloA)-1] = aux
    return arregloA
def insertarcero (arregloA):
    for i in range (0,len(arregloA),1):
        if arregloA[i] > calcularpromedio(arregloA):
            arregloA[i] = 0
        else:
            arregloB.append(arregloA[i])
    return

def maximoB (arregloA):
    i = 0
    max=0
    while i < len(arregloB):
        if arregloB[i] > max:
            max = arregloB[i]
        i = i + 1
    return max




print ("carga del arreglo  ", cargar(arregloA))

print("calculo del promedio  ", calcularpromedio(arregloA))

print("intercambiar primero con ultimo  ",intercambiar(arregloA))

print ("insertar ceros  ", insertarcero(arregloA))

print("arreglo A =" , arregloA)

print("maximo del arreglo b=   ",maximoB(arregloB))

print("arreglo b =", arregloB)