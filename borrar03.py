# Importar el módulo subprocess para ejecutar comandos externos con ffmpeg
import subprocess

# Definir el nombre del archivo de video
video_file = "video.mp4"

# Construir el comando de ffmpeg para reproducir el video
# El argumento -i indica el archivo de entrada
# El argumento -f indica el formato de salida
# El argumento - indica que el resultado se envía a la salida estándar
ffmpeg_command = ["ffmpeg", "-i", video_file, "-f", "sdl", "-"]

# Ejecutar el comando de ffmpeg usando subprocess
# El argumento stdout=subprocess.PIPE indica que se captura la salida estándar
# El argumento stderr=subprocess.STDOUT indica que se redirige la salida de error a la salida estándar
process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Leer la salida estándar del proceso y mostrarla en la consola
# El método readline() lee una línea de la salida estándar
# El método decode() convierte los bytes a una cadena de texto
# El bucle while se ejecuta mientras haya líneas para leer
while True: 
    output = process.stdout.readline()
    if output:
        print(output.decode())
    else:
        break
