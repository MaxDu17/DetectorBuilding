
import serial
import csv
from Model import Model

#NOTE MAKE CSV PARSER
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
for i in range(1, 8):
    valuedict[i] = int(input(translationdict[i] + "_low?"))
    valuedict[i+7] = int(input(translationdict[i] + "_high?"))




ser = serial.Serial(port='COM4', baudrate=9600)
semantic = "no"
while semantic != "ready":
    semantic = str(ser.readline())
    semantic = semantic.replace("b'", '')
    semantic = semantic.replace("\\r\\n'", '')
print("RECEIVED HANDSHAKE")
ser.write('go'.encode('utf-8'))
while semantic != "RECEIVED HANDSHAKE":
    semantic = str(ser.readline())
    semantic = semantic.replace("b'", '')
    semantic = semantic.replace("\\r\\n'", '')
print("SUCCESSFUL PAIRING")

sendstatus = "OFF"
laststatus = "OFF"
change = False
while True:
    try:
        s = str(ser.readline())
        s = s.replace("b'", '')
        s = s.replace("\\r\\n'", '')
        value = int(s)
        voltage = myModel.toVoltage(value)
        temperature = myModel.voltageToTemp((voltage))
        print("The voltage is: " + voltage + "V. The calculated temperature is: " + temperature + " degrees Celsius")

        if(change):
            ser.write(sendstatus.encode('utf-8'))
            print("awaiting color change protocol")
            semantic = "no"
            while semantic != "Successful":
                semantic = str(ser.readline())
                semantic = semantic.replace("b'", '')
                semantic = semantic.replace("\\r\\n'", '')
            change = False


        for i in range(1,8):
            lowerbound = valuedict[i]
            higherbound = valuedict[i + 7]

            if temperature > lowerbound and temperature < higherbound:
                carrier = translationdict[i]
                if(carrier != laststatus):
                    sendstatus = carrier
                    change = True




    except:
        print("small serial error")





