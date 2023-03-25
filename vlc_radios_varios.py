
"""
programa
Este programa lo que hace es transformar un grupo de radios en formatos de hls, etc a udp o RTP
16/1/23


"""
"""
nuevo proyecto para usar vlc

1) Vlc Mosaic
2) Vlm por Python
3) Re-encodear streams
4) Vlc por SRT



"""

import os #extensiones de sistema operativo
import shutil #operaciones copiando y sobreescribiendo
import subprocess
#from subprocess import PIPE, run #podemos correr cualquier instrucción en el sistema operativo como linea de comandos
import sys #me da acceso a los argumentos de la linea de comandos


class cpaths:
    path_video1 = "C:\\Users\\cnigro\\borrar\\videotest1.mp4"
    path_video2 = "C:\\Users\\cnigro\\borrar\\videotest2.mp4"
    path_video3 = "C:\\Users\\cnigro\\borrar\\videotest3.mp4"
    path_video4 = "C:\\Users\\cnigro\\borrar\\videotest4.mp4"
    path_bg     = "C:\\Users\\cnigro\\borrar\\bkgr_white.jpg"
    mosaic_vlm = " C:\\Users\\cnigro\\borrar\\test_vlm_mosaic6_hh.vlm"
    radios_vlm = " C:\\Users\\cnigro\\borrar\\test_vlm_radios_bbc_hh.vlm"
    radios_vlm_2 = "vlm_script\\test_vlm_radios_bbc_hh.vlm"

    tx_srt = "dshow:// :sout=#transcode{vcodec=h264,vb=800,scale=Automatisch,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:duplicate{dst=srt{mux=ts,dst=localhost:9000?mode=caller},dst=display} :no-sout-all :sout-keep"
    video_live = "srt://168.195.108.102:10045"

def main():
    cwd = os.getcwd()
    path1 = cpaths

    #import subprocess
    #"C:\\Users\\cnigro\\borrar\\videotest1.mp4"
    #p = subprocess.Popen(["vlc.exe", "C:\\Users\\cnigro\\borrar\\videotest1.mp4"])
    #esta instruccion es para abrir un video
    #p = subprocess.Popen(["vlc.exe", path1.path_video1])

    #Esta instrucción es para abrir un mosaico con vlm o el grupo de radios
    vlm_mosaic = subprocess.Popen(["vlc.exe", "-vvv", "--vlm-conf",path1.radios_vlm_2])
    #vlc_play = subprocess.Popen(["vlc.exe", "-vvv", cpaths.video_live])

    args = sys.argv
    #print(args)



if __name__ == "__main__":
    args = sys.argv
    #print(args)

main()











































