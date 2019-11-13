
import serial
ser = serial.Serial(port='COM4', baudrate=9600)

#k = open("test.txt", "w")
while(True):
    s = str(ser.readline())
    _, k, __ = s.split("'")
    q = k.split("\\")
    print(q[0])

