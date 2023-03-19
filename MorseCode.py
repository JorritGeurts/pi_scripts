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

    if _letter.upper() == "B":
        Dash()
        Dott()
        Dott()
        Dott()
    
    if _letter.upper() == "C":
        Dash()
        Dott()
        Dash()
        Dott()

    if _letter.upper() == "D":
        Dash()
        Dott()
        Dott()
        
    if _letter.upper() == "E":
        Dott()
    
    if _letter.upper() == "G":
        Dash()
        Dash()
        Dott()
    
    if _letter.upper() == "H":
        Dott()
        Dott()
        Dott()
        Dott()

    if _letter.upper() == "I":
        Dott()
        Dott()

    if _letter.upper() == "J":
        Dott()
        Dash()
        Dash()
        Dash()
    
    if _letter.upper() == "K":
        Dash()
        Dott()
        Dash()

    if _letter.upper() == "L":
        Dott()
        Dash()
        Dott()
        Dott()

    if _letter.upper() == "M":
        Dash()
        Dash()

    if _letter.upper() == "N":
        Dash()
        Dott()
    
    if _letter.upper() == "O":
        Dash()
        Dash()
        Dash()

    if _letter.upper() == "P":
        Dott()
        Dash()
        Dash()
        Dott()

    if _letter.upper() == "Q":
        Dash()
        Dash()
        Dott()
        Dash()

    if _letter.upper() == "R":
        Dott()
        Dash()
        Dott()

    if _letter.upper() == "S":
        Dott()
        Dott()
        Dott()

    if _letter.upper() == "T":
        Dash()

    if _letter.upper() == "U":
        Dott()
        Dott()
        Dash()

    if _letter.upper() == "V":
        Dott()
        Dott()
        Dott()
        Dash()

    if _letter.upper() == "W":
        Dott()
        Dott()
        Dash()
    
    if _letter.upper() == "X":
        Dash()
        Dott()
        Dott()
        Dash()

    if _letter.upper() == "Y":
        Dash()
        Dott()
        Dash()
        Dash()

    if _letter.upper() == "B":
        Dash()
        Dash()
        Dott()
        Dott()

    if _letter.upper() == " ":
        wiringpi.digitalWrite(pin,0)
        time.sleep(0.1)


def Dott():
    wiringpi.digitalWrite(pin,1)
    time.sleep(0.1)
    wiringpi.digitalWrite(pin,0)
    time.sleep(0.1)

def Dash():
    wiringpi.digitalWrite(pin,1)
    time.sleep(0.3)
    wiringpi.digitalWrite(pin,0)
    time.sleep(0.1)



#message input
message = str(input("Give your message: "))

#translation
for i in range(len(message)):
    letter = message[i]

    translate(letter)

    wiringpi.digitalWrite(pin,0)
    time.sleep(0.2)
    

print(letter)
