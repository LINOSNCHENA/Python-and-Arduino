#include <WiFiNINA.h>

char ss1id[] = "YourWiFiNetwork";      // Replace with your network name (SSID)
char pas1sword[] = "YourWiFiPassword";  // Replace with your network password

char ssid[] = "netwoq";        // your network SSID (name)
char password[] = "netwoqpass"; 

WiFiServer server(80);  // Set the port for the server

bool state = false;  // Initial state is off

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

    String request = client.readStringUntil('\r');  // Read the request from the client
    Serial.println(request);

    // Handle different request paths
    if (request.indexOf("/on") != -1) {
      state = true;
    } else if (request.indexOf("/off") != -1) {
      state = false;
    }

    // Send a response to the client
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("");
    client.println("<html><body>");
    client.println("<h1>Arduino WiFi Server</h1>");

    // Display current state
    client.print("Current state: ");
    client.println(state ? "ON" : "OFF");

    // Display buttons to change state
    client.println("<br/><a href=\"/on\"><button>Switch ON</button></a>");
    client.println("<a href=\"/off\"><button>Switch OFF</button></a>");

    client.println("</body></html>");

    delay(100);
    client.stop();  // Close the connection
    Serial.println("Client disconnected");
  }
}
