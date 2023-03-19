import wiringpi
import time
import sys

#setup
wiringpi.wiringPiSetup()
pin = 2
wiringpi.pinMode(pin, 1)

def translate(_letter):
    if _letter.upper() == "A":
        Dott()
        Dash()
        

def Dott():
    wiringpi.digitalWrite(pin,1)
    time.sleep(0.1)
    wiringpi.digitalWrite(pin,0)
    time.sleep(0.1)

def Dash():
    wiringpi.digitalWrite(pin,1)
    time.sleep(0.5)
    wiringpi.digitalWrite(pin,0)
    time.sleep(0.1)



#message input
message = str(input("Give your message: "))

#translation
for i in range(len(message)):
    letter = message[i]

    translate(letter)
    

print(letter)
