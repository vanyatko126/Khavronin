import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.IN)


GPIO.output(20, 0)

while True:
    x = GPIO.input(21)
    if(x==1):
        break
GPIO.output(20, 1)