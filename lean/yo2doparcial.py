#Es importante tener en cuenta que el nombre del modelo de producto puede ingresar en mayúsculas o minúsculas. Si se ingresa en minúsculas, se debe convertir a mayúsculas. Si no se ingresan datos, mostrar un mensaje y finalizar la ejecución del programa.
#La carga de productos se detendrá cuando se introduzca "FIN" como nombre del producto.
#Mostrar la lista de productos y sus precios en una sola función
#Identificar el producto con el precio más bajo y mostrar su nombre.


#Calcular el promedio de los precios de los productos superiores a 10000.
#Eliminar los valores que superen el precio promedio, junto con sus productos asociados.
#Insertar modelo de producto "PRUEBA" y el importe 999 en la posición siguiente a un precio múltiplo de 3.
#Ordenar de forma ascendente tanto los nombres de los productos como los precios, permitiendo al usuario elegir el criterio de ordenación (por precio o por nombre).

vectormodelo = []
vectorprecio = []
mayoresdiez = []
def cargar(vectorprecio,vectormodelo):
    modelo = input("Ingrese el nombre del modelo: ").upper()
    while modelo != "":
        vectormodelo.append(modelo)
        precio = int(input("Ingrese el precio: "))
        while precio <= 0:
            print("El precio ingresado no puede ser menor o igual a 0")
            precio = int(input("Ingrese el precio: "))
        vectorprecio.append(precio)
        modelo = input("Ingrese el nombre del modelo: ").upper()

def mostrar(vectorprecio,vectormodelo):
     print("Modelo \t\t Precio")
     for i in range (len(vectormodelo)):
         print((vectormodelo[i]),"\t\t", (vectorprecio[i]))

def productomasbajo(vectorprecio,vectormodelo):
    min = vectorprecio[0]
    pos = 0
    for i in range(len(vectorprecio)):
        if vectorprecio[i] < min:
            min = vectorprecio[i]
            pos = vectormodelo[i]
    return pos

def crear_arreglo_mayor(vectorprecio):
    for i in range(len(vectorprecio)):
        if vectorprecio[i] > 10000:
            mayoresdiez.append(vectorprecio[i])
def promedio(mayoresdiez):
    if len(mayoresdiez) == 0:
        print("No hay precios mayores a 10,000")
        return 0
    else:
        suma = 0
        for i in range(len(mayoresdiez)):
            suma = suma + mayoresdiez[i]
        promedio = suma / len(mayoresdiez)
        return promedio

def eliminar(vectorprecio,vectormodelo):
    i = 0
    while i < len(vectorprecio):
        if float(vectorprecio[i]) > float(promedio(mayoresdiez)):
            vectorprecio.pop(i)
            vectormodelo.pop(i)
        i = i + 1


cargar(vectorprecio,vectormodelo)

mostrar(vectorprecio,vectormodelo)

print("El producto de menor precio es:")

print(productomasbajo(vectorprecio,vectormodelo))

crear_arreglo_mayor(vectorprecio)

print("promedio", promedio(mayoresdiez))

eliminar(vectorprecio,vectormodelo)

print("Despues de haber eliminado los modelos mayores al promedio:")

mostrar(vectorprecio,vectormodelo)



