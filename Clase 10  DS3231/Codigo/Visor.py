from ds3231 import RelojRTC
import utime

# 1. Crear el objeto del reloj.
# Esta es la línea que "activa" la comunicación con el módulo RTC.
reloj = RelojRTC(sda_pin=0, scl_pin=1)

# 2. Configurar el formato de la hora.
# Puedes elegir entre 24 o 12 horas. Solo descomenta la línea que quieras usar.
reloj.set_time_format(hour_format_24=False)
# reloj.set_time_format(hour_format_24=False)



# 3. Iniciar el bucle de actualización.
# Este bucle leerá y mostrará los datos del reloj una y otra vez.
while True:
    # `reloj.print_time()` muestra la hora.
    reloj.print_time()

    # `reloj.print_date()` muestra la fecha.
    reloj.print_date()

    # `reloj.print_temperature()` muestra la temperatura.
    reloj.print_temperature()
    
    # Una línea para que las actualizaciones se vean más ordenadas en la consola.
    print("-" * 25)

    # El programa se detiene por 1 segundo antes de la siguiente lectura.
    utime.sleep(1)