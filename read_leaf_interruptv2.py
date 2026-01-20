import Encoder
import time
from datetime import datetime

e1 = Encoder.Encoder(6, 13)
e2 = Encoder.Encoder(16, 19)
e3 = Encoder.Encoder(11,  9)
e4 = Encoder.Encoder(25,  8)
e5 = Encoder.Encoder(27, 22)
e6 = Encoder.Encoder(18, 24)

encoder = [e1, e2, e3, e4, e5, e6]

log_file_path = "/home/pi/Desktop/LBIR1251/leaf_log_all.txt"

while (True):
    current_time = datetime.now().strftime("%d%B%Y\t%H:%M:%S")
    line = current_time
    for e in encoder:
        line = line +'\t' + str(e.read())
    print(line)
    file = open(log_file_path, 'a')
    file.write(line + '\n')
    file.close()
    time.sleep(60)

