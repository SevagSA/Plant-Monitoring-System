#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <SPI.h>
#include <MFRC522.h>

const char* ssid = "BELL126";
const char* password = "2EE4A4EA";


const char* mqtt_server = "broker.emqx.io";
#define D3 0
#define D4 2
constexpr uint8_t RST_PIN = D3;     // Configurable, see typical pin layout above
constexpr uint8_t SS_PIN = D4;     // Configurable, see typical pin layout above

MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class
MFRC522::MIFARE_Key key;


WiFiClient vanieriot;
PubSubClient client(vanieriot);


void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("WiFi connected - ESP-8266 IP address: ");
  Serial.println(WiFi.localIP());
}


void callback(String topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.print(topic);
  Serial.print(". Message: ");
  String messagein;
  
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
    messagein += (char)message[i];
  }

  if(topic=="room/light"){
    if (messagein == "ON") 
      Serial.println("Light is ON");
  }else{
          Serial.println("Light is OFF");

  }
  
}


void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
 
    
   //  String clientId = "ESP8266Client-";
   // clientId += String(random(0xffff), HEX);
    // Attempt to connect
   // if (client.connect(clientId.c_str())) {
           if (client.connect("vanieriot")) {

      Serial.println("connected");  
      client.subscribe("room/light");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}


String tag;
void setup() {
  
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init MFRC522
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  if(!client.loop())
    client.connect("vanieriot");
     int sensorValue = analogRead(A0);
     String value = String(sensorValue);
     char light_array[30];
     value.toCharArray(light_array,value.length()+1);
     client.publish("iot/photoresistor/team3", light_array);

    if ( ! rfid.PICC_IsNewCardPresent())
    return;
  if (rfid.PICC_ReadCardSerial()) {
    for (byte i = 0; i < 4; i++) {
      tag += rfid.uid.uidByte[i];
    }
    Serial.println(tag);
    int str_len = tag.length()+1;
    char tag_array[str_len];
    tag.toCharArray(tag_array, str_len);
    client.publish("iot/rfid/team3", tag_array);
    tag = "";
    rfid.PICC_HaltA();
    rfid.PCD_StopCrypto1();
  }


  }
