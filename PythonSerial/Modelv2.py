import math
import numpy as np

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
        third = -2.86036246840982000000E-06
        second = 6.97198515460829000000E-05
        first = -2.83654501267028000000E-04
        constant = 2.26504661351262000000E-03
        '''
        #not used right now
        third = -3.09377938834121000000E-06
        second = 7.59957169700599000000E-05
        first =  -3.38040907667832000000E-04
        constant = 2.41934979987930000000E-03
        '''

        recip = third * (math.log(resistance) ** 3) + second * (math.log(resistance) ** 2) + first * (
            math.log(resistance)) + constant
        kelvin = 1 / recip
        answer = kelvin - 273.15
        return answer

    def resisToTemp_v2(self, resistance, constant, first, third):
        recip = third * (math.log(resistance) ** 3) + first * (math.log(resistance)) + constant
        kelvin = 1 / recip
        answer = kelvin - 273.15
        return answer

    def raw_to_resistance(self, raw): #wrapper function
        return self.toResistance(self.toVoltage(raw))

    def parseSerial(self, value): #for old
        semantic = str(value)
        semantic = semantic.replace("b'", '')
        semantic = semantic.replace("\\r\\n'", '')
        return semantic

    def solve(self, r1, t1, r2, t2, r3, t3): #must be in kelvin
        a = np.array([[1, math.log(r1), math.log(r1)**3],[1, math.log(r2), math.log(r2)**3],
                     [1, math.log(r3), math.log(r3)**3]])
        b = np.array([1/t1, 1/t2, 1/t3])
        x = np.linalg.solve(a, b)

        constant = x[0]
        first = x[1]
        third = x[2]

        return constant, first, third
