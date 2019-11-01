
import serial
ser = serial.Serial(port='COM4', baudrate=9600)
'''
ser.parity = serial.PARITY_ODD
ser.port.open()
ser.port.close()
ser.port.parity = serial.PARITY_NONE
ser.port.close()
'''
#k = open("test.txt", "w")
while(true):
    s = str(ser.readline())
    print(s)

