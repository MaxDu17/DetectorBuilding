
import serial
import csv
ser = serial.Serial(port='COM4', baudrate=9600)

k = open("calibration_cold.csv", "w")
dataWriter = csv.writer(k, lineterminator = "\n")

for i in range(5000):
    try:
        s = str(ser.readline())
        s = s.replace("b'", '')
        s = s.replace("\\r\\n'", '')
        a, b = s.split("&")
        dataWriter.writerow([a, b])
        print(str(i) + "\t" + a + "\t" + b)
    except:
        print("SERIAL ERROR, SKIPPING THIS POINT")
        i = i - 1
    if(i % 10 == 0 and i > 0):
        k.flush()
        print("flush successful")




