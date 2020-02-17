
import serial
import csv
import time
def strip(data):
    data = data.replace("b'", '')
    data = data.replace("\\r\\n'", '')
    a, b = data.split("&")
    return a, int(b)


ser = serial.Serial(port='COM8', baudrate=9600)

k = open("UpennCali.csv", "w")
dataWriter = csv.writer(k, lineterminator = "\n")

timeCount = 0

time.sleep(6)
input("press enter to start capture")
ser.reset_input_buffer()
time.sleep(0.05)
print("buff")
s = str(ser.readline())
print(s)

_, initialMillis = strip(s)
nextMillis = initialMillis + 1000 #this is the lower bound of what to get
print(nextMillis)


while timeCount < 3600: #collect data for an hour
    #try:
    s = str(ser.readline())
    a, b = strip(s)
    #print(str(b) + " and " + str(nextMillis))
    try:
        if b >= nextMillis:
            dataWriter.writerow([a])
            nextMillis += 1000 #we keep on incrementing one second
            timeCount += 1
            print(str(timeCount) + "\t" + a + "\t" + str(b) + "\tNext: " + str(nextMillis))
            if (timeCount % 10 == 0 and timeCount > 0):
                k.flush()
                print("flush successful")

    except:
        print("serial oopsy")

    




