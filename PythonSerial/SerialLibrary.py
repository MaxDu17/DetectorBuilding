from serial.tools import list_ports
import serial

class SerialLibrary():

    def parseSerial(self, value):
        semantic = str(value)
        semantic = semantic.replace("b'", '')
        semantic = semantic.replace("\\r\\n'", '')
        return semantic

    def read_and_parse(self, ser):
        return self.parseSerial(ser.readline())

    def read_and_parse_flush(self, ser):
        ser.reset_input_buffer()
        return self.parseSerial(ser.readline())

    def connect(self, portvalue = 'COM5'):
        try:
            ser = serial.Serial(port=portvalue, baudrate=9600)
            # ser = serial.Serial(port='COM8', baudrate=9600)
        except:
            print("sorry, this port is busy or not correct. double check programs!")
            ports = list(list_ports.comports())
            print("here are the available ports: " + str([k.device for k in ports]))
            quit()
        return ser

    def pair(self, ser):
        assert not(ser == None), "you didn't call connect()"

        semantic = "no"
        while semantic != "ready":
            semantic = self.parseSerial(ser.readline())
        print("RECEIVED HANDSHAKE")
        ser.write('go'.encode('utf-8'))
        while semantic != "RECEIVED HANDSHAKE":
            semantic = self.parseSerial(ser.readline())
        print("SUCCESSFUL PAIRING")
