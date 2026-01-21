import csv
import time
import os.path

from datetime import datetime

import Encoder

pot1 = Encoder.Encoder(6, 13)
pot2 = Encoder.Encoder(16, 19)
pot3 = Encoder.Encoder(11, 9)
pot4 = Encoder.Encoder(25, 8)
pot5 = Encoder.Encoder(27, 22)
pot6 = Encoder.Encoder(18, 24)

pots = [pot1, pot2, pot3, pot4, pot5, pot6]

fname = 'data/data-{year}.csv'.format(year=datetime.now().strftime("%Y"))

if not os.path.isfile(fname):
    print("Output file does not exists.")
    print("Creating and writing header.")
    
    with open(fname, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        
        # Write header
        writer.writerow(['time', 'pot_1', 'pot_2', 'pot_3', 'pot_4', 'pot_5', 'pot_6'])
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