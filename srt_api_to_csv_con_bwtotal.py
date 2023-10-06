"""
sincronizado en produccion
07/09/23


"""


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      comienzo interface swagger       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def API_swagger(CSV_file="SRT-ABC-OTT-05.csv"):
    # MAIN SWAGGER INTERFACE
    """
    este programa pasa los archivos csv a swagger
    toma como dato el argumento CSV_file que es un archivo .CSV
    no devuelve argumentos, solo pasa los datos a ARYA

    """

    import os
    from oauthlib.oauth2 import BackendApplicationClient
    from requests_oauthlib import OAuth2Session

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    """
    SRTIP       =   "http://10.133.96.78:8081/api/v1/login"      #SRT_IP[0]  # IP DEL DISPOSITIVO= /api/v1/login
    client_id="SRT"                                      #SRT_IP[1]  # USER
    client_secret="srtapi2022"                                #SRT_IP[2]  # PASS DEL DISPOSITIVO PARA LA PRIMER CONEXION
     otras credenciales
    pabloapi
    pabloapi

    """

    client = BackendApplicationClient(client_id="SRT")
    oauth = OAuth2Session(client=client)
    htoken = oauth.fetch_token(token_url="http://10.133.96.78:8081/api/v1/login", client_id="SRT",
                               client_secret="srtapi2022")

    csv_file = {"file": (CSV_file, open(CSV_file, "rb"), "application/vnd.ms-excel")}

    swagger_cmd = "http://10.133.96.78:8081/api/v1/ingest/classes/SRT/entry/csv?overrideValidation=true&hasHeaderRow=true&insertOnly=false&verbose=low&uniqueIdColumns=0"


    try:
        swagger_response = oauth.post(url=swagger_cmd, files=csv_file)
        cod_salida = swagger_response.status_code
    except Exception:
        print(f"falla en la carga a ARYA len SRT= {csv_file}linea 124 =  {cod_salida}")

    return


# XXXXXXXXXXXXXXXXXXXXX           FIN INTERFACE SWAGGER          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


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
        f"Description,Asset,Asset Type,Route Name,Source Name,Source Mode,Source Interface,Source IP,Source Protocol,Source Port,S_SSM,Source State,Source BW,Last Update,Destination Name,Destination Protocol,Destination Port,Destination Mode,Destination Interface,Destination IP,Destination BW,Destination State,BW In Total,BW Out Total\n")

    sroutes = API_int(SRT_IP, "FUNCION")[0]["data"]
    BW_in_total= API_int(SRT_IP, "FUNCION")[1]
    BW_out_total= API_int(SRT_IP, "FUNCION")[2]
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

            DEST_FORMATTED = f"{DEST_NAME},{D_PROT},{D_PORT},{D_MODE},{D_INT},{D_ADDRESS},{D_BW},{D_STATE},{BW_in_total},{BW_out_total}\n"
            # filew.write(f"{DEST_FORMATTED2_EXTRAS}{DEST_FORMATTED_EXTRAS}")

            n2 += 1

            DEST_FORMATTED_2 = f"{DESCRIPTION},{ASSET},{Asset_Type},{ROUTE_NAME},{SOURCE_NAME},,,,,,,,,{LAST_UPDATE},"
            if n2 == 1: DEST_FORMATTED_2 = f""
            filew.write(f"{DEST_FORMATTED_2}{DEST_FORMATTED}")

    filew.close()


