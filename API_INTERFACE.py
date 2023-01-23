"""
11/8/22
aca pruebo la nueva interface para agregar nuevas funcionalidades

"""


class ventana:

    #import PySimpleGUI as sg

    def __init__(self,FFlag, filename):
        self.FFlag = FFlag
        self.filename = filename

    global ok_result

    def ventana2(self):
        import PySimpleGUI as sg
        sg.theme("GrayGrayGray")

        #FFlag es el flag de generación de archivo
        #FFlag = True (todavía no entró el nombre del SRT
        #FFlag = False (ya entró el SRT y voy a pasarlo al SWAGGER y al ARYA)

        if self.FFlag == False:
            texto = self.filename
        else:
            texto = "nombre del dispositivo"


        from os import walk, getcwd
        def dir(ruta=getcwd()):
            listaarchivos = []
            for (_, _, archivos) in walk(f"{ruta}/CSV_FILES"):
                listaarchivos.extend(archivos)
            return listaarchivos

        # listado de todos los mgm de los SRTs
        SRT_ABC_01          =   [".) SRT-ABC-01                     ","10.177.58.101", "haiadmin", "tnstafl2420", "SRT-ABC-01"]
        SRT_ABC_02          =   [".) SRT-ABC-02                     ","172.22.99.102", "haiadmin", "tnstafl2420", "SRT-ABC-02"]
        SRT_ABC_03          =   [".) SRT-ABC-03                     ","10.177.58.103", "haiadmin", "tnstafl2420", "SRT-ABC-03"]
        SRT_ABC_04          =   [".) SRT-ABC-04                     ","172.22.99.104", "haiadmin", "tnstafl2420", "SRT-ABC-04"]
        SRT_CBC_01          =   [".) SRT-CBC-01                     ","10.133.92.150", "haiadmin", "tnstafl2420", "SRT-CBC-01"]
        SRT_CBC_02          =   [".) SRT-CBC-02                     ","172.23.241.150", "haiadmin", "tnstafl2420", "SRT-CBC-02"]
        SRT_COBC_01         =   [".) SRT-COBC-01                    ","10.177.242.101", "haiadmin", "tnstafl2420", "SRT-COBC-01"]
        SRT_COBC_02         =   [".) SRT-COBC-02                    ","10.177.231.220", "haiadmin", "tnstafl2420", "SRT-COBC-02"]
        SRT_LCF_01          =   [".) SRT-LCF-01                     ","172.22.90.1",    "haiadmin", "tnstafl2420", "SRT-LCF-01"]
        SRT_ABC_OTT_01    =     [".) SRT-ABC-OTT-01                 ","10.177.30.134", "haiadmin", "manager", "SRT-ABC-OTT-01"]
        SRT_ABC_OTT_02    =     [".) SRT-ABC-OTT-02                 ","10.177.30.135", "haiadmin", "manager", "SRT-ABC-OTT-02"]
        SRT_ABC_OTT_03    =     [".) SRT-ABC-OTT-03                 ","10.177.30.136", "haiadmin", "manager", "SRT-ABC-OTT-03"]
        SRT_ABC_OTT_04    =     [".) SRT-ABC-OTT-04                 ","10.177.30.137", "haiadmin", "manager", "SRT-ABC-OTT-04"]
        SRT_ABC_OTT_05    =     [".) SRT-ABC-OTT-05                 ","10.177.30.138", "haiadmin", "manager", "SRT-ABC-OTT-05"]
        SRT_CBC_OTT_06    =     [".) SRT-CBC-OTT_06                 ","10.133.30.134", "haiadmin", "manager", "SRT-CBC-OTT-06"]
        SRT_CBC_OTT_07    =     [".) SRT-CBC-OTT-07                 ","10.133.30.135", "haiadmin", "manager", "SRT-CBC-OTT-07"]
        SRT_CBC_OTT_08    =     [".) SRT-CBC-OTT-08                 ","10.133.30.136", "haiadmin", "manager", "SRT-CBC-OTT-08"]
        SRT_BBC_OTT_09    =     [".) SRT-BBC-OTT-09                 ","10.19.197.50", "haiadmin", "manager", "SRT-BBC-OTT-09"]
        SRT_BBC_OTT_10    =     [".) SRT-BBC-OTT-10                 ","10.19.197.51", "haiadmin", "manager", "SRT-BBC-OTT-10"]
        SRT_BBC_OTT_11    =     [".) SRT-BBC-OTT-11                 ","10.19.197.52", "haiadmin", "manager", "SRT-BBC-OTT-11"]
        SRT_JBC_OTT_12    =     [".) SRT-JBC-OTT-12                 ","10.219.69.50", "haiadmin", "manager", "SRT-JBC-OTT-12"]
        SRT_JBC_OTT_13    =     [".) SRT-JBC-OTT-13                 ","10.219.69.51", "haiadmin", "manager", "SRT-JBC-OTT-13"]
        SRT_JBC_OTT_14    =     [".) SRT-JBC-OTT-14                 ","10.219.69.52", "haiadmin", "manager", "SRT-JBC-OTT-14"]
        SRT_JBC_OTT_15    =     [".) SRT-JBC-OTT-15                 ","10.219.69.53", "haiadmin", "manager", "SRT-JBC-OTT-15"]
        SRT_JBC_OTT_16    =     [".) SRT-JBC-OTT-16                 ","10.219.69.54", "haiadmin", "manager", "SRT-JBC-OTT-16"]
        SRT_JBC_OTT_17    =     [".) SRT-JBC-OTT-17                 ","10.219.69.55", "haiadmin", "manager", "SRT-JBC-OTT-17"]
        SRT_JBC_OTT_18    =     [".) SRT-JBC-OTT-18                 ","10.219.69.56", "haiadmin", "manager", "SRT-JBC-OTT-18"]


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
            #, SRT_LCF_01
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
            #, SRT_JBC_OTT_17
            #, SRT_JBC_OTT_18
        ]
        layout = [
            [sg.Text(text=texto,auto_size_text= False, key="nombre_de_archivo")],
            [sg.Listbox(disabled=False,values=listbox_texto, size=(22, 12), key="listbox_01", enable_events=False)],
            [sg.Button("Generate CSV",disabled=False,tooltip="Generate .CSV file from the selected SRT"), sg.Button("Upload_Swagger",disabled= False,tooltip="Upload the selected device to ARYA"),sg.Button("Use .CSV file",tooltip="Use .CSV file to upload to ARYA")],
            [sg.Button("Ok", disabled=False), sg.Button("Exit", disabled=False)]
            ]

        layout_original = [
            [sg.Text(text=texto,auto_size_text= False, key="nombre_de_archivo")],
            [sg.Listbox(disabled=not self.FFlag,values=listbox_texto,default_values = SRT_ABC_03, size=(22, 12), key="listbox_01", enable_events=False)],
            [sg.Button("Generate CSV",disabled=not self.FFlag,tooltip="Generate .CSV file from the selected SRT"), sg.Button("Upload_Swagger",disabled= self.FFlag,tooltip="Upload the selected device to ARYA"),sg.Button("Use .CSV file",tooltip="Use .CSV file to upload to ARYA")],
            [sg.Button("Ok", disabled=False), sg.Button("Exit", disabled=False)]
            ]

        window = sg.Window("SRT Process", layout)

        """   13/5/22
        generacion de lista de archivos

        """


        #print(dir())


        while True:
            event, values = window.read()
            if event in ("Exit", None):
                """
                try:
                    x
                except Exception as e:
                    #print(str(e))
                    x = "no eligió ningún dispositivo"
                """
                break

            #si upload, primero carga archivo y despues lo sube a swagger
            if event == "Upload_Swagger":
                #x = ["Swagger"]
                print("eligio upload swagger")
                window.read()
                #return x[0]



            if event == "Generate CSV":
                #x = window["listbox_01"].get()
                #if x == []: x = ["011234567890123456789","011234567890123456789", "011234567890123456789", "011234567890123456789", "011234567890123456789"]
                #texto = x[0][0:1][0][3:20]
                #window["nombre_de_archivo"].Update(texto)
                print("generar csv")
                window.read()




            if event == "Use .CSV file":
                window["listbox_01"].Update(values=dir())
                window.Read()
                x = window["listbox_01"].get()
                #texto = x[0]
                print(f"opcion use .CSV = {x[0]}")
                window["nombre_de_archivo"].Update(texto)
                print("eligio generar .csv file")

                #return x[0]



            if event == "Ok":
                ok_result = "ok presionado"
                return print("ok presionado")

        window.close()




"""
pruebo la clase ventana

"""
v1 = ventana(FFlag = True, filename  = "xxx")


x2= v1.ventana2()
print(x2)
print()




#if x2[0] != "":
    #v1 = ventana(FFlag = True, filename  = "xxx")
    #x2 = v1.ventana2()
    #print(x2)

"""
fin de la clase ventana
"""






























