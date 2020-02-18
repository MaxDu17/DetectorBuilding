
import serial
import csv
import time
def strip(data):
    data = data.replace("b'", '')
    data = data.replace("\\r\\n'", '')
    a, b = data.split("&")
    return a, int(b)


ser = serial.Serial(port='COM5', baudrate=9600)

k = open("Penn4.csv", "w")
dataWriter = csv.writer(k, lineterminator = "\n")

timeCount = 0

time.sleep(6)
input("press enter to start capture")
ser.reset_input_buffer()
#time.sleep(2)
#print("wait wait wait wait wait wait wait wait")
test = False
while not(test):
    try:
        s = str(ser.readline())
        print(s)

        a, initialMillis = strip(s)
        nextMillis = initialMillis + 1001.3 #this is the lower bound of what to get
        print(nextMillis)
        dataWriter.writerow([0, a])
        test = True
    except:
        print("failed, trying again")

while timeCount <= 7200: #collect data for an hour
    #try:

    #print(str(b) + " and " + str(nextMillis))
    try:
        s = str(ser.readline())
        a, b = strip(s)
        if b >= nextMillis:
            dataWriter.writerow([timeCount+1, a])
            nextMillis += 1001.3 #we keep on incrementing one second
            timeCount += 1
            print(str(timeCount) + "\t" + a + "\t" + str(b) + "\tNext: " + str(nextMillis))
            if (timeCount % 100 == 0 and timeCount > 0):
                k.flush()
                print("flush successful")

    except:
        print("serial oopsy")

    




