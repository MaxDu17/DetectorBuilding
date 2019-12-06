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

        b_1 = 3336.73016
        k_1 = 0.13303
        #the above are for use in resistances GREATER than the threshold

        b_2 =3524.56114
        k_2 =0.07387
        if(resistance > self.transitionresis):
            answer = self.regressModel(resistance, b_1, k_1)
        else:
            answer = self.regressModel(resistance, b_2, k_2)

        return answer



    def parseSerial(self, value):
        semantic = str(value)
        semantic = semantic.replace("b'", '')
        semantic = semantic.replace("\\r\\n'", '')
        return semantic