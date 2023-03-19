import wiringpi
import time
import sys

#def blink(_pin,_pin2):
    #wiringpi.digitalWrite(_pin, 1)
    #wiringpi.digitalWrite(_pin2, 1)
    #time.sleep(0.1)
    #wiringpi.digitalWrite(_pin, 0)
    #wiringpi.digitalWrite(_pin2, 0)
    #time.sleep(0.1)

#setup
print("start")
wiringpi.wiringPiSetup()
pin = 2
sos = [0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 0.5, 0.5, 0.5]

#lights on
for pulse in sos:
    wiringpi.digitalWrite(pin, wiringpi.HIGH)
    time.sleep(pulse)

    wiringpi.digitalWrite(pin, wiringpi.LOW)
    time.sleep(pulse)

print("done")