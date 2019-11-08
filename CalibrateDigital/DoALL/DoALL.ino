#include <OneWire.h> 
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 2 
OneWire oneWire(ONE_WIRE_BUS); 
float calibrated[5];

DallasTemperature sensors(&oneWire);
void setup(void) 
{ 
 Serial.begin(9600); 
 sensors.begin(); 
} 
void loop(void) 
{ 
 sensors.requestTemperatures(); // Send the command to get temperature readings 
 for(int i = 0; i < 5; i ++)
 {
  calibrated[i] = sensors.getTempCByIndex(i);
 }
 
 Serial.print(sensors.getTempCByIndex(0)); 
  // Why "byIndex"?  
   // You can have more than one DS18B20 on the same bus.  
   // 0 refers to the first IC on the wire 
   delay(1000); 
}
