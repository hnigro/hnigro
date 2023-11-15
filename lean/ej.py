temp = []
vol = []

def cargar(temp,vol):
    for i in range(3):
        numtemp = int(input("Ingrese la temperatura: "))
        temp.append(numtemp)
        numvol = int(input("Ingrese el volumen: "))
        vol.append(numvol)


def mostrar(vol,temp):
    print("TEMPERATURA  \t\t  VOLUMEN")
    for i in range(len(vol)):
        print(temp[i]," \t\t\t\t ",(vol[i]))

def max(temp):
    tempmax = 0
    for i in range(len(temp)):
        if temp[i] > tempmax:
            tempmax = temp[i]
    return tempmax

def min(temp):
    tempmin = max(temp)
    for i in range(len(temp)):
        if temp[i] < tempmin:
            tempmin = temp[i]
    return tempmin

#def ordenar(temp):
   # print(temp.reverse())
 #   return temp



cargar(temp,vol)

mostrar(vol,temp)


print("La mayor tempera tura registrada fue :",max(temp))

print("Y la menor temperatura registrada fue :",min(temp))

print("temp =", temp)
print("Las temperaturas ordenadas de mayor a menor quedan asi:")
print(temp.reverse())