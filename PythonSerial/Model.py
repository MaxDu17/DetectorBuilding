import math


class Model:
    r_bottom = 1500 + 120 + 120  # these are approximate values only
    r_top = 2200

    def toVoltage(self, value):
        print(value)
        answer = value * (5.0/65536.0)
        return answer

    def toResistance(self, value): # converts voltage to resistance
        source_voltage = 5.0
        voltagedifference = value
        non_var_side = source_voltage * self.r_bottom / (self.r_bottom + self.r_top)

        absvoltage = non_var_side + voltagedifference

        numerator = absvoltage * self.r_top
        denomenator = source_voltage - absvoltage
        resis = numerator / denomenator
        return resis

    def resisToTemp(self, resistance):
        third = -2.70539185771856000000E-06
        second = 6.60086236619423000000E-05
        first = -2.53817749918175000000E-04
        constant = 2.18681334419397000000E-03

        '''
        #not used right now
        third = -2.86036246840982000000E-06
        second = 6.97198515460829000000E-05
        first = -2.83654501267028000000E-04
        constant = 2.26504661351262000000E-03
        '''

        '''
        #not used right now
        third = -3.09377938834121000000E-06
        second = 7.59957169700599000000E-05
        first =  -3.38040907667832000000E-04
        constant = 2.41934979987930000000E-03
        '''


        recip = third * (math.log(resistance) ** 3) + second * (math.log(resistance) ** 2) + first * (math.log(resistance)) + constant
        kelvin = 1/recip
        answer = kelvin - 273.15
        return answer

    def parseSerial(self, value): #for old
        semantic = str(value)
        semantic = semantic.replace("b'", '')
        semantic = semantic.replace("\\r\\n'", '')
        return semantic

