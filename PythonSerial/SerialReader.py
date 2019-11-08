
import serial
ser = serial.Serial(port='COM4', baudrate=9600)

#k = open("test.txt", "w")
while(True):
    s = int(ser.readline())
    print(s)

