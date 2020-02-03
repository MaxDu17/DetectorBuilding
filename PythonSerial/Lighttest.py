import pickle
import serial
import csv
from Model import Model
import time
myModel = Model()

translationdict = {
1: "R",
    2 : "G",
    3 : "B",
    4 : "RG",
    5 : "RB",
     6: "BG",
    7: "RGB"

}


ser = serial.Serial(port='COM4', baudrate=9600)
semantic = "no"
while semantic != "ready":
    semantic = myModel.parseSerial(ser.readline())
print("RECEIVED HANDSHAKE")
ser.write('go'.encode('utf-8'))
while semantic != "RECEIVED HANDSHAKE":
    semantic = myModel.parseSerial(ser.readline())
print("SUCCESSFUL PAIRING")

sendstatus = "OFF"
laststatus = "OFF"
count = 0
while True:
    command = input("your command")

    ser.write(command.encode('utf-8'))







