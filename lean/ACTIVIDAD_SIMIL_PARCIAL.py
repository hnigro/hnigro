# Ernesto Quintano, quedó a cargo de la empresa familiar "Quintano S.A".
 
# Toda la vida la empresa trabajó utilizando cuadernos y 2 empleados administrativos para registrar los productos fabricados y los precios.
 
# Ernesto, cree que es hora de empezar a informatizar.
 
# Por eso le solicita a Ud. Lo siguiente:
 
# Se leen y se cargan en vectores los siguientes datos:
 
# Modelo de producto, en letras
# Precio unitario, no puede ser negativos ni 0
 
# Cabe destacar además, que el nombre del modelo puede ingresarse en mayúscula o minúscula.
# En el caso de que se ingrese en minúscula, se debe convertir a mayúscula.
# Si la carga es nula (no se ingresaron datos), mostrar una leyenda y finalizar la ejecución.
 
# La carga de productos finaliza cuando se coloca “FIN” en el nombre del producto.
 
# 1) Mostrar en forma de lista de productos y sus precios en una sola función.
# 2) Mostrar el nombre del producto de mayor precio
# 3) Calcular el promedio de los precios
# 4) Eliminar los valores que superen al promedio y sus productos asociados.
# 5) Ordenar ambos vectores, elegir el criterio por precio o producto.
# Recuerden que luego de insertar, eliminar u ordenar se debe mostrar cómo quedan los vecto

#vector producto (mayus o minusc) si se pone fin se termina
#vector precio (no puede ser negaativo ni 0)

#mostrar producto y precio en una sola funcion
#mostrar el nombre de producto de mayor precio
#aliminar los productos q salgan mas del promedio

vectorprodu = []
vectorprecio = []



#mostrar (vectorprodu,vectorprecio)

#mayorprecio(vectorprodu)

#promedio(vectorprecio)

#eliminarmayores (vectorprecio, promedio)

#ordenar(vectorprecio,vectorprodu)

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
        else:
            i = i + 1
    return vectorprecio

def ordenar(vectorprecio):
    vectorprecio.reverse()






cargar(vectorprodu,vectorprecio)

mostrar(vectorprodu,vectorprecio)

print("El mayor precio es ",mayorprecio(vectorprecio))

print("El promedio es:",calcpromedio(vectorprecio))

print("Despues de eliminar")

print("eliminado",eliminarprodu(vectorprecio))

mostrar(vectorprodu,vectorprecio)