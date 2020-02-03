import math

class Model:
    transitionresis = 5068

    def toVoltage(self, value):
        answer = value * (5.0/1024.0)
        return answer

    def toResistance(self, value): # converts voltage to resistance
        resistor = 1196
        volt = 5
        num = value * resistor
        denom = volt - value
        resis = num / denom
        return resis

    def regressModel(self, resistance, B, K): #this is a plug and chug
        num = B
        denom = math.log((resistance/K))
        temp = num/denom
        temp = temp - 273.15 #kelvin conversion
        return temp


    def resisToTemp(self, resistance):

        third = -4.69025551730340000000E-09
        second = 4.63543381558865000000E-06
        first = 2.14112850892514000000E-04
        constant = 1.00219715468020000000E-03

        recip = third * (math.log(resistance) ** 3) + second * (math.log(resistance) ** 2) + first * (math.log(resistance)) + constant
        kelvin = 1/recip
        answer = kelvin - 273.15
        return answer



    def parseSerial(self, value):
        semantic = str(value)
        semantic = semantic.replace("b'", '')
        semantic = semantic.replace("\\r\\n'", '')
        return semantic