from ds3231 import RelojRTC

# 1. Crear el objeto del reloj.
# Con esto, la Pi Pico se prepara para comunicarse con el módulo.
reloj = RelojRTC(sda_pin=0, scl_pin=1)

# 2. Configurar el formato de la hora.
# Decidan si quieren que el reloj funcione en 12 o 24 horas.
# Para 12 horas: False; Para 24 horas: True.
reloj.set_time_format(hour_format_24=False)

# 3. Sincronizar la hora manualmente.
# Usen esta función para establecer una hora y fecha específicas.
# Por ejemplo, aquí configuramos el reloj a las 10:30:00 AM del 15 de enero de 2025.
# `segundo=0`
# `minuto=30`
# `hora=10` (Recuerden que es en formato de 24 horas para la configuración)
# `dia=15`
# `mes=1`
# `año=2025`
# `dia_semana=4` (1=Domingo, 2=Lunes, ..., 7=Sábado. Un 4 sería Miércoles)
#
# NOTA: En la librería, la hora para la configuración manual siempre se debe
# dar en formato de 24 horas.
reloj.set_time_manual(
    segundo=0,
    minuto=30,
    hora=10, 
    dia=15,
    mes=1,
    año=2025,
    dia_semana=4
)

# 4. Mostrar la hora configurada.
# Por último, imprimimos la hora, fecha y temperatura para confirmar que los datos se guardaron correctamente.

reloj.print_time()
reloj.print_date()
reloj.print_temperature()
