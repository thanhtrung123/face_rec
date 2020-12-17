import RPi.GPIO as GPIO #import the GPIO library
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

name = "Ryan"
print("Hello " + name)

while True:
    if GPIO.input(15):
       print("Door is open")
       time.sleep(2)
    if GPIO.input(15) == False:
       print("Door is closed")
       time.sleep(2)