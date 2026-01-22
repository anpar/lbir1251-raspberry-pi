import RPi.GPIO as GPIO

import csv
import time
import os.path

from datetime import datetime

import Encoder

# Attention : le constructeur (__init__) de la classe Encoder appelle
# setmode(GPIO.BCM) -> les numéros indiqués ci-dessous correspondent donc
# aux numérox des GPIO (c'est important pour le sens de connexion de la broche
# sur le raspberry, parce que ces numéros diffèrent des numéros physiques des
# pins sur la board). Les deux GPIO indiqués ici correspondent à ceux liés
# aux pins CLK et DT sur l'encodeur rotatif.
enc1 = Encoder.Encoder(6, 13)   # e.g., GPIO 6 et GPIO 13
enc2 = Encoder.Encoder(16, 19)
enc3 = Encoder.Encoder(11, 9)
enc4 = Encoder.Encoder(25, 8)
enc5 = Encoder.Encoder(27, 22)
enc6 = Encoder.Encoder(18, 24)

pots = [enc1, enc2, enc3, enc4, enc5, enc6]

# Les GPIOs ci-dessous correpondent à ceux qui ne sont pas utilisés pour la
# lecture des encodeurs. 2 parmi les 3 pour chaque paire d'encodeurs servent
# d'alimentation, le 3e sert soit de GND (peu probable vu que ça marche en les
# mettant tous à HIGH comme ci-dessous) soit à la lecture d'un bouton ?
# 20, 21, 26 pour les encodeurs 1 et 2
# 1, 5, 7 pour les encodeurs 3 et 4
# 10, 17, 23 pour les encodeurs 5 et 5
GPIO.setmode(GPIO.BCM)
GPIOs = [1, 5, 7, 10, 17, 23, 20, 21, 26]

for gpio in GPIOs:
    GPIO.setup(gpio, GPIO.OUT, initial=GPIO.HIGH)

fname = 'data/data-{year}.csv'.format(year=datetime.now().strftime("%Y"))

if not os.path.isfile(fname):
    print("Output file does not exists.")
    print("Creating and writing header.")
    
    with open(fname, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        
        # Write header
        writer.writerow(['time', 'enc_1', 'enc_2', 'enc_3', 'enc_4', 'enc_5', 'enc_6'])
else:
    print("Output file already exists.")
    print("I will append data to the existing file.")
    
while True:
    # Open in append mode, allows to re-start the script without destroying
    # the data if needed (e.g., if something goes wrong in the middle of the
    # experiment)
    with open(fname, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        row = [datetime.now().strftime("%d-%m-%Y %H:%M:%S")] \
            + [pot.read() for pot in pots]     
    
        print("Writing row: " + str(row))
    
        writer.writerow(row)
    
    time.sleep(60)