#M&V_TECHNOLOGIE

#Clase N°8.2 RGB "Básico"

# Importamos las siguentes librerias
#Machine: es un módulo específico de MicroPython que contiene funciones y clases que permiten obtener acceso directo y
#sin restricciones sobre el hardware del microcontrolador (CPU, pines, temporizadores, ADC,  buses –UART, SPI, I2C, etc.).

# Time: es una librería estándar de MicroPython proporciona un conjunto de funciones para indicar el tiempo que el microcontrolador
#lleva encendido, medir intervalos de tiempo e introducir retardos (esperas) en la ejecución de los programas

from machine import Pin, PWM
import time
import random

# Declarar variables para los pines
Rojo  = PWM(Pin(15))     #Declaramos que la variable "Rojo " Perteneciente al pin 15 y quedara como salida "OUTPUT"
Verde = PWM(Pin(14))     #Declaramos que la variable "Verde" Perteneciente al pin 14 y quedara como salida "OUTPUT"
Azul  = PWM(Pin(13))     #Declaramos que la variable "Azul"  Perteneciente al pin 13 y quedara como salida "OUTPUT"

Rojo.freq(5000)   
Verde.freq(5000)   
Azul.freq(5000)

def colour(G,B,R):
        Rojo.duty_u16  (R*257)      
        Verde.duty_u16 (G*257)
        Azul.duty_u16  (B*257)
        
while True:  #Declaramos el bucle infinito
    
     colour(random.randrange(255),random.randrange(255),random.randrange(255))  #Verde
     time.sleep(0.4)   #Colocamos un tiempo de espera de 1 segundo