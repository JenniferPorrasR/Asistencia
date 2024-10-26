import time
from picamera2 import Picamera2
from PIL import Image, ImageDraw, ImageFont

# Inicializa la cámara
picam2 = Picamera2()

# Captura la imagen
filename = "prueba.jpg"
picam2.start_and_capture_file(filename)

# Obtén la hora UTC actual
current_time_utc = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())

# Calcula la hora local restando 6 horas a la hora UTC
# time.gmtime() proporciona la hora en UTC, así que restamos 6 horas (21600 segundos)
local_time_epoch = time.time() - 6 * 3600  # Epoch time menos 6 horas
local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(local_time_epoch))

# Abre la imagen capturada
image = Image.open(filename)

# Crea un objeto para dibujar en la imagen
draw = ImageDraw.Draw(image)

# Especifica la fuente y el tamaño
# Asegúrate de que la fuente especificada esté en tu sistema. Puedes cambiarla si es necesario.
font_size = 50  # Tamaño más grande para la fecha y la hora
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)

# Define las posiciones donde se imprimirán las horas
text_position_utc = (10, 10)  # Posición para la hora UTC
text_position_local = (10, 80)  # Posición para la hora local (más abajo para no superponerse)

# Superpone las horas en la imagen
draw.text(text_position_utc, current_time_utc, font=font, fill=(255, 255, 255))
draw.text(text_position_local, local_time, font=font, fill=(255, 255, 255))

# Guarda la imagen con las horas superpuestas
output_filename = "prueba_con_horas.jpg"
image.save(output_filename)

print(f"Imagen guardada como {output_filename} con la hora UTC {current_time_utc} y la hora local {local_time}")
