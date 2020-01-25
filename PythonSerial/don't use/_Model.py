class Model:

    def toVoltage(self, value):
        answer = value * (5.0/1024.0)
        return answer

    def voltageToTemp(self, value):
        answer = -3.2591 * (value ** 3)  + 29.153 * (value ** 2) + -112.57 * (value) + 218.68
        return answer

    def parseSerial(self, value):
        semantic = str(value)
        semantic = semantic.replace("b'", '')
        semantic = semantic.replace("\\r\\n'", '')
        return semantic