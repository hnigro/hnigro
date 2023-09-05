"""
este es un archivo donde voy a poner todos los módulos que voy a usar

"""



def API_srt(SRT_IP, FUNCION):
    # XXXXXXXXXXXXXXXXXXX     comienzo API INT     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
    #  FUNCION es para crear el CSV teniendo como dato la ip de mgm del srt.

    import json
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    session = requests.Session()

    #estas dos lineas las uso para debugger
    SRT_ABC_01 = [".) SRT-ABC-01                   ", "10.177.58.101", "haiadmin", "tnstafl2420", "SRT-ABC-01"]
    SRT_IP = SRT_ABC_01
    #borrar las dos lineas cuando use el programa


    SRTIP = SRT_IP[0]  # IP DEL DISPOSITIVO
    SRT_USER = SRT_IP[1]  # USER
    SRT_PASS = SRT_IP[2]  # PASS DEL DISPOSITIVO PARA LA PRIMER CONEXION

    # me loggeo

    srt_login = session.post(
        f"https://{SRTIP}/api/session",
        json={
            "username": SRT_USER,
            "password": SRT_PASS
        },
        verify=False)

    SRT_ID_RAW = session.get(
        f"https://{SRTIP}/api/devices").text  # ID DEL SRT CON CORCHETES E INFO GRAL POCO IMPORTANTE recorta corchetes del texto para que sea reconocible como DICT
    ID = json.loads(SRT_ID_RAW[1:-1])["_id"]  # ID DEL SRT PARA SER USADA EN COMANDOS

    # me imprime el nro de rutas
    API_CMD = session.get(f"https://{SRTIP}/api/gateway/{ID}/routes?page=1&pageSize=300")

    """
    esta instruccion me da info del status de la interface, incluso el BW real de entrada y salida
    apicmd2 = "GET/api/system/metric/snapshot"   
    """

    Api_snapshot_data_raw = session.get(f"https://{SRTIP}/api/system/metric/snapshot")


    RTA_API_CMD = """{"system":{"uptime":41030403},"memory":{"usedPercent":"35.84"},"loadAvg":{"1m":"6.42","5m":"6.25","15m":"6.02"},"cpu":{"loadPercent":"34.36"},"network":{"receivedMbps":"485.44","sentMbps":"490.50"}}"""

    # el siguiente es el BW de entrada y salida posta del sistema
    # info_del_sistema = Api_snapshot_data_raw.text
    BW_received_posta = json.loads(Api_snapshot_data_raw.text)["network"]["receivedMbps"]
    BW_sent_posta = json.loads(Api_snapshot_data_raw.text)["network"]["sentMbps"]

    print(f"bw recibido en el SRT: {SRT_IP[3]}  posta =====           {BW_received_posta}")
    print(f"bw de salida en el SRT: {SRT_IP[3]}  posta posta =====           {BW_sent_posta}")

    """
    lo siguiente es la info que me entrega la interface cuando le pido el BW del sistema 
    texto de la linea para leer: = {'system': {'uptime': 50703206}, 'memory': {'usedPercent': '25.21'}, 'loadAvg': {'1m': '4.81', '5m': '4.91', '15m': '4.87'}, 'cpu': {'loadPercent': '29.44'}, 'network': {'receivedMbps': '491.02', 'sentMbps': '496.22'}}
    BW_sent_posta = json.loads(Api_snapshot_data_raw.text)["network"]["sentMbps"]

    """

    # me toma la info del llamado
    Api_data_raw = json.loads(API_CMD.text)
    # XXXXXXXXXXXXXXXXXXX      FIN API INT     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
    return Api_data_raw


# **********************************************************************************************************************
# *******************      def Generacion_CSV(SRT_IP):  comienzo    *****************************************************
# **********************************************************************************************************************

def Generacion_CSV(SRT_IP):
    # **********************************************************************************************************************
    """
    Esta función toma el argumento de los datos del SRT  SRT_IP
    crea el archivo filew (variable global)

    """

    filepath = "CSV_FILES\\"
    global filew
    filew = open(f"{filepath}{SRT_IP[3]}.csv", "w")

    # esta linea me imprime el nombre del archivo que creé
    # print(f"linea 62 _____nombre del archivo creado = {filew.name}")
    # me imprime los títulos de las planillas

    filew.write(
        f"Description,Asset,Asset Type,Route Name,Source Name,Source Mode,Source Interface,Source IP,Source Protocol,Source Port,S_SSM,Source State,Source BW,Last Update,Destination Name,Destination Protocol,Destination Port,Destination Mode,Destination Interface,Destination IP,Destination BW,Destination State\n")

    sroutes = API_int(SRT_IP, "FUNCION")["data"]
    # esta linea me imprime toda la info sobre la respuesta de las rutas del srt
    # print(sroutes)

    # BW_total(sroutes)

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
                # sdest["usedBandwidth"]
                D_BW = sdest["usedBandwidth"]
            except KeyError:
                D_BW = 0

            DEST_FORMATTED = f"{DEST_NAME},{D_PROT},{D_PORT},{D_MODE},{D_INT},{D_ADDRESS},{D_BW},{D_STATE}\n"
            # filew.write(f"{DEST_FORMATTED2_EXTRAS}{DEST_FORMATTED_EXTRAS}")

            n2 += 1

            DEST_FORMATTED_2 = f"{DESCRIPTION},{ASSET},{Asset_Type},{ROUTE_NAME},{SOURCE_NAME},,,,,,,,,{LAST_UPDATE},"
            if n2 == 1: DEST_FORMATTED_2 = f""
            filew.write(f"{DEST_FORMATTED_2}{DEST_FORMATTED}")
    # **********************************************************************************************************************
    # *******************      def Generacion_CSV(SRT_IP):  fin    *****************************************************
    # **********************************************************************************************************************

    filew.close()









#falta comenzar ventana

def ventana(FFlag, filename):
    """
    este modulo se basa en la funcion ventana que usa el fflaf (file flag) y el filename
    FFlag: en la primer pasada es True porque todavia no tomo el nombre del srt que voy a usar
    en la segunda pasada lo pongo en false porque ya tengo el nombre del archivo y lo voy a pasar a ARYA por la interfaz de swagger
    filename: nombre del archivo que voy a pasar a ARYA

    """

    #variables para activar el programa

    texto ="texto"



    import PySimpleGUI as sg
    layout = [
        [sg.Text(text=texto, auto_size_text=True, key="nombre_de_archivo")],
        [sg.Listbox(disabled=not FFlag, values=listbox_texto, size=(22, 12),
                    key="listbox_01", enable_events=False)],
        [sg.Button("Generate CSV", disabled=not FFlag), sg.Button("Upload_Arya", disabled=FFlag)],
        [sg.Button("Update DTH SRTs", disabled=False),
         sg.Check("Activate refresh", key="activar_r", enable_events=True)],
        [sg.Button("Exit", )]

    ]

    window = sg.Window("SRT Process", layout, resizable=True, element_justification="center")

    """event, values = window.read()
    texto =  values["activar_r"]
    print("xxxxxxxxxxxxxxxxxxxxxxxxx valor de checkbox linea 312 =============", texto)
    """

    while True:
        event, values = window.read()
        # print(event, values)

        # sg.popup("linea 322 _____este es un mensaje de popup")
        if event in ("Exit", None):
            exit(100)


ventana(1, "")

























