#include " Softwareserial.h"  
softwareSerial serial.connection(10, 11);#  
define BUFFER_SIZE 64  
char inData[BUFFER_SIZE];  
char inchar = -1;  
int count = 0;  
int i = 0;  
void setup()  
{  
    serial.begin(9600);  
    serial_connection.begin(9600);  
    serial_connection.println("Ready!!!");  
    serial_println("Started");  
}  
Void loop()  
{  
    byte byte = Count = serial_connection.available();  
    if (byte_ Count) {  
        Serial println("Incoming Data");  
        Int first_bytes = bytes - Count;  
        int remaining_bytes = 0;  
        if (first_bytes > +BUFFER_SIZE - 1)  
        {  
            remaining_bytes = bytes_count = (BUFFER_SIZE - 1);  
        }  
        for (i = 0; i < first_byte; i++)  
        {  
            intchar = Serial_connection.read();  
            int Data[i] = inchar;  
        }  
        intData[i] = '\0';  
        if (string(inData) == "BOOP 2")  
        {  
            Serial.println("************* start Motor ********************");  
        }  
        elseif(string(inData) == "BOOP 4")  
        {  
            Serial.println("************* stop Motor ********************");  
        }  
        for (i = 0; i < remaining_bytes; i++)  
        {  
            inchar = Serial_connection.read();  
        }  
        Serial_ConnectionPrintln("Hello From Blue" + string(count));  
        Count++;  
    }  
    delay(100)  