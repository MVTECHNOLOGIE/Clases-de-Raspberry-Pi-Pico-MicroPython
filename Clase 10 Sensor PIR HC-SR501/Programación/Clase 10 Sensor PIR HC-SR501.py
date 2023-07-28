import machine
import utime

pir_pin = machine.Pin(1, machine.Pin.IN)  # Pin digital al que está conectado el sensor PIR
led_pin = machine.Pin(4, machine.Pin.OUT)  # Pin digital al que está conectado el LED

while True:
    if pir_pin.value() == 1:  # Si se detecta movimiento (valor 1 es equivalente a HIGH)
        led_pin.value(1)  # Encender el LED
        utime.sleep(1)  # Esperar un segundo
    else:
        led_pin.value(0)  # Apagar el LED
