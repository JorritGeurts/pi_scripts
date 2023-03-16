import RPi.GPIO as GPIO
import time

# set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

# loop to flash LED
while True:
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.5)  # adjust this interval to change the flashing rate
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.5)