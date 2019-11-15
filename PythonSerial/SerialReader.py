
import serial
import csv
ser = serial.Serial(port='COM4', baudrate=9600)

k = open("calibration.csv", "w")
dataWriter = csv.writer(k, lineterminator = "\n")

for i in range(10):
    s = str(ser.readline())
    s = s.replace("b'", '')
    s = s.replace("\\r\\n'", '')
    a, b = s.split("&")
    dataWriter.writerow([a, b])
    print(a + "\t" + b)




