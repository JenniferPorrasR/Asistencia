import time
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_and_capture_file("prueba.jpg")
