from picamera import PiCamera
from time import sleep
import time
import datetime as dt
from gpiozero import LED, Button

camera = PiCamera()
led = LED(17)
button = Button(2)

camera.resolution = (1920, 1080)
camera.framerate = 30


while True:

    VideoTime = dt.datetime.now().strftime("%d-%m-%y-%H-%M-%S")
    VideoName = VideoTime + '.h264'
    FilePath = "/home/pi/Desktop/Aufnahme/"
    ComlpeteFilePath = FilePath + VideoName

    button.wait_for_press()
   # camera.start_preview()
    camera.start_recording(ComlpeteFilePath)
    led.on()
    sleep(1)
    
    button.wait_for_press()
   # camera.stop_preview()
    camera.stop_recording()
    led.off()
    sleep(1)
