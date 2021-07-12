#include "DHT.h"

//Define o pin digital 4 do arduíno
#define DHTPIN 4
#define DHTTYPE DHT22   



DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  
  dht.begin();
}

void loop() {
  
  delay(2000);

  
  float h = dht.readHumidity();
  //Leitura de umidade
  float t = dht.readTemperature();
  //Leitura da temperatura em Celcius
  
  // VErificação de leitura.
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Falha de leitura do sensor!"));
    return;
  }

  Serial.print(h);
  Serial.print(F(","));
  Serial.print(t);
  
}
