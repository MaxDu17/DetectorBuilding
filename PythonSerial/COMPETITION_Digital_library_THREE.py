import pickle
import serial
from Modelv2 import Model
import time
myModel = Model()

from SerialLibrary import SerialLibrary
serialHelp = SerialLibrary()
BIAS = 0
constant = 0
first = 0
third = 0


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

def calculateVandT(): #running
    s = serialHelp.read_and_parse(ser)

    value = int(s)
    resistance = myModel.raw_to_resistance(value)

    voltage = myModel.toVoltage(value)
    #resistance = myModel.toResistance(voltage)

    temperature = myModel.resisToTemp_v2(resistance, constant, first, third) #this is temporarily removed
    return voltage, temperature

def checkLights(temperature, laststatus): #running
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


def calibrate():
    THRESHOLD = 0.1
    global constant, first, third
    status = input("load calibration from previous? (y, n, s)")
    if (status == "y"):
        try:
            value = pickle.load(open("Cali.pkl", "rb"))
            constant = value[0]
            first = value [1]
            third = value[2]
        except:
            print("whoops, you might not have made a file!")
            quit()
    else:
        t1 = 273.15 + float(input("Temp 1?"))
        r1 = myModel.raw_to_resistance(serialHelp.read_and_parse_flush(ser))
        t2 = 273.15 + float(input("Temp 2?"))
        r2 = myModel.raw_to_resistance(serialHelp.read_and_parse_flush(ser))
        t3 = 273.15 + float(input("Temp 3?"))
        r3 = myModel.raw_to_resistance(serialHelp.read_and_parse_flush(ser))

        constant, first, third = myModel.solve(r1, t1, r2, t2, r3, t3)
        pickle.dump([constant, first, third], open( "Cali.pkl", "wb" ) )
def main():
    laststatus = "OFF"

    setup()
    calibrate()

    while True:
        ser.reset_input_buffer()
        voltage, temperature = calculateVandT()
        temperature = temperature + BIAS
        print("The voltage is: " + str(round(voltage,5)) + "V. The calculated temperature is: " + str(round(temperature,2)) + " degrees Celsius")
        print("c {}\t f {} \t t {}".format(constant, first, third))
        laststatus = checkLights(temperature, laststatus)


if __name__ == '__main__':
    main()