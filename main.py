import RPi.GPIO as GPIO
import os
import time

SOUND_DEVICE = "front:CARD=Device,DEV=0"
ALARM_FILE = "yippee-tbh.wav"

GPIO.setmode(GPIO.BCM)
os.system("amixer set Master 100%")

while True:
    GPIO.setup(4, GPIO.IN)
    input = GPIO.input(4)
    print(input)
    if (input):
        os.system("aplay " + SOUND_DEVICE + " " + ALARM_FILE)
    time.sleep(0.5)