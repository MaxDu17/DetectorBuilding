
#define REDPIN 13
#define GREENPIN 12
#define BLUEPIN 11
int raw;
String in;

void setup(void) 
{ 
  Serial.begin(9600); 
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
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
 raw += analogRead(A1); 
 raw += analogRead(A2); 
 raw += analogRead(A3); 
 raw += analogRead(A4); 
 raw += analogRead(A5); 
 raw /=6; 
 String rawS = String(raw);  
 Serial.println(rawS);
 in = Serial.readString();
 in.trim();
 if(in.equals("R"))
 {
    digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, LOW);
   
 }
 else if(in.equals("G"))
 {
  digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, LOW);
    
 }
  else if(in.equals("B"))
 {
 digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, HIGH);
    
 }

  else if(in.equals("RG"))
  {
digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, LOW);
    
  }
    else if(in.equals("RB"))
  {
  digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, HIGH);
   
  }
    else if(in.equals("BG"))
  {
 digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, HIGH);
   
  }
      else if(in.equals("RGB"))
  {
  digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, HIGH);
   
  }
     else if(in.equals("OFF"))
  {
  digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, LOW);
   
  }

 
 
}
