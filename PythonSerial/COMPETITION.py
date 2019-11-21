import pickle
import serial
import csv
from Model import Model
import time
myModel = Model()
valuedict = { #note: add 7 to the original value to get the lower bound
    1: -1, #R_low
    2 : -1, #G_low
    3 : -1, #B_low
    4 : -1, #"RG_low
    5 : -1,#"RB_low
     6: -1,#"BG_low
    7: -1,#"RGB_low
     8: -1,#"R_up
    9: -1,#"G_up
     10: -1,#"B_up
     11: -1,#"RG_up
     12: -1,#"RB_up
    13: -1,#"BG_up
     14: -1#"RGB_up
}

translationdict = {
1: "R",
    2 : "G",
    3 : "B",
    4 : "RG",
    5 : "RB",
     6: "BG",
    7: "RGB"

}
print("-----------SETUP------------")
status = input("load from previous? (y, n, s)")
if(status == "y"):
    try:
        valuedict = pickle.load(open("RANGES.pkl", "rb"))
    except:
        print("whoops, you might not have made a file!")
        quit()

elif(status == "n"):
    for i in range(1, 8):
        valuedict[i] = int(input(translationdict[i] + "_low?"))
        valuedict[i+7] = int(input(translationdict[i] + "_high?"))
        status = input("save for later? (y, n)")
        if(status == "y"):
            pickle.dump( valuedict, open( "RANGES.pkl", "wb" ) )


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
change = False
count = 0
while True:

    s = myModel.parseSerial(ser.readline())
    value = int(s)
    voltage = myModel.toVoltage(value)
    temperature = myModel.voltageToTemp((voltage))
    count++
    if(count % 10 == 0):
        print("The voltage is: " + str(round(voltage,2)) + "V. The calculated temperature is: " + str(round(temperature,2)) + " degrees Celsius")

    if(change):
        ser.write(sendstatus.encode('utf-8'))
        print("awaiting color change protocol")
        semantic = "no"
        while semantic != "Successful":
            semantic = myModel.parseSerial(ser.readline())
        change = False


    for i in range(1,8):
        lowerbound = valuedict[i]
        higherbound = valuedict[i + 7]
        if(lowerbound  == -1 or higherbound == -1):
            continue

        if temperature > lowerbound and temperature < higherbound:
            carrier = translationdict[i]
            if(carrier != laststatus):
                sendstatus = carrier
                change = True






