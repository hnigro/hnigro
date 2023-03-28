# le agrego al principal una funcion Generacion_CSV(SRT_IP):



# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      comienzo interface swagger       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def API_swagger(CSV_file="SRT-ABC-OTT-05.csv"):
    # MAIN SWAGGER INTERFACE
    """
    este programa pasa los archivos csv a swagger

    """

    import os
    from oauthlib.oauth2 import BackendApplicationClient
    from requests_oauthlib import OAuth2Session

    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    """
    SRTIP       =   "http://10.133.96.78:8081/api/v1/login"      #SRT_IP[0]  # IP DEL DISPOSITIVO= /api/v1/login
    client_id="SRT"                                      #SRT_IP[1]  # USER
    client_secret="srtapi2022"                                #SRT_IP[2]  # PASS DEL DISPOSITIVO PARA LA PRIMER CONEXION

    pabloapi
    pabloapi

    """

    client = BackendApplicationClient(client_id="SRT")
    oauth = OAuth2Session(client=client)
    htoken = oauth.fetch_token(token_url="http://10.133.96.78:8081/api/v1/login", client_id="SRT",
                               client_secret="srtapi2022")

    csv_file = {"file": (CSV_file, open(CSV_file, "rb"), "application/vnd.ms-excel")}

    swagger_cmd = "http://10.133.96.78:8081/api/v1/ingest/classes/SRT/entry/csv?overrideValidation=true&hasHeaderRow=true&insertOnly=false&verbose=low&uniqueIdColumns=0"

    swagger_response = oauth.post(url=swagger_cmd, files=csv_file)
    cod_salida = swagger_response.status_code

    print(f"respuesta = {swagger_response.text}")
    print(f"código = {cod_salida}")

    return


# XXXXXXXXXXXXXXXXXXXXX           FIN INTERFACE SWAGGER          xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx




# **********************************************************************************************************************
# *******************      def Generacion_CSV(SRT_IP):  comienzo    *****************************************************

def Generacion_CSV(SRT_IP):
    # **********************************************************************************************************************

    filepath = "CSV_FILES\\"
    global filew
    filew= open(f"{filepath}{SRT_IP[3]}.csv", "w")

    print(f"nombre del archivo creado = {filew.name}")
    # me imprime los títulos de las planillas

    filew.write(
        f"Description,Asset,Asset Type,Route Name,Source Name,Source Mode,Source Interface,Source IP,Source Protocol,Source Port,S_SSM,Source State,Source BW,Last Update,Destination Name,Destination Protocol,Destination Port,Destination Mode,Destination Interface,Destination IP,Destination BW,Destination State\n")

    sroutes = API_int(SRT_IP, "FUNCION")["data"]
    #print(sroutes)

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
            print(len(ROUTE_NAME))
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













# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  ventana comienzo xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def ventana(FFlag, filename):
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
    SRT_CBC_01 = [".) SRT-CBC-01                   ", "10.133.92.150", "haiadmin", "tnstafl2420", "SRT-CBC-01"]
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
        # ,SRT_JBC_OTT_17
        # ,SRT_JBC_OTT_18
    ]

    #  borrar  listbox_texto3 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    listbox_texto3 = {
        # listado de todos los mgm de los SRTs
          "SRT_ABC_01": [".) SRT-ABC-01                   ", "10.177.58.101", "haiadmin", "tnstafl2420", "SRT-ABC-01"]
        , "SRT_ABC_02": [".) SRT-ABC-02                   ", "172.22.99.102", "haiadmin", "tnstafl2420", "SRT-ABC-02"]
        , "SRT_ABC_03": [".) SRT-ABC-03                   ", "10.177.58.103", "haiadmin", "tnstafl2420", "SRT-ABC-03"]
        , "SRT_ABC_04": [".) SRT-ABC-04                   ", "172.22.99.104", "haiadmin", "tnstafl2420", "SRT-ABC-04"]
        , "SRT_CBC_01": [".) SRT-CBC-01                   ", "10.133.92.150", "haiadmin", "tnstafl2420", "SRT-CBC-01"]
        , "SRT_CBC_02": [".) SRT-CBC-02                   ", "172.23.241.150", "haiadmin", "tnstafl2420", "SRT-CBC-02"]
        , "SRT_COBC_01": [".) SRT-COBC-01                  ", "10.177.242.101", "haiadmin", "tnstafl2420", "SRT-COBC-01"]
        , "SRT_COBC_02": [".) SRT-COBC-02                  ", "10.177.231.220", "haiadmin", "tnstafl2420", "SRT-COBC-02"]
        , "SRT_LCF_01": [".) SRT-LCF-01                   ", "172.22.90.1", "haiadmin", "tnstafl2420", "SRT-LCF-01"]
        , "SRT_ABC_OTT_01": [".) SRT-ABC-OTT-01             ", "10.177.30.134", "haiadmin", "manager", "SRT-ABC-OTT-01"]
        , "SRT_ABC_OTT_02": [".) SRT-ABC-OTT-02             ", "10.177.30.135", "haiadmin", "manager", "SRT-ABC-OTT-02"]
        , "SRT_ABC_OTT_03": [".) SRT-ABC-OTT-03             ", "10.177.30.136", "haiadmin", "manager", "SRT-ABC-OTT-03"]
        , "SRT_ABC_OTT_04": [".) SRT-ABC-OTT-04             ", "10.177.30.137", "haiadmin", "manager", "SRT-ABC-OTT-04"]
        , "SRT_ABC_OTT_05": [".) SRT-ABC-OTT-05             ", "10.177.30.138", "haiadmin", "manager", "SRT-ABC-OTT-05"]
        , "SRT_CBC_OTT_06": [".) SRT-CBC-OTT_06             ", "10.133.30.134", "haiadmin", "manager", "SRT-CBC-OTT-06"]
        , "SRT_CBC_OTT_07": [".) SRT-CBC-OTT-07             ", "10.133.30.135", "haiadmin", "manager", "SRT-CBC-OTT-07"]
        , "SRT_CBC_OTT_08": [".) SRT-CBC-OTT-08             ", "10.133.30.136", "haiadmin", "manager", "SRT-CBC-OTT-08"]
        , "SRT_BBC_OTT_09": [".) SRT-BBC-OTT-09             ", "10.19.197.50", "haiadmin", "manager", "SRT-BBC-OTT-09"]
        , "SRT_BBC_OTT_10": [".) SRT-BBC-OTT-10             ", "10.19.197.51", "haiadmin", "manager", "SRT-BBC-OTT-10"]
        , "SRT_BBC_OTT_11": [".) SRT-BBC-OTT-11             ", "10.19.197.52", "haiadmin", "manager", "SRT-BBC-OTT-11"]
        , "SRT_JBC_OTT_12": [".) SRT-JBC-OTT-12             ", "10.219.69.50", "haiadmin", "manager", "SRT-JBC-OTT-12"]
        , "SRT_JBC_OTT_13": [".) SRT-JBC-OTT-13             ", "10.219.69.51", "haiadmin", "manager", "SRT-JBC-OTT-13"]
        , "SRT_JBC_OTT_14": [".) SRT-JBC-OTT-14             ", "10.219.69.52", "haiadmin", "manager", "SRT-JBC-OTT-14"]
        , "SRT_JBC_OTT_15": [".) SRT-JBC-OTT-15             ", "10.219.69.53", "haiadmin", "manager", "SRT-JBC-OTT-15"]
        , "SRT_JBC_OTT_16": [".) SRT-JBC-OTT-16             ", "10.219.69.54", "haiadmin", "manager", "SRT-JBC-OTT-16"]
        , "SRT_JBC_OTT_17": [".) SRT-JBC-OTT-17             ", "10.219.69.55", "haiadmin", "manager", "SRT-JBC-OTT-17"]
        , "SRT_JBC_OTT_18": [".) SRT-JBC-OTT-18             ", "10.219.69.56", "haiadmin", "manager", "SRT-JBC-OTT-18"]
    }
    # print(listbox_texto3.keys())
    # fin borrar lisbox_texto3   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # print(listbox_texto.index(SRT_JBC_OTT_18))
    # print(listbox_texto.__getitem__(10)[1])

    layout = [
        [sg.Text(text=texto, auto_size_text=False, key="nombre_de_archivo")],
        [sg.Listbox(disabled=not FFlag, values=listbox_texto, default_values=SRT_ABC_03, size=(22, 12),
                    key="listbox_01", enable_events=False)],
        [sg.Button("Generate CSV", disabled=not FFlag), sg.Button("Upload_Swagger", disabled=FFlag), sg.Button("Exit")],
        [sg.Button("Update SRTs in Production", disabled=False)]

    ]

    window = sg.Window("SRT Process", layout)

    while True:
        event, values = window.read()
        # print(f"evento = {event}")
        # print(f"valor = {values}")
        if event in ("Exit", None):
            try:
                x
            except Exception as e:
                print(str(e))
                x = "no eligió ningún dispositivo"
            break

        elif event == "Upload_Swagger":
            x = ["Swagger"]

            #importado de abajo
            API_swagger(CSV_file=filew.name)

            break

        elif event == "Generate CSV":
            x = window["listbox_01"].get()
            texto = x[0][0:1][0][3:20]
            window["nombre_de_archivo"].Update(texto)

            break


        #********************************************************************************
        # ********************************************************************************

        elif event == "Update SRTs in Production":
            #SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]
            #abc01SRT_ABC_01
            Generacion_CSV([SRT_ABC_01[1], SRT_ABC_01[2], SRT_ABC_01[3], SRT_ABC_01[4]])
            API_swagger(CSV_file=f"CSV_FILES\\{SRT_ABC_01[4]}.csv")

            # abc02
            Generacion_CSV([SRT_ABC_02[1], SRT_ABC_02[2], SRT_ABC_02[3], SRT_ABC_02[4]])
            API_swagger(CSV_file=f"CSV_FILES\\{SRT_ABC_02[4]}.csv")

            # abc03
            Generacion_CSV([SRT_ABC_03[1], SRT_ABC_03[2], SRT_ABC_03[3], SRT_ABC_03[4]])
            API_swagger(CSV_file=f"CSV_FILES\\{SRT_ABC_03[4]}.csv")

            # abc04
            Generacion_CSV([SRT_ABC_04[1], SRT_ABC_04[2], SRT_ABC_04[3], SRT_ABC_04[4]])
            API_swagger(CSV_file=f"CSV_FILES\\{SRT_ABC_04[4]}.csv")

            # cbc01
            Generacion_CSV([SRT_CBC_01[1], SRT_CBC_01[2], SRT_CBC_01[3], SRT_CBC_01[4]])
            API_swagger(CSV_file=f"CSV_FILES\\{SRT_CBC_01[4]}.csv")

            # cbc02
            Generacion_CSV([SRT_CBC_02[1], SRT_CBC_02[2], SRT_CBC_02[3], SRT_CBC_02[4]])
            API_swagger(CSV_file=f"CSV_FILES\\{SRT_CBC_02[4]}.csv")

            # cobc01
            Generacion_CSV([SRT_COBC_01[1], SRT_COBC_01[2], SRT_COBC_01[3], SRT_COBC_01[4]])
            API_swagger(CSV_file=f"CSV_FILES\\{SRT_COBC_01[4]}.csv")

            # cobc02
            Generacion_CSV([SRT_COBC_02[1], SRT_COBC_02[2], SRT_COBC_02[3], SRT_COBC_02[4]])
            API_swagger(CSV_file=f"CSV_FILES\\{SRT_COBC_02[4]}.csv")

            break

        # ********************************************************************************
        # ********************************************************************************

    window.close()
    return x[0]


# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  ventana fin     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx




# XXXXXXXXXXXXXXXXXXX     comienzo API INT     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
def API_int(SRT_IP, FUNCION):
    #  FUNCION es para crear el CSV teniendo como dato la ip de mgm del srt.
    #

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

    # me toma la info del llamado
    INFO = json.loads(API_CMD.text)

    return INFO


# XXXXXXXXXXXXXXXXXXX      FIN API INT     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx

# XXXXXXXXXXXXXXXXXXX       COMIENZO LAST UPDATE    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def Last_Update():
    import datetime
    # print (datetime.datetime.now())
    now_month = datetime.datetime.now().month
    now_day = datetime.datetime.now().day
    now_year = datetime.datetime.now().year

    last_updated = f"{now_month}/{now_day}/{now_year}"
    return last_updated


# XXXXXXXXXXXXXXXXXXX       FIN LAST UPDATE         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# este es el device que elijo para trabajar
# SRT_IP = SRT_ABC_01



#**********************************************************************************************
#******************       COMIENZO PROGRAMA        ********************************************
#**********************************************************************************************

try:
    SRT_IP0 = ventana(FFlag=True, filename="")
    SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]
    # SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]#esta linea es para listbox_texto3.keys()

except Exception as errorh1:
    print(errorh1)
    quit()

Generacion_CSV(SRT_IP)




try:
    SRT_IP0 = ventana(FFlag=False, filename=filew.name)
    # SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]
    # SRT_IP = SRT_IP0[1], SRT_IP0[2], SRT_IP0[3], SRT_IP0[4]#esta linea es para listbox_texto3.keys()

except Exception as errorh1:
    print(errorh1)
    quit()

"""
if SRT_IP0 == "Swagger":
    API_swagger(CSV_file=filew.name)
"""
input("Press <ENTER> to end")



#**********************************************************************************************
#******************       FIN PROGRAMA        ********************************************
#**********************************************************************************************






