import pickle
import serial
from Model import Model
import time
myModel = Model()

from SerialLibrary import SerialLibrary
serialHelp = SerialLibrary()
BIAS = 0

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
def setup():
    global valuedict
    global ser
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
            valuedict[i] = float(input(translationdict[i] + "_low?"))
            valuedict[i+7] = float(input(translationdict[i] + "_high?"))
        status = input("save for later? (y, n)")
        if(status == "y"):
            pickle.dump( valuedict, open( "RANGES.pkl", "wb" ) )

    ser = serialHelp.connect(portvalue="COM5")
    serialHelp.pair(ser)

def calculateVandT():
    global succ
    s = myModel.parseSerial(ser.readline())

    value = int(s)
    voltage = myModel.toVoltage(value)
    resistance = myModel.toResistance(voltage)
    temperature = myModel.resisToTemp(resistance) #this is temporarily removed
    return voltage, temperature

def checkLights(temperature, laststatus):

    for i in range(1, 8):
        lowerbound = valuedict[i]  # this is just how we get low and high
        higherbound = valuedict[i + 7]
        if (lowerbound == -1 or higherbound == -1):  # this skips irrelevant values
            continue

        if temperature > lowerbound and temperature < higherbound:  # this checks boundaries
            carrier = translationdict[i]  # this is the command needed
            if (carrier != laststatus):  # this is so we don't send the same command
                laststatus = carrier
                print("\tswitching color to: " + carrier)
                ser.write(carrier.encode('utf-8'))


    return laststatus

def main():
    laststatus = "OFF"

    setup()

    while True:
        ser.reset_input_buffer()
        voltage, temperature = calculateVandT()
        temperature = temperature + BIAS
        print("The voltage is: " + str(round(voltage,5)) + "V. The calculated temperature is: " + str(round(temperature,2)) + " degrees Celsius")
        laststatus = checkLights(temperature, laststatus)


if __name__ == '__main__':
    main()