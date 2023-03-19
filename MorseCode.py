import wiringpi
import time
import sys

#setup
wiringpi.wiringPiSetup()
pin = 2
wiringpi.pinMode(pin, 1)

#input
message = str(input("Give your message"))

print(message)
