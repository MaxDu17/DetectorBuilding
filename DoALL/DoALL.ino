
#define REDPIN 13
#define GREENPIN 12
#define BLUEPIN 11

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
 switch(in)
 {
  case "R":
    digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
    break;
  case "G":
    digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
    break;
  case "B":
    digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
    break;
  case "RG":
    digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
    break;
  case "RB":
  digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
    break;
  case "BG":
  digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
    break;
  case "RGB":
  digitalWrite(REDPIN, HIGH);
    digitalWrite(GREENPIN, HIGH);
    digitalWrite(BLUEPIN, HIGH);
    Serial.println("Successful");
    break;
  case "OFF":
    digitalWrite(REDPIN, LOW);
    digitalWrite(GREENPIN, LOW);
    digitalWrite(BLUEPIN, LOW);
    Serial.println("Successful");
    break;
  default:
  break
 }
 
}
