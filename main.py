import RPi.GPIO as GPIO
import os
import time

# Constants
SOUND_DEVICE = "front:CARD=Device,DEV=0"
ALARM_FILE = "alarm.wav"
VOLUME = 100  # Out of 100
CLOCK = 0.1  # Seconds to wait between checking the sensor(s)

GPIO.setmode(GPIO.BCM)
os.system("amixer set Master " + str(VOLUME) + "%")

# Pins
GPIO.setup(4, GPIO.IN)  # Laser sensor


while True:
    input = GPIO.input(4)
    print(input)
    if (input):
        os.system("aplay --device " + SOUND_DEVICE + " " + ALARM_FILE)
    time.sleep(CLOCK)