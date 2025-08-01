import RPi.GPIO as GPIO
import os
import time

# Constants
SOUND_DEVICE = "front:CARD=Device,DEV=0"
ALARM_FILE = "alarm.wav"
VOLUME = 95  # Out of 100
CLOCK = 0.05  # Seconds to wait between checking the sensor(s)

GPIO.setmode(GPIO.BCM)
os.system("amixer set Master " + str(VOLUME) + "%")

# Pins
GPIO.setup(4, GPIO.IN)  # Laser sensor
GPIO.setup(14, GPIO.IN)  # IR sensor

while True:
    laserIn = GPIO.input(4)  # Laser sensor
    irIn = GPIO.input(14)  # IR sensor

    # Prints
    print("Laser:", laserIn)
    print("IR:", irIn)
    
    if (laserIn or irIn):
        os.system("aplay --device " + SOUND_DEVICE + " " + ALARM_FILE)
    time.sleep(CLOCK)