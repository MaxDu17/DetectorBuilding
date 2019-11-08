#include <OneWire.h> 
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 2 
#define REDPIN 13
#define GREENPIN 12
#define BLUEPIN 11

OneWire oneWire(ONE_WIRE_BUS); 
float calibrated[5];
double avg; 
DallasTemperature sensors(&oneWire);
double raw; 
void setup(void) 
{ 
  Serial.begin(9600); 
  sensors.begin(); 
  pinMode(A0, INPUT);

} 

void loop(void) 
{ 
 sensors.requestTemperatures(); // Send the command to get temperature readings 
 for(int i = 0; i < 5; i ++)
 {
  calibrated[i] = sensors.getTempCByIndex(i);
  avg += sensors.getTempCByIndex(i)
 }
 avg = avg/5;
 raw = analogRead(A0);
 Serial.out.println(avg + "\n" + raw); 
  // Why "byIndex"?  
  // You can have more than one DS18B20 on the same bus.  
  // 0 refers to the first IC on the wire 
   delay(1000); 
  
}
