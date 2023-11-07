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
# Recuerden que luego de insertar, eliminar u ordenar se debe mostrar cómo quedan los vectores





"""
arreglo = []

for i in range (5):
    numero = int(input("Ingresa un numero"))
    arreglo.append(numero)

print("Datos cargados")
for i in range (len(arreglo)):
    print(arreglo[i],end="   ")


def hola(numero):
    print("el numero es:", numero)

"""

def existeelemento (arreglo ,elemento):
    existe = False
    for i in range(len(arreglo)):
        if arreglo [i] == elemento:
            existe = True
    return existe

elemento = int(input('decime que numero queres econtrar'))

arreglo = [100,12,15,16,17,18]

print(arreglo)
if existeelemento(arreglo,elemento) == True :
    print('Existe en el arreglo el numero ', elemento )

else:
    print('El',elemento, 'no existe' )

