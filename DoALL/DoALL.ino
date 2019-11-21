
#define REDPIN 13
#define GREENPIN 12
#define BLUEPIN 11
String raw;
String in;

void setup(void) 
{ 
  Serial.begin(9600); 
  pinMode(A0, INPUT);
  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT); 
  String status_  = ""; 
  while(!status_.equals("go"))
  {
    Serial.println("ready");
    status_ = Serial.readString(); 
    status_.trim(); 
  }
  Serial.println("RECEIVED HANDSHAKE");
} 

void loop(void) 
{ 
 raw = analogRead(A0);
 String rawS = String(raw);  
 Serial.println(rawS);
 in = Serial.readString();
 in.trim();
 if(in.equals("R"))
 {
    digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
 }
 else if(in.equals("G"))
 {
  digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
 }
  else if(in.equals("B"))
 {
 digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
 }

  else if(in.equals("RG"))
  {
digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
  }
    else if(in.equals("RB"))
  {
  digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
  }
    else if(in.equals("BG"))
  {
 digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
  }
      else if(in.equals("RGB"))
  {
  digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
  }
     else if(in.equals("OFF"))
  {
  digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
  }

 
 
}
