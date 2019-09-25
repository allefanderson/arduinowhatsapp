import serial
import time

ser = serial.Serial('COM3', 9600)

def led_on_off():
   
        print("LED is off...")
        time.sleep(0.1)
        ser.write(b'L')
        
led_on_off()
