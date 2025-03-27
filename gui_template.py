





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

        sg.theme("GrayGrayGray")


        listbox_texto = [
            "SRT_ABC_01"
            , "SRT_ABC_02"
            , "SRT_JBC_OTT_18"
        ]

        # print(listbox_texto.index(SRT_JBC_OTT_18))
        # print(listbox_texto.__getitem__(10)[1])

        layout = [
            [sg.Text(text="textolinea37", auto_size_text=True, key="nombre_de_archivo")],
            [sg.Listbox(disabled=not FFlag, values=listbox_texto, default_values="default value linea38", size=(22, 12),
                        key="listbox_01", enable_events=False)],
            [sg.Button("Generate CSV", disabled=not FFlag), sg.Button("Upload_Arya", disabled=FFlag)],
            [sg.Button("Update DTH SRTs", disabled=False),
             sg.Check("Activate refresh", key="activar_r", enable_events=True)],
            [sg.Button("Exit", )]

        ]

        window = sg.Window("SRT Process", layout, resizable=True, element_justification="center")


        while True:
            event, values = window.read()
            # print(event, values)

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

                    # abc05
                    try:
                        Generacion_CSV([SRT_ABC_05[1], SRT_ABC_05[2], SRT_ABC_05[3], SRT_ABC_05[4]])
                        API_swagger(CSV_file=f"CSV_FILES\\{SRT_ABC_05[4]}.csv")
                    except Exception:
                        print(
                            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx___________SRT_ABC_05_______________excepcion _________________________xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

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





