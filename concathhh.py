import pandas as pd

# 1. Listá acá los archivos que querés unir
archivos = [
    'CSV_FILES\\SRT-ABC-01.csv',
    'CSV_FILES\\SRT-ABC-02.csv',
    'CSV_FILES\\SRT-ABC-03.csv',
    'CSV_FILES\\SRT-ABC-04.csv',
    'CSV_FILES\\SRT-ABC-05.csv',
    'CSV_FILES\\SRT-CBC-01.csv',
    'CSV_FILES\\SRT-CBC-02.csv',
    'CSV_FILES\\SRT-COBC-01.csv',
    'CSV_FILES\\SRT-COBC-02.csv',
]

# 2. Une y guarda
df = pd.concat([pd.read_csv(f, encoding='latin1') for f in archivos], ignore_index=True)
df.to_csv('CSV_FILES\\SRT_consolidadoshh.csv', index=False)

print(f'Archivos unidos : {len(archivos)}')
print(f'Filas totales   : {len(df)}')
print(f'Assets incluidos: {sorted(df["Asset"].unique())}')