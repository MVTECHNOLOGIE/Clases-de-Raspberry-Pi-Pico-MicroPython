#Importamos la librerias.
from machine import Pin
import time

LED = Pin(15,Pin.OUT)   #Declaramos como salida el pin 15 almacenándolo en la variable "LED". 
LED2 = Pin(25,Pin.OUT)  #Declaramos como salida el pin 25 almacenándolo en la variable "LED2".
LED3 = Pin(14,Pin.OUT)  #Declaramos como salida el pin 14 almacenándolo en la variable "LED3".

PULSADOR = Pin(16,Pin.IN ,Pin.PULL_DOWN) #Declaramos como salida el pin 16 almacenándolo en la
                                         #variable "Pulsador" y activando la resistencia interna para Pull-Down.
PULSADOR2 = Pin(17 ,Pin.IN) #Declaramos como salida el pin 16 almacenándolo en la variable "Pulsador2".

while True: #Iniciamos bucle infinito
    
    if PULSADOR.value() == 1:  #Si el pulso enviado del pulsador1 es alto "High".
        LED.value(1)           #Encendera el LED.
        print("Led Rojo Encendido") #Imprimiendo "Led Rojo Encendido".
        time.sleep(0.2)             #Le damos un tiempo de 200ms para evitar rebote.
    else :                     #Si el pulso no esta en alto "High".
        LED.value(0)           #Entonces se Apagara el LED.
        
    if PULSADOR2.value() == 1:  #Si el pulso enviado del pulsador 2 es alto "High".
        LED2.value(0)           #Encendera el LED.
        print("Led Verde Apagado") #Imprimiendo "Led Rojo Encendido".
        time.sleep(0.2)              #Le damos un tiempo de 200ms para evitar rebote.
    else :                     #Si el pulso no esta en alto "High".
        LED2.value(1)          #Entonces se Encendera el LED.
        
    if PULSADOR.value() == 1 and PULSADOR2.value() == 1: #Si el pulso enviado del pulsador 1 y 2 es alto "High".
        LED3.value(0)         #Encendera el LED.
        print("Led Azul Apagado")  #Imprimiendo "Led Azul Apagado".
        time.sleep(0.2)        #Le damos un tiempo de 200ms para evitar rebote.
    else :                    #Si ambos pulso no estan en alto "High".
        LED3.value(1)        #Entonces se Encendera el LED.
        