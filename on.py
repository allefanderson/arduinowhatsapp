import serial
import time

ser = serial.Serial('COM3', 9600)

def led_on_off():
   
        print("LED is on...")
        time.sleep(0.1) 
        ser.write(b'H') 
        
time.sleep(2) # Aguarde para que se inicialize a conexão com a serial.

led_on_off()
