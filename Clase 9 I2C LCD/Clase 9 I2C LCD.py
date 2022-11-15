import utime
from machine import I2C,Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#Dirección del I2C y tamaño del LCD
I2C_ADDR  =  0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Raspberry Pi Pico
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

#Configuración LCD
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def lcd_str(message, col, row):
    lcd.move_to(col, row) # Mover a la posición según los valores de fila y col (Y, X)
    lcd.putstr(message) #Envía una cadena de caracteres a la pantalla. IMPORTANTE: para
    #imprimir una variable puedes usar la siguiente instrucción: lcd.putstr (str (Variable))
    
while True:
    
    lcd.blink_cursor_on()  # El cursor parpadeante al imprimir
    lcd_str("Suscribete a", 2,0)
    lcd_str("M&V TECHNOLOGIE", 0,1)
    utime.sleep(2)
    lcd.clear()
    lcd_str("I2C Address:"+str(hex(I2C_ADDR)),0,0)
    lcd_str("M&V TECHNOLOGIE",0,1)
    utime.sleep(2)         
    lcd.blink_cursor_off()  # Apaga el cursor parpadeante al imprimir
    lcd.clear()
    