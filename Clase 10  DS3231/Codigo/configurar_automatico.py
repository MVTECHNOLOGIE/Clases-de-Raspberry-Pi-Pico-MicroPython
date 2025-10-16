from ds3231 import RelojRTC
import utime

# 1. Crear el objeto del reloj.
# Con esto, le decimos a la Pi Pico que se prepare para hablar con el módulo RTC.
reloj = RelojRTC(sda_pin=0, scl_pin=1)

# 2. Sincronizar la hora automáticamente.
# Esta función lee la hora de tu computadora y la guarda en el reloj del módulo.
# ¡Importante! Después de la primera vez, comenten esta línea para que no se
# sobrescriba la hora del reloj cada vez que lo enciendan.
reloj.sync_from_pc()

# 3. Configurar el formato.
# Aquí pueden elegir si quieren la hora en formato de 12 o 24 horas.
# Para 12 horas, usen `False`. Para 24, usen `True`.
reloj.set_time_format(hour_format_24=False)

# 4. Mostrar la hora configurada.
# Finalmente, usamos las funciones de la librería para confirmar que la configuración
# fue exitosa.

reloj.print_time()
reloj.print_date()

