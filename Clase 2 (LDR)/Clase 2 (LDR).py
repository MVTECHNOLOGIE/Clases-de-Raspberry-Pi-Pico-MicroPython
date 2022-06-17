from machine import Pin   #importar librerias
import time               

ldr = machine.ADC(26)     #Seleccionamos el pin 26 ADC "pin analógico"
led = Pin(25,Pin.OUT)     #Seleccionamos el LED de la placa Pi Pico que corresponde al pin 25

while True:               #Se utiliza para especificar un bucle infinito 
    
     valor = ldr.read_u16()        # La variable "valor" es igual al voltaje lee, con una precisión de 16 bits
     print("Valor LDR: " , valor)  # Imprimimos las variables, en este caso es "valor
     
     # Los valores variaran entre "0 y 65535"
     
     luz = round(valor/65535*100)     #Dado que el resultado de la lectura de 16 bits estará entre 0 y 65535, el
                                      #valor de la luz se convertirá en un porcentaje y
                                      #finalmente se devolverá como el resultado de la función.
    
     print("Luz Solar: ",luz,"%")     # Imprimimos las variables, en este caso es "luz"
                                      
     time.sleep(1)                    #Tiempo de espera


        
        