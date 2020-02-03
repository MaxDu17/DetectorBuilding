import math


class Model:
    r_bottom = 1500 + 120 + 120  # these are approximate values only
    r_top = 2200

    def toVoltage(self, value):
        answer = value * (5.0/65536.0)
        return answer

    def toResistance(self, value): # converts voltage to resistance
        source_voltage = 5.0
        voltagedifference = value
        non_var_side = source_voltage * self.r_top / (self.r_bottom + self.r_top)
        absvoltage = non_var_side + voltagedifference

        numerator = absvoltage * self.r_top
        denomenator = source_voltage - absvoltage
        resis = numerator / denomenator
        return resis

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