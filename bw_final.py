





"""
bw posta
para esto voy a usar también el prueba_desde_cero

va a formar varios módulos:

API_int(SRT_ID): la idea de este módulo es que se conecte con el dispositivo y obtenga los datos crudos que necesitamos
_SRT_ID es la id del dispositivo donde figura la ip, usuario, pass
_apicmd3 es la respuesta que voy a tener después de hacer el llamado a la API
_BW_received_posta es el dato del BW recibido que saco de apicmd3-
_BW_sent_posta es el dato del BW de salida que saco de apicmd3-
_el return que voy a devolver es:BW_received_posta y BW_sent_posta



"""





# XXXXXXXXXXXXXXXXXXX     comienzo API INT     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
def API_int(SRT_ID):

    #  FUNCION es para crear el CSV teniendo como dato la ip de mgm del srt.

    import json
    import requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    session = requests.Session()


    # me loggeo

    srt_login = session.post(
        f"https://172.22.99.104/api/session",
        json={
            "username": "haiadmin",
            "password": "tnstafl2420"
        },
        verify=False)
       #apicmd2 = "https://172.22.99.104/api/system/metric/snapshot"
    apicmd3 = session.get("https://172.22.99.104/api/system/metric/snapshot")
    RTA_API_CMD = """{"system":{"uptime":41030403},"memory":{"usedPercent":"35.84"},"loadAvg":{"1m":"6.42","5m":"6.25","15m":"6.02"},"cpu":{"loadPercent":"34.36"},"network":{"receivedMbps":"485.44","sentMbps":"490.50"}}"""

    #el siguiente es el BW de entrada y salida posta del sistema
    apicmd3_json = apicmd3.text
    BW_received_posta = json.loads(apicmd3.text)["network"]["receivedMbps"]
    BW_sent_posta = json.loads(apicmd3.text)["network"]["sentMbps"]

    #print(apicmd3.text)

    encabezado = ["SRT	BW INPUT","BW OUTPUT","BW OUTPUT REMAINING","LAST UPDATE"]
    print(f"SRT	BW INPUT	BW OUTPUT	BW OUTPUT REMAINING	LAST UPDATE\n")
    print(f"bw recibido posta        =====          {BW_received_posta}")
    print(f"bw de salida posta posta =====          {BW_sent_posta}")



    """
    texto de la linea para leer: {'system': {'uptime': 50703206}, 'memory': {'usedPercent': '25.21'}, 'loadAvg': {'1m': '4.81', '5m': '4.91', '15m': '4.87'}, 'cpu': {'loadPercent': '29.44'}, 'network': {'receivedMbps': '491.02', 'sentMbps': '496.22'}}

    """
    return BW_received_posta,BW_sent_posta



# XXXXXXXXXXXXXXXXXXX      FIN API INT     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx




API_int("SRT_ID")




