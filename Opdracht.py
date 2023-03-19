import wiringpi
import time
import sys

# def blink(_pin):
#     wiringpi.pinMode(i, 1)
#     time.sleep(0.5)

#setup
print("start")
wiringpi.wiringPiSetup()
Pins = [2, 3, 4, 6]
for pi in Pins:
    wiringpi.pinMode(pi, wiringpi.OUTPUT)

#lights on
for index in range(1,10):
    for pi in Pins:
        wiringpi.digitalWrite(pi, wiringpi.HIGH)
    time.sleep(1)
    

#lights off
for pi in Pins:
    wiringpi.digitalWrite(pi, wiringpi.LOW)
time.sleep(1) 


print("done")