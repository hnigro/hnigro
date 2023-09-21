"""se ingresa:
-factura: no puede ser menor a 0
-producto vendido: pinza 500, tenaza 752, motosierra 1360.
-cantidad vendida (no puede ser negativa)
-nombre del cliente

se pide:
*total facturado
*cantidad vendida por herramienta
*porcentajes de ventas ($) por producto
*el cliente de mayor facturacion individual
*el numero de factura de menor cantidad vendida (venta indivudual)
"""

acumpin = 0
acumten = 0
acummot = 0
contpin = 0
contten = 0
contmot = 0
cl_mayor_facturacion = 0
min_factura = 0
pinza = 500
tenaza = 752
moto = 1360
venta_indiv_total = 0

factura = int(input("Ingrese el numero de factura: "))

while factura < 0:
    print('El numero de factura no puede ser menor a 0')
    factura= int(input("Ingrese el numero de factura: "))

while factura != 0:
    producto = (input("ingrese el producto: pinza, tenaza o motosierra: "))
    nombre = (input('Decime tu nombre'))
    if producto == "pinza":
        cantpin = int(input('Que cantidad de pinzas compraste '))
        acumpin = acumpin + cantpin * pinza
        contpin = contpin + cantpin
    elif producto == 'tenaza':
        cantten = int(input('Que cantidad de tenazas compraste'))
        acumten = acumten + cantten * tenaza
        contten = contten + cantten
    elif producto == 'motosierra':
        cantmot = int(input('Que cantidad de motosierras compraste'))
        acummot = acummot + cantmot * moto
        contmot = contmot + cantmot
    else:
        print('No vendemos eso')
        producto = (input("ingrese el producto: pinza, tenaza o motosierra: "))

    if venta_indiv_total < acumpin + acumten + acummot:
        venta_indiv_total = acumpin + acumten + acummot


    factura = int(input("Ingrese el numero de factura: "))

conttotal = contmot + contten + contpin
ventatotal = acumpin + acumten + acummot
print('La venta total es de :' , ventatotal)
print('La venta de pinzas fue de :' , contpin)
print('La venta de tenazas fue de :' , contten)
print('La venta de motosierras fue de :' , contmot)
print('El porcentaje de ventas de pinzas fue de :', ((contpin * 100)/conttotal))
print('El porcentaje de ventas de tenazas fue de :', ((contten * 100)/conttotal))
print('El porcentaje de ventas de motosierras fue de :', ((contmot * 100)/conttotal))
print(f"el cliente de mayor facturación es: {cl_mayor_facturacion}")

