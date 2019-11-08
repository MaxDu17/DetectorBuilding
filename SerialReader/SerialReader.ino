#define REDPIN 13
#define GREENPIN 12
#define BLUEPIN 11
void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);

  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);

}

void loop() {
  Serial.println(analogRead(A0)); 
  delay(500);

}
