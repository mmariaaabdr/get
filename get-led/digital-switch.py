import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
buttom = 13
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buttom, GPIO.IN)
state = 0

while True:
    if GPIO.input(buttom):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)