# **********************************************************************************************************************
# *******************      def Generacion_CSV(SRT_IP):  fin    *****************************************************
# **********************************************************************************************************************


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  ventana comienzo xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
class ventana_class:

    def ventana(FFlag, filename):
        """
        este modulo se basa en la funcion ventana que usa el fflaf (file flag) y el filename
        FFlag: en la primer pasada es True porque todavia no tomo el nombre del srt que voy a usar
        en la segunda pasada lo pongo en false porque ya tengo el nombre del archivo y lo voy a pasar a ARYA por la interfaz de swagger


        """

        import PySimpleGUI as sg

        # FFlag es el flag de generación de archivo
        # FFlag = True (todavía no entró el nombre del SRT
        # FFlag = False (ya entró el SRT y voy a pasarlo al SWAGGER y al ARYA)

        if FFlag == False:
            texto = filename
        else:
            texto = "nombre del dispositivo"

        sg.theme("GrayGrayGray")

        # listado de todos los mgm de los SRTs
        SRT_ABC_01 = [".) SRT-ABC-01                   ", "10.177.58.101", "haiadmin", "tnstafl2420", "SRT-ABC-01"]
        SRT_ABC_02 = [".) SRT-ABC-02                   ", "172.22.99.102", "haiadmin", "tnstafl2420", "SRT-ABC-02"]
        SRT_ABC_03 = [".) SRT-ABC-03                   ", "10.177.58.103", "haiadmin", "tnstafl2420", "SRT-ABC-03"]
        SRT_ABC_04 = [".) SRT-ABC-04                   ", "172.22.99.104", "haiadmin", "tnstafl2420", "SRT-ABC-04"]
        SRT_CBC_01 = [".) SRT-CBC-01                   ", "10.133.92.150", "haiadmin", "Vr109!", "SRT-CBC-01"]
        SRT_CBC_02 = [".) SRT-CBC-02                   ", "172.23.241.150", "haiadmin", "tnstafl2420", "SRT-CBC-02"]
        SRT_COBC_01 = [".) SRT-COBC-01                  ", "10.177.242.101", "haiadmin", "tnstafl2420", "SRT-COBC-01"]
        SRT_COBC_02 = [".) SRT-COBC-02                  ", "10.177.231.220", "haiadmin", "tnstafl2420", "SRT-COBC-02"]
        SRT_LCF_01 = [".) SRT-LCF-01                   ", "172.22.90.1", "haiadmin", "tnstafl2420", "SRT-LCF-01"]
        SRT_ABC_OTT_01 = [".) SRT-ABC-OTT-01             ", "10.177.30.134", "haiadmin", "manager", "SRT-ABC-OTT-01"]
        SRT_ABC_OTT_02 = [".) SRT-ABC-OTT-02             ", "10.177.30.135", "haiadmin", "manager", "SRT-ABC-OTT-02"]
        SRT_ABC_OTT_03 = [".) SRT-ABC-OTT-03             ", "10.177.30.136", "haiadmin", "manager", "SRT-ABC-OTT-03"]
        SRT_ABC_OTT_04 = [".) SRT-ABC-OTT-04             ", "10.177.30.137", "haiadmin", "manager", "SRT-ABC-OTT-04"]
        SRT_ABC_OTT_05 = [".) SRT-ABC-OTT-05             ", "10.177.30.138", "haiadmin", "manager", "SRT-ABC-OTT-05"]
        SRT_CBC_OTT_06 = [".) SRT-CBC-OTT_06             ", "10.133.30.134", "haiadmin", "manager", "SRT-CBC-OTT-06"]
        SRT_CBC_OTT_07 = [".) SRT-CBC-OTT-07             ", "10.133.30.135", "haiadmin", "manager", "SRT-CBC-OTT-07"]
        SRT_CBC_OTT_08 = [".) SRT-CBC-OTT-08             ", "10.133.30.136", "haiadmin", "manager", "SRT-CBC-OTT-08"]
        SRT_BBC_OTT_09 = [".) SRT-BBC-OTT-09             ", "10.19.197.50", "haiadmin", "manager", "SRT-BBC-OTT-09"]
        SRT_BBC_OTT_10 = [".) SRT-BBC-OTT-10             ", "10.19.197.51", "haiadmin", "manager", "SRT-BBC-OTT-10"]
        SRT_BBC_OTT_11 = [".) SRT-BBC-OTT-11             ", "10.19.197.52", "haiadmin", "manager", "SRT-BBC-OTT-11"]
        SRT_JBC_OTT_12 = [".) SRT-JBC-OTT-12             ", "10.219.69.50", "haiadmin", "manager", "SRT-JBC-OTT-12"]
        SRT_JBC_OTT_13 = [".) SRT-JBC-OTT-13             ", "10.219.69.51", "haiadmin", "manager", "SRT-JBC-OTT-13"]
        SRT_JBC_OTT_14 = [".) SRT-JBC-OTT-14             ", "10.219.69.52", "haiadmin", "manager", "SRT-JBC-OTT-14"]
        SRT_JBC_OTT_15 = [".) SRT-JBC-OTT-15             ", "10.219.69.53", "haiadmin", "manager", "SRT-JBC-OTT-15"]
        SRT_JBC_OTT_16 = [".) SRT-JBC-OTT-16             ", "10.219.69.54", "haiadmin", "manager", "SRT-JBC-OTT-16"]
        SRT_JBC_OTT_17 = [".) SRT-JBC-OTT-17             ", "10.219.69.55", "haiadmin", "manager", "SRT-JBC-OTT-17"]
        SRT_JBC_OTT_18 = [".) SRT-JBC-OTT-18             ", "10.219.69.56", "haiadmin", "manager", "SRT-JBC-OTT-18"]

        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

        listbox_texto = [
            SRT_ABC_01
            , SRT_ABC_02
            , SRT_ABC_03
            , SRT_ABC_04
            , SRT_CBC_01
            , SRT_CBC_02
            , SRT_COBC_01
            , SRT_COBC_02
            # , SRT_LCF_01
            , SRT_ABC_OTT_01
            , SRT_ABC_OTT_02
            , SRT_ABC_OTT_03
            , SRT_ABC_OTT_04
            , SRT_ABC_OTT_05
            , SRT_CBC_OTT_06
            , SRT_CBC_OTT_07
            , SRT_CBC_OTT_08
            , SRT_BBC_OTT_09
            , SRT_BBC_OTT_10
            , SRT_BBC_OTT_11
            , SRT_JBC_OTT_12
            , SRT_JBC_OTT_13
            , SRT_JBC_OTT_14
            , SRT_JBC_OTT_15
            , SRT_JBC_OTT_16
            , SRT_JBC_OTT_17
            , SRT_JBC_OTT_18
        ]

        # print(listbox_texto.index(SRT_JBC_OTT_18))
        # print(listbox_texto.__getitem__(10)[1])

        layout = [
            [sg.Text(text=texto, auto_size_text=True, key="nombre_de_archivo")],
            [sg.Listbox(disabled=not FFlag, values=listbox_texto, default_values=SRT_ABC_03, size=(22, 12),
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
                try:
                    x
                except Exception as e:
                    print(str(e))
                    x = "no eligió ningún dispositivo"
                break

            elif event == "Upload_Arya":
                x = ["Swagger"]


            elif event == "Generate CSV":
                x = window["listbox_01"].get()
                texto = x[0][0:1][0][3:20]
                window["nombre_de_archivo"].Update(texto)
                break


            elif event == "Update DTH SRTs":
                # activar_cb = True
                while True:

                    # SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]

                    # abc01
                    try:
                        Generacion_CSV([SRT_ABC_01[1], SRT_ABC_01[2], SRT_ABC_01[3], SRT_ABC_01[4]])
                        API_swagger(CSV_file=f"CSV_FILES\\{SRT_ABC_01[4]}.csv")
                    except Exception:
                        print(
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx___________SRT_ABC_01_______________excepcion _________________________xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                    # abc02
                    try:
                        Generacion_CSV([SRT_ABC_02[1], SRT_ABC_02[2], SRT_ABC_02[3], SRT_ABC_02[4]])
                        API_swagger(CSV_file=f"CSV_FILES\\{SRT_ABC_02[4]}.csv")
                    except Exception:
                        print(
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx___________SRT_ABC_02_______________excepcion _________________________xxxxxxxxxxxxxxxxxxxxxxxxxxxx")


                    # abc03
                    try:
                        Generacion_CSV([SRT_ABC_03[1], SRT_ABC_03[2], SRT_ABC_03[3], SRT_ABC_03[4]])
                        API_swagger(CSV_file=f"CSV_FILES\\{SRT_ABC_03[4]}.csv")
                    except Exception:
                        print(
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx___________SRT_ABC_03_______________excepcion _________________________xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                    # abc04
                    try:
                        Generacion_CSV([SRT_ABC_04[1], SRT_ABC_04[2], SRT_ABC_04[3], SRT_ABC_04[4]])
                        API_swagger(CSV_file=f"CSV_FILES\\{SRT_ABC_04[4]}.csv")
                    except Exception:
                        print(
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx___________SRT_ABC_04_______________excepcion _________________________xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                    # cbc01
                    try:
                        Generacion_CSV([SRT_CBC_01[1], SRT_CBC_01[2], SRT_CBC_01[3], SRT_CBC_01[4]])
                        API_swagger(CSV_file=f"CSV_FILES\\{SRT_CBC_01[4]}.csv")
                    except Exception:
                        print(
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx___________SRT_CBC_01_______________excepcion _________________________xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                    # cbc02
                    try:
                        Generacion_CSV([SRT_CBC_02[1], SRT_CBC_02[2], SRT_CBC_02[3], SRT_CBC_02[4]])
                        API_swagger(CSV_file=f"CSV_FILES\\{SRT_CBC_02[4]}.csv")
                    except Exception:
                        print(
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx___________SRT_CBC_02_______________excepcion _________________________xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                    # cobc01
                    try:
                        Generacion_CSV([SRT_COBC_01[1], SRT_COBC_01[2], SRT_COBC_01[3], SRT_COBC_01[4]])
                        API_swagger(CSV_file=f"CSV_FILES\\{SRT_COBC_01[4]}.csv")
                    except Exception:
                        print(
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx___________SRT_COBC_01______________excepcion _________________________xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                    # cobc02
                    try:
                        Generacion_CSV([SRT_COBC_02[1], SRT_COBC_02[2], SRT_COBC_02[3], SRT_COBC_02[4]])
                        API_swagger(CSV_file=f"CSV_FILES\\{SRT_COBC_02[4]}.csv")
                    except Exception:
                        print(
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx___________SRT_COBC_02______________excepcion _________________________xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

                    print("linea 461 _____entra en el loop de refresco")

                    # window["activar_r"].update(values)  # show the event and values in the window
                    activar_cb = window["activar_r"].get()
                    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", activar_cb)
                    window.refresh()  # make sure it's shown immediately
                    # print("VALUES", values)

                    # event, values = window.read()
                    # activar_cb = values["activar_r"]
                    print("Linea 388 activar_cb ====", activar_cb)

                    if activar_cb == False:
                        break

                    elif activar_cb == True:
                        timer()

            # ********************************************************************************
            # ********************************************************************************

        window.close()
        return x[0]


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  ventana fin     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


# XXXXXXXXXXXXXXXXXXX     comienzo API INT     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
def API_int(SRT_IP, FUNCION):
    #  FUNCION es para crear el CSV teniendo como dato la ip de mgm del srt.

    import json
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    session = requests.Session()

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

    apicmd3 = session.get(f"https://{SRTIP}/api/system/metric/snapshot")


    RTA_API_CMD = """{"system":{"uptime":41030403},"memory":{"usedPercent":"35.84"},"loadAvg":{"1m":"6.42","5m":"6.25","15m":"6.02"},"cpu":{"loadPercent":"34.36"},"network":{"receivedMbps":"485.44","sentMbps":"490.50"}}"""

    # el siguiente es el BW de entrada y salida posta del sistema
    # info_del_sistema = apicmd3.text
    BW_in_total = json.loads(apicmd3.text)["network"]["receivedMbps"]
    BW_out_total = json.loads(apicmd3.text)["network"]["sentMbps"]

    print(f"bw recibido en el SRT: {SRT_IP[3]}  posta =====           {BW_in_total}")
    print(f"bw de salida en el SRT: {SRT_IP[3]}  posta posta =====           {BW_out_total}")

    """
    lo siguiente es la info que me entrega la interface cuando le pido el BW del sistema 
    texto de la linea para leer: = {'system': {'uptime': 50703206}, 'memory': {'usedPercent': '25.21'}, 'loadAvg': {'1m': '4.81', '5m': '4.91', '15m': '4.87'}, 'cpu': {'loadPercent': '29.44'}, 'network': {'receivedMbps': '491.02', 'sentMbps': '496.22'}}
    BW_out_total = json.loads(apicmd3.text)["network"]["sentMbps"]

    """

    # me toma la info del llamado
    INFO = json.loads(API_CMD.text)
    return INFO, BW_in_total, BW_out_total


# XXXXXXXXXXXXXXXXXXX      FIN API INT     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx

# XXXXXXXXXXXXXXXXXXX       COMIENZO LAST UPDATE    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def Last_Update():
    import datetime
    last_updated = datetime.datetime.now().strftime("%m/%d/%y %H:%M")
    return last_updated
# XXXXXXXXXXXXXXXXXXX       FIN LAST UPDATE         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# XXXXXXXXXXXXXXXXXXX       COMIENZO TIMER        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def timer():
    import time
    x = time
    print("linea 473 _____antes de time")
    x.sleep(1)
    print("linea 475 _____despues de time")
    return print("return linea 482")
# XXXXXXXXXXXXXXXXXXX       FIN TIMER        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# **********************************************************************************************
# ******************       COMIENZO PROGRAMA        ********************************************
# **********************************************************************************************


def main():
    import PySimpleGUI as sg2
    v = ventana_class

    try:
        SRT_IP0 = v.ventana(FFlag=True, filename="")
        SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]
        # SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]#esta linea es para listbox_texto3.keys()

    except Exception as errorh1:
        print(errorh1)
        quit()

    Generacion_CSV(SRT_IP)

    try:
        SRT_IP0 = v.ventana(FFlag=False, filename=filew.name)
        # SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]
        # SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]#esta linea es para listbox_texto3.keys()

    except Exception as errorh1:
        print(errorh1)
        quit()

    if SRT_IP0 == "Swagger":
        API_swagger(CSV_file=filew.name)

    # input("Press <ENTER> to end")

    sg2.popup(f"finalizar\n ")



# **********************************************************************************************
# ******************       FIN PROGRAMA        ********************************************
# **********************************************************************************************

if __name__ == "__main__":
    main()


