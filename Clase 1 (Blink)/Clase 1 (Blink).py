#M&V_TECHNOLOGIE

#Clase N°1 Parpadeo "Blink"

# Importamos las siguentes librerias
#Machine: es un módulo específico de MicroPython que contiene funciones y clases que permiten obtener acceso directo y
#sin restricciones sobre el hardware del microcontrolador (CPU, pines, temporizadores, ADC,  buses –UART, SPI, I2C, etc.).

# Time: es una librería estándar de MicroPython proporciona un conjunto de funciones para indicar el tiempo que el microcontrolador
#lleva encendido, medir intervalos de tiempo e introducir retardos (esperas) en la ejecución de los programas

from machine import Pin
import time

# Declarar variables para los pines

LED = Pin(14, Pin.OUT)     #Declaramos que la variable "LED" Perteneciente al pin 25 y quedara como salida "OUTPUT"

while True:                #Declaramos el bucle infinito

    LED.value(1)           #Indicamos que el pin 25 deberá estar en alto "HIGH" o "1" 
    time.sleep(0.5)        #Colocamos un tiempo de espera de 500 milisegundos, es decir medio segundo
    LED.value(0)           #Indicamos que el pin 25 deberá estar en bajo "LOW" o "0"
    time.sleep(0.5)        #Colocamos un tiempo de espera de 500 milisegundos, es decir medio segundo