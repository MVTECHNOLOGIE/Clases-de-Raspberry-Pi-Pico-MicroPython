# Importamos las librerias necesarias
from machine import Pin
import time

# Definimos los pines que se usarán para los LEDs
pines = [Pin(i, Pin.OUT) for i in (22, 21, 20, 19, 18, 17)]
intervalo = 0.05  # intervalo de tiempo entre cada cambio de estado del LED

def secuencia_bandera(pines, intervalo):
    # Bucle infinito para repetir la secuencia
    while True:
        # Recorremos la lista de pines y encendemos cada LED
        for pin in pines:
            pin.value(1)
            time.sleep(intervalo)  # Esperamos antes de cambiar al siguiente LED
        # Recorremos la lista de pines en orden inverso y apagamos cada LED
        for pin in reversed(pines):
            pin.value(0)
            time.sleep(intervalo)  # Esperamos antes de cambiar al siguiente LED

# Ejecutamos la función
secuencia_bandera(pines, intervalo)