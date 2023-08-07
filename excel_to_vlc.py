
"""
este proyecto usa un archivo excel donde estan los datos de multicast de los streams a reproducir (vlc_parsed_xls.xlsx)y los pasa a una lista
vlc-convertido-playlist.xspf
"""


import pandas as pd


filepath = "VLC_FILES\\"

"""
global filew
filew = open(f"{filepath}{SRT_IP[3]}.csv", "w")
"""


df = pd.read_excel(f"{filepath}vlc_parsed_xls.xlsx")
#print (f"DF ============hh\nhh==================={df}\n\n")
ttitulo = df["titulo"]
tprotocolo = df["protocolo"]
tip = df["ip"]
tpuerto = df["puerto"]
tfuente = df["fuente"]

#print(ttitulo[0:])

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

