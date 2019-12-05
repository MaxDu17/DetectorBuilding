
import serial
import csv
ser = serial.Serial(port='COM4', baudrate=9600)

k = open("FmInviteCali.csv", "w")
dataWriter = csv.writer(k, lineterminator = "\n")
temp = 0.0
counter = 0
while temp < 95:
    try:
        s = str(ser.readline())
        s = s.replace("b'", '')
        s = s.replace("\\r\\n'", '')
        a, b = s.split("&")
        dataWriter.writerow([a, b])
        print(str(counter) + "\t" + a + "\t" + b)
        temp = float(b)
        counter +=1
    except:
        print("SERIAL ERROR, SKIPPING THIS POINT")
    if(counter % 10 == 0 and counter > 0):
        k.flush()
        print("flush successful")




