"""
09/08/23


"""


class data_model:
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
        # , SRT_JBC_OTT_17
        # ,SRT_JBC_OTT_18
    ]



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
    """
    apicmd2 = "GET/api/system/metric/snapshot"
    apicmd3 = session.get(f"https://{SRTIP}/api/system/metric/snapshot")
    RTA_API_CMD = """{"system":{"uptime":41030403},"memory":{"usedPercent":"35.84"},"loadAvg":{"1m":"6.42","5m":"6.25","15m":"6.02"},"cpu":{"loadPercent":"34.36"},"network":{"receivedMbps":"485.44","sentMbps":"490.50"}}"""

    # el siguiente es el BW de entrada y salida posta del sistema
    apicmd3_json = apicmd3.text
    BW_received_posta = json.loads(apicmd3.text)["network"]["receivedMbps"]
    BW_sent_posta = json.loads(apicmd3.text)["network"]["sentMbps"]

    # print(apicmd3.text)

    print(f"bw recibido posta =====           {BW_received_posta}")
    print(f"bw de salida posta posta =====           {BW_sent_posta}")

    """
    texto de la linea para leer: {'system': {'uptime': 50703206}, 'memory': {'usedPercent': '25.21'}, 'loadAvg': {'1m': '4.81', '5m': '4.91', '15m': '4.87'}, 'cpu': {'loadPercent': '29.44'}, 'network': {'receivedMbps': '491.02', 'sentMbps': '496.22'}}

    """

    # me toma la info del llamado
    INFO = json.loads(API_CMD.text)
    return INFO


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

