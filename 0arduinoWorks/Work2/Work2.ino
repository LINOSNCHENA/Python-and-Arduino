#include <WiFiNINA.h>

// char ssid[] = "YourWiFiNetwork";      // Replace with your network name (SSID)
// char password[] = "YourWiFiPassword";  // Replace with your network password

char ssid[] = "netwoq";        // your network SSID (name)
char password[] = "netwoqpass"; 

WiFiServer server(80);  // Set the port for the server

int buttonPin = 2;      // Pin number for the button
int ledPin = 13;        // Pin number for the LED

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  
  Serial.begin(9600);
  
  // Connect to Wi-Fi network
  while (WiFi.begin(ssid, password) != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  
  server.begin();  // Start the server
}

void loop() {
  WiFiClient client = server.available();  // Check for incoming client connections

  if (client) {  // If a client is connected
    Serial.println("New client connected");

    // Read the request from the client
    String request = client.readStringUntil('\r');
    Serial.println(request);

    if (request.indexOf("/on") != -1) {
      digitalWrite(ledPin, HIGH);  // Turn on the LED
    }
    else if (request.indexOf("/off") != -1) {
      digitalWrite(ledPin, LOW);   // Turn off the LED
    }

    // Send a response to the client
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("");
    client.println("<html><body>");
    client.println("<h1>Arduino WiFi Button Control</h1>");
    client.println("<p><a href=\"/on\">Switch On</a></p>");
    client.println("<p><a href=\"/off\">Switch Off</a></p>");
    client.println("</body></html>");

    delay(100);
    client.stop();  // Close the connection
    Serial.println("Client disconnected");
  }
}
