import wiringpi
import time
import sys

#setup
wiringpi.wiringPiSetup()
pin = 2
wiringpi.pinMode(pin, 1)

#message input
message = str(input("Give your message: "))

#translation
for i in range(len(message)):
    letter = message[i]

print(letter)
