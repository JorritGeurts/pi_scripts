import wiringpi
import time
import sys

def blink(_pin,_pin2):
     wiringpi.digitalWrite(_pin, 1)
     wiringpi.digitalWrite(_pin2, 1)
     time.sleep(0.1)
     wiringpi.digitalWrite(_pin, 0)
     wiringpi.digitalWrite(_pin2, 0)
     time.sleep(0.1)

#setup
print("start")
wiringpi.wiringPiSetup()
pin1 = 2
wiringpi.pinMode(pin1,1)

wiringpi.wiringPiSetup()
pin2 = 3
wiringpi.pinMode(pin2,1)

wiringpi.wiringPiSetup()
pin3 = 4
wiringpi.pinMode(pin3,1)

wiringpi.wiringPiSetup()
pin4 = 6
wiringpi.pinMode(pin4,1)

#lights on
for i in range(1,4):
    for i in range(1,6):
        blink(pin1,pin3)
    for i in range(1,6):
        blink(pin2,pin4)

print("done")