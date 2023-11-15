#ingresae turnos
#ver turnos
#eliminar turnos
#ver estadisticas
#salir

#23 pacientes por dia
#nombre ,numero de socio ,horario ,tratamiento :control ,arreglocaries ,ortodoncia ,extraccion
#mostrar todos los turnos ordenados de menor a mayor segun el horsrio asignado mostrando todos los datos de cada paciente


vecnombres = []
vecnumeros = []
vechora = []
vectratamientos = []
def cargar(vecnombres,vecnumeros,vechora,vectratamientos):
    for i in range(5):
        nombres =(input("Ingrese el nombre del paciente: "))
        vecnombres.append(nombres)
        numeros = (int(input("Ingrese el numero de socio: ")))
        vecnumeros.append(numeros)
        tiempo = int(input("Ingrese la hora del turno"))
        while tiempo < 8 or tiempo > 20:
            tiempo = int(input("Los turnos solo pueden ser de 8 a 20 hs ,ingrese la hora: "))
        vechora.append(tiempo)
        tratamiento=(input("Ingrese que tratamiento hara:Ortodoncia , Control ,Arreglo ,Extraccion: ")).upper()
        while tratamiento != "ORTODONCIA " or tratamiento != 'CONTROL' or tratamiento != "ARREGLO" or tratamiento != "EXTRACCION":
            tratamiento = input("Por favor ingrese un tratamiento valido: ").upper()
        vectratamientos.append(tratamiento)




cargar(vecnombres , vecnumeros ,vechora ,vectratamientos)




