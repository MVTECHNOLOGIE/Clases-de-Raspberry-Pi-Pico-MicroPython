from machine import Pin,UART 
import time

uart = UART(0,9600)

led_green = Pin(12,Pin.OUT)
led_yellow  = Pin(4,Pin.OUT)
led_red = Pin(16,Pin.OUT)
led_blue = Pin(2,Pin.OUT)

while True:
    
    if uart.any(): 
        comando = uart.readline() 
        print(comando)
        
        if "c" in comando:
            led_blue.value(1)
        if "d" in comando:
            led_blue.value(0)    
        
        if "e" in comando:
            led_red.value(1)
        if "f" in comando:
            led_red.value(0)
            
        if "a" in comando:
            led_yellow.value(1)
        if "b" in comando:
            led_yellow.value(0)
            
        if "g" in comando:
            led_green.value(1)
        if "h" in comando:
            led_green.value(0)
            
            time.sleep(0.5)
            
                 
