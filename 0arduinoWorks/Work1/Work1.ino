#include <WiFiNINA.h>

//char sXsid[] = "YourWiFiNetwork";      // Replace with your network name (SSID)
// char paXssword[] = "YourWiFiPassword";  // Replace with your network password

char ssid[] = "netwoq";        // your network SSID (name)
char password[] = "netwoqpass"; 


WiFiServer server(80);  // Set the port for the server
bool buttonState = false;  // Initial button state

void setup() {
  Serial.begin(9600);

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

    // Read the request from the client
    String request = client.readStringUntil('\r');
    Serial.println(request);

    if (request.indexOf("/off") != -1) {
      // Switch off the button
      buttonState = false;
      Serial.println("Button OFF");
    }

    // Send a response to the client
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("");
    client.println("<html><body>");
    client.println("<h1>Button State: " + String(buttonState) + "</h1>");
    client.println("<a href=\"/off\">Switch Off</a>");
    client.println("</body></html>");

    delay(100);
    client.stop();  // Close the connection
    Serial.println("Client disconnected");
  }
}
