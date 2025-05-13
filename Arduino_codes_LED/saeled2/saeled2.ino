#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Update these with values suitable for your network.
 //test.mosquitto.org
 //broker.hivemq.org
const char* ssid = "LED1";
const char* password = "wifiLED1";
const char* mqtt_server = "185.39.142.44";
char etat = '0';
const char* id = "toto";
const char* pswd = "toto";
const int buttonPin = 16;
boolean buttonState = 0;         // current state of the button
boolean lastButtonState = 0;
WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
int value = 0;

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
  etat = (char)payload[0];
  // Switch off the LED if 0 is received
  if (etat == '0') {
    digitalWrite(2, LOW); 
  } else if (etat == '1'){ // Else turn the LED on
    digitalWrite(2, HIGH);  
  }

}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str(), id, pswd)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("LED2", "connected");
      // ... and resubscribe
      client.subscribe("LED2");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void check() {
      if (etat == '1') {
      client.publish("LED2", "1");
      } else {
        client.publish("LED2", "0");
      }
}

void setup() {
  pinMode(2, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
  if (digitalRead(buttonPin) == HIGH){
    if (etat == '0') {
    digitalWrite(2, HIGH);
    etat = '1';
    } else {
    digitalWrite(2, LOW);
    etat = '0';
    }
    delay(300);
  unsigned long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    ++value;
    check();
  
    //snprintf (msg, MSG_BUFFER_SIZE, "test", value);
    //Serial.print("Publish message: ");
    //Serial.println(msg);
    //client.publish("LED1", msg);
  }
  }
}
