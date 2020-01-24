import pickle
import serial
from Model import Model
import time
myModel = Model()
from serial.tools import list_ports

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

    try:
        ser = serial.Serial(port='COM4', baudrate=9600)
        #ser = serial.Serial(port='COM6', baudrate=9600)
    except:
        print("sorry, this port is busy or not correct. double check programs!")
        ports = list(list_ports.comports())
        print("here are the available ports: " + str([k.device for k in ports]))
        quit()

    semantic = "no"
    while semantic != "ready":
        semantic = myModel.parseSerial(ser.readline())
    print("RECEIVED HANDSHAKE")
    ser.write('go'.encode('utf-8'))
    while semantic != "RECEIVED HANDSHAKE":
        semantic = myModel.parseSerial(ser.readline())
    print("SUCCESSFUL PAIRING")


def calibrate():
    global BIAS
    answer = input("load from existing data? (y, n)")
    if answer == "y":
        try:
            BIAS = pickle.load(open("BIAS.pkl", "rb"))
        except:
            print("whoops! file doesn't exist.")
            quit()
    else:
        truth = int(input("what is the baseline?"))
        measured, _ = getSample(10, 0.3)
        print("the offset is " + str(truth - measured))
        answer = input("do you want to assign this bias to the entire system? (y, n)")
        if answer == "y":
            BIAS = truth - measured
            answer = input("save? (y, n)")
            if answer == "y":
                pickle.dump(BIAS, open("BIAS.pkl", "wb"))
        else:
            print("calibration data discarded")

def calculateVandT():
    s = myModel.parseSerial(ser.readline())
    value = int(s)
    voltage = myModel.toVoltage(value)
    resistance = myModel.toResistance(voltage)
    temperature = myModel.resisToTemp(resistance)
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

def getSample(number, threshold):
    counter = 0
    total = 0
    totalv = 0
    giveupcount = 0
    ser.reset_input_buffer()
    while(counter < number):
        voltage, temperature = calculateVandT()
        print("getting value " + str(counter) + ", which is " + str(round(temperature, 3)))
        if(counter == 0):
            runningavg = temperature
        else:
            runningavg = total/(counter)
        if(temperature > (runningavg + threshold) or temperature < (runningavg - threshold)):
            print("dropped value")
            giveupcount += 1
        else:
            total += temperature
            totalv += voltage
            counter += 1
        if(giveupcount > 10):
            break #this prevents bogus values from holding up the code


    return (total/number + BIAS), totalv/number



def main():
    laststatus = "OFF"
    semantic = "y"
    counter = 0
    setup()

    status = input("are you in calibrate mode? (y, n)")
    if (status == "y"):
        calibrate()

    while True:
        if counter % 20 == 0:
            semantic = input("What do you want? Continuous (c), sample (s)")
        if semantic == "c":
            ser.reset_input_buffer()
            voltage, temperature = calculateVandT()
            temperature = temperature + BIAS
            print("The voltage is: " + str(round(voltage,2)) + "V. The calculated temperature is: " + str(round(temperature,2)) + " degrees Celsius")
            laststatus = checkLights(temperature, laststatus)


            counter += 1
        elif semantic == "s":
            num = int(input("how many values do you want to average?"))
            threshold = float(input("at what threshold?"))
            avgtemp, avgvolt = getSample(num, threshold)
            avgtempadj = avgtemp + BIAS
            print("The average voltage is: " + str(round(avgvolt, 2)) + "V. The average calculated temperature (adjusted) is: " + str(
                round(avgtempadj, 2)) + " degrees Celsius")
            input("press enter to continue")
            counter = 20 #kinda a stupid way to get a new option to come about



if __name__ == '__main__':
    main()