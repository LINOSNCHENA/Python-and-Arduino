#include <Arduino_LSM6DS3.h>
#include <WiFiNINA.h>

//char ssid[] = "YourWiFiNetwork";      // Replace with your network name (SSID)
//char 1password[] = "YourWiFiPassword";  // Replace with your network password

char ssid[] = "netwoq";        // your network SSID (name)
char password[] = "netwoqpass"; 

WiFiServer server(80);  // Set the port for the server

void setup() {
  Serial.begin(9600);

  if (!IMU.begin()) {
    Serial.println("Failed to initialize LSM6DS3 sensor.");
    while (1);
  }

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

    // Read accelerometer and gyroscope data
    float accelX;// = IMU.accelerationX();
    float accelY;// = IMU.accelerationY();
    float accelZ;// = IMU.accelerationZ();
  //float x, y, z;
       IMU.readAcceleration(accelX,accelY,accelZ);
    float gyroX;// = IMU.readGyroX();
    float gyroY;// = IMU.readGyroY();
    float gyroZ;// = IMU.readGyroZ();
     IMU.readGyroscope(gyroX,gyroY,gyroZ);

    // Send the data to the client
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html");
    client.println("");
    client.println("<html><body>");
    client.println("<h1>IMU Data</h1>");
    client.print("<p>Acceleration (m/s^2): X=");
    client.print(accelX);
    client.print(" Y=");
    client.print(accelY);
    client.print(" Z=");
    client.println(accelZ);
    client.print("Gyroscope (dps): X=");
    client.print(gyroX);
    client.print(" Y=");
    client.print(gyroY);
    client.print(" Z=");
    client.println(gyroZ);
    client.println("</p></body></html>");

    delay(100);
    client.stop();  // Close the connection
    Serial.println("Client disconnected");
  }
}
