from machine import Pin, ADC, PWM     #Importamos librerías   
import time                                

LED = PWM(Pin(15))     # Declaramos el pin 15 como PWM
LED.freq(1000)     # 1000Hz

POT = ADC(26)     #Declaramos la variable para la lectura analógica pin 26

while True: #Bucle infinito
    
  Valor = POT.read_u16()      # Almacenamos los valores leídos de nuestro potenciómetro en la variable "Valor"
                              #que serán de 0 a 65535
  
  porcentaje = round(Valor/65535*100) #Redondeamos los valores de 0 a 100
  
  print("Valor de 0 a 100:" ,porcentaje,"%") # Imprimimos los valores almacenados en la variable "porcentaje"
  
  
  LED.duty_u16(Valor)         # Establesemos el valor del ciclo de trabajo como el del valor del potenciómetro
  
  time.sleep(0.25)            # Le damos un diempo de 250ms