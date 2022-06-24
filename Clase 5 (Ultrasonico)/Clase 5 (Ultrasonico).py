# Importamos libreria
from machine import Pin
import time

TRIGGER = Pin(14,Pin.OUT)  # Declaramos el pin 14 como salida y lo almacenamos en la variable TRIGGER
ECHO = Pin(15, Pin.IN)     # Declaramos el pin 14 como salida y lo almacenamos en la variable TRIGGER
distancia = 0              # Declaramos que la variable distancia tenga un valor de 0

while True:                # Iniciamos el bucle infinito

    TRIGGER.high()         # TRIGGER pasa a valor alto // TRIGGER.value(1)
    time.sleep(0.00001)    # le damos un tiempo de 10 Micosegundos //time.sleep_us(10)
    TRIGGER.low()          # TRIGGER pasa a valor bajo // TRIGGER.value(0)
    
    while ECHO.value() == 0:          
        comienzo = time.ticks_us() # Medimos el tiempo en que la señal tarda en ir 
    while ECHO.value() ==1:
        final = time.ticks_us()    # Medimos el tiempo en que la señal tarda en volver
    
    duracion = final - comienzo    # Calculamos la duración 
    distancia = (duracion * 0.0343) / 2 # Calculamos la distancia multiplicando la velocidad del sonido y dividiéndola por 2 para así poder tomar la distancia del objeto
    print("Distancia:",distancia,"cm") # Imprimimos la variable distancia 
    time.sleep(1)  #le damos un tiempo de 1 Segundo