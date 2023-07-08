#include <WiFiNINA.h>
#include <ArduinoJson.h>

char ssid[] = "YourWiFiNetwork";      // Replace with your network name (SSID)
char password[] = "YourWiFiPassword";  // Replace with your network password

WiFiServer server(80);  // Set the port for the server

int ledPin = LED_BUILTIN;  // Pin connected to the LED

float accelX, accelY, accelZ;  // Variables to store accelerometer data

void setup() {
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);  // Set LED pin as an output
  digitalWrite(ledPin, LOW); // Start with LED off

  // Connect to Wi-Fi network
  while (WiFi.begin(ssid, password) != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  server.begin();  // Start the server
}

void loop() {
  WiFiClient client = server.available();  // Check for incoming client connections

  if (client) {  // If a client is connected
    Serial.println("New client connected");

    while (client.connected()) {
      if (client.available()) {
        String request = client.readStringUntil('\r');  // Read the request

        if (request.indexOf("/data") != -1) {
          // Create a JSON document
          StaticJsonDocument<200> jsonDoc;

          // Populate the JSON document with accelerometer data
          jsonDoc["accelX"] = accelX;
          jsonDoc["accelY"] = accelY;
          jsonDoc["accelZ"] = accelZ;

          // Serialize the JSON document to a string
          String jsonData;
          serializeJson(jsonDoc, jsonData);

          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: application/json");
          client.println("");
          client.println(jsonData);
        }

        client.println("HTTP/1.1 200 OK");
        client.println("Content-Type: text/html");
        client.println("");
        client.println("<html><body>");
        client.println("<h1>Accelerometer Data</h1>");
        client.println("<p>Click <a href=\"/data\">here</a> to get accelerometer data.</p>");
        client.println("</body></html>");

        delay(100);
        break;
      }
    }

    client.stop();  // Close the connection
    Serial.println("Client disconnected");
  }

  // Read accelerometer data
  // Replace the code below with your actual accelerometer data reading logic
  accelX = readAccelX();
  accelY = readAccelY();
  accelZ = readAccelZ();
}

float readAccelX() {
  // Implement the code to read the accelerometer X-axis data here
  // Replace the return statement with your actual implementation
  return 0.0;
}

float readAccelY() {
  // Implement the code to read the accelerometer Y-axis data here
  // Replace the return statement with your actual implementation
  return 0.0;
}

float readAccelZ() {
  // Implement the code to read the accelerometer Z-axis data here
  // Replace the return statement with your actual implementation
  return 0.0;
}
