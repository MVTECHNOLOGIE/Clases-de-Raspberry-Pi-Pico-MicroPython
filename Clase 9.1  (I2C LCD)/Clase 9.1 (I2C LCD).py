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

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

feliz = [0x00,
  0x00,
  0x0A,
  0x00,
  0x11,
  0x0E,
  0x00,
  0x00]
triste = [0x00,
  0x00,
  0x0A,
  0x00,
  0x00,
  0x0E,
  0x11,
  0x00]
serio = [0x00,
  0x00,
  0x0A,
  0x00,
  0x00,
  0x1F,
  0x00,
  0x00]
corazon = [0x00,
  0x00,
  0x0A,
  0x1F,
  0x1F,
  0x0E,
  0x04,
  0x00]
humano = [0x0E,
  0x0E,
  0x0E,
  0x04,
  0x1F,
  0x04,
  0x0E,
  0x11]
bateria = [0x0E,
  0x11,
  0x11,
  0x13,
  0x17,
  0x1F,
  0x1F,
  0x1F]
Bocina = [0x02,
  0x06,
  0x1E,
  0x1E,
  0x1E,
  0x1E,
  0x06,
  0x02]
pulso = [0x01,
  0x05,
  0x15,
  0x15,
  0x15,
  0x15,
  0x05,
  0x01]

def lcd_str(message, col, row):
    lcd.move_to(col, row) # Mover a la posición según los valores de fila y col (Y, X)
    lcd.putstr(message) #Envía una cadena de caracteres a la pantalla. IMPORTANTE: para
    #imprimir una variable puedes usar la siguiente instrucción: lcd.putstr (str (Variable))
def main():
    lcd.custom_char(0, bytearray(feliz))
    lcd.custom_char(1, bytearray(triste))
    lcd.custom_char(2, bytearray(serio))
    lcd.custom_char(3, bytearray(corazon))
    lcd.custom_char(4, bytearray(humano))
    lcd.custom_char(5, bytearray(bateria))
    lcd.custom_char(6, bytearray(Bocina))
    lcd.custom_char(7, bytearray(pulso))
    #lcd.custom_char(Num, bytearray ([caracteres HEX]))) –
    #Num puede ser cualquier número entero 0 – 8 (escribiendo en ubicaciones CGRAM)
    #simplemente utilizado para numerar. Los caracteres HEX se crean simplemente usando
    #este enlace: https://maxpromer.github.io/LCD-Character-Creator/ . 
    
    while True:

        lcd.clear()
        lcd_str("Caracteres", 3, 0)
        lcd.move_to(1,1)
        lcd.putchar (chr(0))
        lcd.move_to(3,1)
        lcd.putchar (chr(1))
        lcd.move_to(5,1)
        lcd.putchar (chr(2))
        lcd.move_to(7,1)
        lcd.putchar (chr(3))
        lcd.move_to(9,1)
        lcd.putchar (chr(4))
        lcd.move_to(11,1)
        lcd.putchar (chr(5))
        lcd.move_to(13,1)
        lcd.putchar (chr(6))
        lcd.putchar (chr(7))
        utime.sleep(3)
        lcd.clear()
    
        lcd.blink_cursor_on()  # El cursor parpadeante al imprimir
        lcd_str("Suscribete a", 2,0)
        lcd_str("M&V TECHNOLOGIE", 0,1)
        utime.sleep(3)
        lcd.clear()
        lcd_str("I2C Address:"+str(hex(I2C_ADDR)),0,0)
        lcd_str("M&V TECHNOLOGIE",0,1)
        utime.sleep(3)         
        lcd.blink_cursor_off()  # Apaga el cursor parpadeante al imprimir
        lcd.clear()
        
        
if __name__ == '__main__':
    main()
