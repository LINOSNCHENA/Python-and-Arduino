// data collection source file IMUCollect.ino

#include <Arduino_LSM9DS1.h>


void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println("Hz");
}

void loop() {
  float ax, ay, az, gx, gy, gz;

  if (!IMU.accelerationAvailable() || !IMU.gyroscopeAvailable())
    return;

  IMU.readAcceleration(ax, ay, az);
  IMU.readGyroscope(gx, gy, gz);

  // Serial.print("IMU: ");
  // Serial.print(",");
  Serial.print(ax);//1
  Serial.print(",");
  Serial.print(ay);//2
  Serial.print(",");
  Serial.print(az);//3
  Serial.print(",");
  Serial.print(gx);//4
  Serial.print(",");
  Serial.print(gy);//5
  Serial.print(",");
  Serial.print(gz);//6
  Serial.print("\n");
  delay(1000); // Two Seconds
}
