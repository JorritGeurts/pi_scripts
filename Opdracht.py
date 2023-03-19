import wiringpi
import time
import sys

 def blink(_pin):
     wiringpi.digitalWrite(_pin, 1)
     time.sleep(0.5)
     wiringpi.digitalWrite(_pin, 0)
     time.sleep(0.5)

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
    blink(pin1)
    blink(pin2)
    blink(pin3)
    blink(pin4)


print("done")