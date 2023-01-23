# **********************************************************************************************************************
# *******************      def Generacion_CSV(SRT_IP):  comienzo    *****************************************************

def Generacion_CSV(SRT_IP):
    # **********************************************************************************************************************

    filepath = "CSV_FILES\\"
    global filew
    filew = open(f"{filepath}{SRT_IP[3]}.csv", "w")

    print(f"linea 62 _____nombre del archivo creado = {filew.name}")
    # me imprime los títulos de las planillas

    filew.write(
        f"Description,Asset,Asset Type,Route Name,Source Name,Source Mode,Source Interface,Source IP,Source Protocol,Source Port,S_SSM,Source State,Source BW,Last Update,Destination Name,Destination Protocol,Destination Port,Destination Mode,Destination Interface,Destination IP,Destination BW,Destination State\n")

    sroutes = API_int(SRT_IP, "FUNCION")["data"]
    # print(sroutes)

    # hace un listado de las rutas con sus fuentes
    for svalue in sroutes:

        ASSET = SRT_IP[3]
        Asset_Type = "Broadcast"
        ROUTE_NAME = svalue["name"]
        R_STATE_NAME = svalue["state"]
        SOURCE_NAME = svalue["source"]["name"]
        DESTINATIONS = svalue["destinations"]
        ROUTE_ID = svalue["id"]  # lo voy a usar si quiero estadisticas de la ruta

        S_INT = svalue["source"]["networkInterface"]
        S_MODE = svalue["source"]["mode"]
        S_ADDRESS = svalue["source"]["address"]
        S_PROT = svalue["source"]["protocol"].upper()
        S_PORT = svalue["source"]["port"]
        S_STATE = svalue["source"]["state"]
        S_BW = svalue["source"]["usedBandwidth"]
        LAST_UPDATE = Last_Update()

        try:
            svalue["source"]["sourceAddress"]
            S_SSM = svalue["source"]["sourceAddress"]
        except KeyError:
            S_SSM = "0.0.0.0"
        n = 0

        # generacion de nro de digitos para la fuente (genera 2 digitos para 99 rutas y 3 digitos para mas de 99 en el source)
        if len(ROUTE_NAME) > 3:
            if ROUTE_NAME[2] == "_":
                DIGITS = ROUTE_NAME[0:2]
            elif ROUTE_NAME[3] == "_":
                DIGITS = ROUTE_NAME[0:3]
            else:
                DIGITS = ROUTE_NAME
        else:
            print(f"linea 41 _____", len(ROUTE_NAME))
            DIGITS = ROUTE_NAME

        DESCRIPTION_SOURCE = f"{ASSET}-{DIGITS}-{n + 1}"
        # fin generacion de nro de digitos para la fuente (genera 2 digitos para 99 rutas y 3 digitos para mas de 99 en el source)

        # print(DESCRIPTION_SOURCE)
        # agrego asset y description
        filew.write(
            f"{DESCRIPTION_SOURCE},{ASSET},{Asset_Type},{ROUTE_NAME},{SOURCE_NAME},{S_MODE},{S_INT},{S_ADDRESS},{S_PROT},{S_PORT},{S_SSM},{S_STATE},{S_BW},{LAST_UPDATE},")

        #   inicializacion de variables de formateo del destino

        DEST_FORMATTED_2 = f""

        # si la fuente no tiene destinos entonces saltea la linea (porque de lo contrario me imprime la ruta siguiente en
        # el lugar del destino de la ruta anterior
        if DESTINATIONS == []:
            filew.write(f"\n")

        #   imprime cada uno de los datos de destino por cada destino
        n2 = 0
        for sdest in DESTINATIONS:
            DEST_NAME = sdest["name"]
            D_PROT = sdest["protocol"].upper()
            D_PORT = sdest["port"]
            D_MODE = sdest["mode"]
            D_INT = sdest["networkInterface"]
            D_ADDRESS = sdest["address"]
            D_STATE = sdest["state"]

            if len(ROUTE_NAME) > 3:
                if ROUTE_NAME[2] == "_":
                    DIGITS = ROUTE_NAME[0:2]
                elif ROUTE_NAME[3] == "_":
                    DIGITS = ROUTE_NAME[0:3]
            else:
                DIGITS = ROUTE_NAME

            DESCRIPTION = f"{ASSET}-{DIGITS}-{n2 + 1}"

            # esta variable me tira error si la fuente no está activada. por eso tratamiento de errores
            try:
                sdest["usedBandwidth"]
                D_BW = sdest["usedBandwidth"]
            except KeyError:
                D_BW = ""

            DEST_FORMATTED = f"{DEST_NAME},{D_PROT},{D_PORT},{D_MODE},{D_INT},{D_ADDRESS},{D_BW},{D_STATE}\n"
            # filew.write(f"{DEST_FORMATTED2_EXTRAS}{DEST_FORMATTED_EXTRAS}")

            n2 += 1

            DEST_FORMATTED_2 = f"{DESCRIPTION},{ASSET},{Asset_Type},{ROUTE_NAME},{SOURCE_NAME},,,,,,,,,{LAST_UPDATE},"
            if n2 == 1: DEST_FORMATTED_2 = f""
            filew.write(f"{DEST_FORMATTED_2}{DEST_FORMATTED}")

    filew.close()


# **********************************************************************************************************************
# *******************      def procesamiento(SRT_IP):  fin    **********************************************************
# **********************************************************************************************************************


def BW_total(sroutes):
    #determinacion de BW en source
    S_BW_total=0
    D_BW_total=0
    for svalue in sroutes:
        S_BW = svalue["source"]["usedBandwidth"]
        S_BW_total = S_BW_total + S_BW

        DESTINATIONS = svalue["destinations"]
        if DESTINATIONS == []:
            filew.write(f"\n")


        for sdest in DESTINATIONS:
            try:
                #sdest["usedBandwidth"]
                D_BW = float(sdest["usedBandwidth"])
                D_BW_total = D_BW_total + D_BW
            except KeyError:
                D_BW = 0

    return print(f"ancho de banda de entrada = {S_BW_total}   ______ \n ancho de banda salida = {D_BW_total}")







