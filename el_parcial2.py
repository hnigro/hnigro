"""se ingresa:
-factura: no puede ser menor a 0
-producto vendido: pinza 500, tenaza 752, motosierra 1360.
-cantidad vendida (no puede ser negativa)
-nombre del cliente

se pide:
*total facturado
*cantidad vendida por herramienta
*porcentajes de ventas ($) por producto
*el cliente de mayor facturacion individual *el numero de factura de menor cantidad vendida (venta indivudual)
"""

acum = 0
acum1 = 0
acum2 = 0
acum3 = 0
cant1 = 0
cant2 = 0
cant3 = 0
mayor = 0
minvta = 0
precio1 = 500
precio2 = 752
precio3 = 1360
total = 0

factura = (input("Ingrese el numero de factura: "))

while factura < 0:
    factura = int(input("La factura no puede ser menor a 0. \n Ingrese el numero de factura: "))

while factura != 0:
    producto = str(input("ingrese el producto: pinza, tenaza o motosierra: "))

    while producto != "pinza" and producto != "tenaza" and producto != "motosierra":
        producto = str(input("Ese no es un valor correcto. Ingrese el nombre del producto: "))

    cantidad = int(input("ingrese la cantidad vendida: "))

    while cantidad < 1:
        cantidad = int(input("la cantidad no puede ser menor a 1,ingrese un nuevo valor: "))

    nombre = input("cuál es su nombre: ")

    if producto == "pinza":
        cant1 = cant1 + cantidad
        fact1 = cantidad * precio1
        acum1 = acum1 + fact1
        if mayor == 0:
            mayor = fact1
            mayornombre = nombre
        if mayor < fact1:
            mayor = fact1
            mayornombre = nombre
        if minvta == 0:
            minvta = cant1
            nummin = factura
        if minvta > cant1:
            minvta = cant1
            nummin = factura

    elif producto == "tenaza":
        cant2 = cant2 + cantidad
        fact2 = cantidad * precio2
        acum2 = acum2 + fact2
        if mayor == 0:
            mayor = fact2
            mayornombre = nombre
        if mayor < fact2:
            mayor = fact2
            mayornombre = nombre
        if minvta == 0:
            minvta = cant2
            nummin = factura
        if minvta > cant2:
            minvta = cant2
            nummin = factura


    elif producto == "motosierra":
        cant3 = cant3 + cantidad
        fact3 = cantidad * precio3
        acum3 = acum3 + fact3
        if mayor == 0:
            mayor = fact3
            mayornombre = nombre
        if mayor < fact3:
            mayor = fact3
            mayornombre = nombre
        if minvta == 0:
            minvta = cant3
            nummin = factura
        if minvta > cant3:
            minvta = cant3
            nummin = factura




    total = acum1 + acum2 + acum3


    factura = int(input("Ingrese el numero de factura: "))

if total !=0:
    print("la cantidad vendida de pinzas es", cant1, "la cantidad de tenazas vendidas es", cant2,
          "la cantidad de motosierras vendidas es", cant3)
    print(" el total facturado es", total)
    print("el porcentaje de ventas en pesos de pinzas es $ es de", acum1 * 100 / total)
    print("el porcentaje de ventas en pesos de tenazas es $ es de", acum2 * 100 / total)
    print("el porcentaje de ventas en pesos de motosierras es $ es de", acum3 * 100 / total)
    print("el cliente de mayor facturacion individual es", mayornombre)
    print("el numero de factura con la menor cantidad es:", nummin)

else:
    print("no han habido ventas")



