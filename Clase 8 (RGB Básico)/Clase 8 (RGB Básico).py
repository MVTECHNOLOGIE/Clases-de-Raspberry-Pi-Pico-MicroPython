#M&V_TECHNOLOGIE

#Clase N°8 RGB "Básico"

# Importamos las siguentes librerias
#Machine: es un módulo específico de MicroPython que contiene funciones y clases que permiten obtener acceso directo y
#sin restricciones sobre el hardware del microcontrolador (CPU, pines, temporizadores, ADC,  buses –UART, SPI, I2C, etc.).

# Time: es una librería estándar de MicroPython proporciona un conjunto de funciones para indicar el tiempo que el microcontrolador
#lleva encendido, medir intervalos de tiempo e introducir retardos (esperas) en la ejecución de los programas

from machine import Pin
import time

# Declarar variables para los pines
Rojo  = Pin(15, Pin.OUT)     #Declaramos que la variable "Rojo " Perteneciente al pin 15 y quedara como salida "OUTPUT"
Verde = Pin(14, Pin.OUT)     #Declaramos que la variable "Verde" Perteneciente al pin 14 y quedara como salida "OUTPUT"
Azul  = Pin(13, Pin.OUT)     #Declaramos que la variable "Azul" Perteneciente al pin 13 y quedara como salida "OUTPUT"

while True:               #Declaramos el bucle infinito
    Rojo.value(1)         #Indicamos que el pin 15 deberá estar en alto "HIGH" o "1"
    Verde.value(0)        #Indicamos que el pin 14 deberá estar en bajo "LOW" o "0"
    Azul.value(0)         #Indicamos que el pin 13 deberá estar en bajo "LOW" o "0"
    
    time.sleep(0.5)       #Colocamos un tiempo de espera de 500 milisegundos, es decir medio segundo
    
    Rojo.value(0)         #Indicamos que el pin 15 deberá estar en bajo "LOW" o "0"
    Verde.value(1)        #Indicamos que el pin 14 deberá estar en alto "HIGH" o "1"
    Azul.value(0)         #Indicamos que el pin 13 deberá estar en bajo "LOW" o "0"
    
    time.sleep(0.5)       #Colocamos un tiempo de espera de 500 milisegundos, es decir medio segundo
    
    Rojo.value(0)         #Indicamos que el pin 15 deberá estar en bajo "LOW" o "0"
    Verde.value(0)        #Indicamos que el pin 14 deberá estar en bajo "LOW" o "0"
    Azul.value(1)         #Indicamos que el pin 13 deberá estar en alto "HIGH" o "1"
    
    time.sleep(0.5)       #Colocamos un tiempo de espera de 500 milisegundos, es decir medio segundo
    
    
    
    