
"""
este proyecto usa un archivo excel donde estan los datos de multicast de los streams a reproducir (vlc_parsed_xls.xlsx)y los pasa a una lista
vlc-convertido-playlist.xspf



____________________

import pandas as pd, glob

pd.concat([pd.read_csv(f, encoding='latin1') for f in sorted(glob.glob('/mnt/user-data/uploads/SRT-ABC-0*.csv'))]).to_csv('/mnt/user-data/outputs/SRT_consolidados.csv', index=False)

print("✅ Listo: SRT_consolidados.csv")


_____________________________
Son 3 líneas. Cada parte hace una cosa:

glob.glob('...*.csv') → encuentra los archivos por patrón
sorted() → los ordena del 01 al 05
pd.read_csv(f, encoding='latin1') → lee cada archivo
pd.concat([...]) → une todas las filas
.to_csv(..., index=False) → guarda sin agregar columna de índice
Sonnet 4.6 High




"""


import pandas as pd


filepath = "VLC_FILES\\"

"""
global filew
filew = open(f"{filepath}{SRT_IP[3]}.csv", "w")
"""


df = pd.read_excel(f"{filepath}vlc_parsed_xls.xlsx")

ttitulo = df["titulo"]
tprotocolo = df["protocolo"]
tip = df["ip"]
tpuerto = df["puerto"]
tfuente = df["fuente"]

ncant_canales = len(df["ip"])


# rutina para pasar de excel a VLC  >>   xspf

playlist = open(f"{filepath}vlc-convertido-playlist.xspf", "w",encoding="utf-8")

playlist.write(f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
playlist.write(f"<playlist xmlns=\"http://xspf.org/ns/0/\" xmlns:vlc=\"http://www.videolan.org/vlc/playlist/ns/0/\" version=\"1\">\n")
playlist.write(f"	<title>Lista de reproducción</title>\n")
playlist.write(f"	<trackList>\n")


for n in range(ncant_canales):
    tipposta = f"{tprotocolo[n]}://{tfuente[n]}@{tip[n]}:{tpuerto[n]}"

    playlist.write(f"		<track>\n")
    playlist.write(f"			<location>{tipposta}</location>\n")
    playlist.write(f"			<title>{ttitulo[n]}</title>\n")
    playlist.write(f"			<extension application=\"http://www.videolan.org/vlc/playlist/0\">\n")
    playlist.write(f"				<vlc:id>{n}</vlc:id>\n")
    playlist.write(f"				<vlc:option>network-caching=1000</vlc:option>\n")
    playlist.write(f"			</extension>\n")
    playlist.write(f"		</track>\n")


playlist.write(f"	</trackList>\n")
playlist.write(f"	<extension application=\"http://www.videolan.org/vlc/playlist/0\">\n")


for m in range(ncant_canales):
    playlist.write(f"		<vlc:item tid=\"{m}\"/>\n")


playlist.write(f"	</extension>\n")
playlist.write(f"</playlist>\n")


playlist.close()

