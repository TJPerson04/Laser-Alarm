import RPi.GPIO as GPIO
import os
import time

# Constants
SOUND_DEVICE = "front:CARD=Device,DEV=0"
ALARM_FILE = "alarm.wav"
VOLUME = 95  # Out of 100
CLOCK = 0.05  # Seconds to wait between checking the sensor(s)
IR_MULT = 3  # How many times to loop the alarm if the IR sensor is triggered

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
    
    if (laserIn):
        os.system("aplay --device " + SOUND_DEVICE + " " + ALARM_FILE)
    
    # Run the alarm for longer if the IR sensor is tripped
    if (irIn):
        for i in range(IR_MULT):
            os.system("aplay --device " + SOUND_DEVICE + " " + ALARM_FILE)
    time.sleep(CLOCK)