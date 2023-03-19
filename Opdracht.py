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
Pins = [2, 3, 4, 6]
for i in Pins:
    wiringpi.digitalWrite(i, wiringpi.OUTPUT)

for pin in pins:
    wiringpi.digitalWrite(pin, 0)
time.sleep(0.4)

print("done")