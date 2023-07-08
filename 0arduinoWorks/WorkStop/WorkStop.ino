#include <WiFiNINA.h>

char ssid[] = "netwoq";        // your network SSID (name)
char password[] = "netwoqpass"; 

WiFiServer server(80);  // Set the port for the server

int ledPin = LED_BUILTIN;  // Pin connected to the LED
bool isBlinking = false;   // Flag to track blinking status

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

        if (request.indexOf("/start") != -1) {
          isBlinking = true;  // Start blinking
        } else if (request.indexOf("/stop") != -1) {
          isBlinking = false; // Stop blinking
          digitalWrite(ledPin, LOW); // Turn off LED
        }

        client.println("HTTP/1.1 200 OK");
        client.println("Content-Type: text/html");
        client.println("");
        client.println("<html><body>");
        client.println("<h1>LED Control</h1>");
        client.println("<p>Click <a href=\"/start\">here</a> to start blinking the LED.</p>");
        client.println("<p>Click <a href=\"/stop\">here</a> to stop blinking the LED.</p>");
        client.println("</body></html>");

        delay(100);
        break;
      }
    }

    client.stop();  // Close the connection
    Serial.println("Client disconnected");
  }

  // Blinking logic
  if (isBlinking) {
    digitalWrite(ledPin, HIGH);  // Turn on LED
    delay(500);
    digitalWrite(ledPin, LOW);   // Turn off LED
    delay(500);
  }
}
