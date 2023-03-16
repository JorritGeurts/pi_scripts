import wiringpi
import time
import sys

# def blink(_pin):
#     wiringpi.pinMode(i, 1)
#     time.sleep(0.5)

print("start")
wiringpi.wiringPiSetup()
Pins = [2, 3, 4, 6]
for i in Pins:
    wiringpi.pinMode(i, 0)

for index in range(1,10):
    wiringpi.pinMode(i, 1)
    time.sleep(1)

print("done")