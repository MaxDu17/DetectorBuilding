
from Model import Model

myModel = Model()


while(True):
    value = float(input("enter in raw analog value"))
    voltage = myModel.toVoltage(value)
    resistance = myModel.toResistance(voltage)
    temperature = myModel.resisToTemp(resistance)


    print("resistance: " + str(resistance) + " , and temperature: " + str(temperature))