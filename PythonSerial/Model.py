class Model:

    def toVoltage(self, value):
        answer = value * (5.0/1024.0)
        return answer

    def voltageToTemp(self, value):
        answer = -2.6951 * (value ** 3)  + 23.66 * (value ** 2) + -95.274 * (value) + 201.12
        return answer