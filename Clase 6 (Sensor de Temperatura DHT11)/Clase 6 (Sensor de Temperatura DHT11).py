#Declaramos libreras
import dht #Incluida en el Firmware
from machine import Pin 
import time 

Sensor = dht.DHT11(Pin(15)) 

led = Pin(14,Pin.OUT)

while True:
    
    Sensor.measure()
    temp = Sensor.temperature()
    hum = Sensor.humidity()
    time.sleep(1)  # Son 5 segundos
    
    print(f"Temperatura: {temp}°C Humedad: {hum}%")
    
    if temp > 30:
        led.value(1)
    else:
        led.value(0)