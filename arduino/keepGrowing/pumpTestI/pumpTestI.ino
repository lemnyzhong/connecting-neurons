// int potentiometer = A0;
int pump = 13;
int reset = 4;
int val = 0;

void turnOnPump() {
  digitalWrite(pump, HIGH);
}

void turnOffPump() {
  digitalWrite(pump, LOW);
}

// int readVal() {
//   val = analogRead(potentiometer);
//   return val;
// }

void setup() {
  Serial.begin(9600);

  pinMode(pump, OUTPUT);

  digitalWrite(4, HIGH);
  pinMode(4, OUTPUT);
}

void loop() {
  unsigned long time = millis();
  Serial.println(time);

  if (time > 5000) {
    turnOnPump();
  }

  if (time > 10000) {
    digitalWrite(4, LOW);
  }

}



