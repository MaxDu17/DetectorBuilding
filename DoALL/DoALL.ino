
#define REDPIN 13
#define GREENPIN 12
#define BLUEPIN 11
String raw;
String in;

void setup(void) 
{ 
  Serial.begin(9600); 
  pinMode(A0, INPUT);
  
  String status_  = ""; 
  while(status_ != "go")
  {
    Serial.println("ready");
    status_ = Serial.read(); 
  }
  Serial.println("RECEIVED HANDSHAKE");
} 

void loop(void) 
{ 
 raw = analogRead(A0);
 String rawS = String(raw);  
 Serial.println(rawS);
 in = Serial.read();
 if(in == "R")
 {
    digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
 }
 else if(in == "G")
 {
  digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
 }
  else if(in == "B")
 {
 digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
 }

  else if(in == "RG")
  {
digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
  }
    else if(in == "RB")
  {
  digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
  }
    else if(in == "BG")
  {
 digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
  }
      else if(in == "RGB")
  {
  digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
  }
     else if(in == "OFF")
  {
  digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
  }

 
 
}
