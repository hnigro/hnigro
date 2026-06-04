import pandas as pd, glob

lista_total= ["CSV_FILES\\SRT-ABC-01.csv","CSV_FILES\\SRT-ABC-02.csv","CSV_FILES\\SRT-ABC-03.csv","CSV_FILES\\SRT-ABC-04.csv","CSV_FILES\\SRT-ABC-05.csv","CSV_FILES\\SRT-CBC-01.csv","CSV_FILES\\SRT-CBC-02.csv","CSV_FILES\\SRT-COBC-01.csv","CSV_FILES\\SRT-COBC-02.csv"]
"""
pd.concat(
    [pd.read_csv(f, encoding='latin1') for f in sorted(glob.glob("CSV_FILES\\SRT-ABC-0*.csv"))]).to_csv(
    "CSV_FILES\\SRT_consolidados.csv", index=False)

pdfinal = pd.concat(
    [pd.read_csv(f, encoding='latin1') for f in lista_total]).to_csv(
    "CSV_FILES\\SRT_consolidados.csv", index=False)


df_final = pd.concat(
    [pd.read_csv(f) for f in lista_total], ignore_index=True)



print(" Listo: SRT_consolidados.csv")

"""



# Lista de archivos
archivos = [
    "CSV_FILES\SRT-ABC-01.csv",
    "CSV_FILES\\SRT-ABC-02.csv",
    "CSV_FILES\\SRT-ABC-03.csv",
    "CSV_FILES\\SRT-ABC-04.csv",
    "CSV_FILES\\SRT-ABC-05.csv",
    "CSV_FILES\\SRT-CBC-01.csv",
    "CSV_FILES\\SRT-CBC-02.csv",
    "CSV_FILES\\SRT-COBC-01.csv",
    "CSV_FILES\\SRT-COBC-02.csv"
            ]

# Leer y concatenar
df_final = pd.concat([pd.read_csv(f) for f in archivos], ignore_index=True)

# Guardar el resultado
df_final.to_csv("CSV_FILES\\resultado_concatenado.csv", index=False)

print("✅ Archivos concatenados correctamente.")
