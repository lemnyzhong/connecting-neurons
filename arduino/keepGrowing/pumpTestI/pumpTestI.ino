int potentiometer = A0;
int pump = 0;
int val = 0;

void turnOnPump() {
  digitalWrite(pump, HIGH);
}

void turnOffPump() {
  digitalWrite(pump, LOW);
}

int readVal() {
  val = analogRead(potentiometer);
  return val;
}

void setup() {
  Serial.begin(9600);

  pinMode(pump, OUTPUT);

  pinMode(potentiometer, INPUT);

}

void loop() {
  // analogWrite(pump, 155);
  // delay(5000);
  // turnOffPump();
  // delay(5000);
  // turnOnPump();
  // delay(5000);
  // turnOffPump();
  // delay(30000);

}



