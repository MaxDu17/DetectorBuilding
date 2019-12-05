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
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  
  
} 

void loop(void) 
{ 
 sensors.requestTemperatures(); // Send the command to get temperature readings 
 for(int i = 0; i < 5; i ++)
 {
  calibrated[i] = sensors.getTempCByIndex(i);
  avg += sensors.getTempCByIndex(i);
  if(calibrated[i] == -127)
  {
    Serial.println("pullup");
  }
 }
 avg = avg/5;

 
 raw = analogRead(A0);
 raw += analogRead(A1); 
 raw += analogRead(A2); 
 raw += analogRead(A3); 
 raw += analogRead(A4); 
 raw += analogRead(A5); 
 raw /=6; 

 String rawS = String(raw);  
 Serial.println(rawS + "&" + avg); 
  avg = 0; 
  
}
