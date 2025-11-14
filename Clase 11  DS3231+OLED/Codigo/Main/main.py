# main.py - Reloj DS3231 + OLED SSD1306 en Raspberry Pi Pico
# Muestra hora, fecha y temperatura en pantalla OLED con reloj DS3231.

import machine       # Controla pines y periféricos del microcontrolador.
import utime         # Permite usar funciones de tiempo (pausas, reloj interno).
from ssd1306 import SSD1306_I2C   # Librería para manejar pantalla OLED por I2C.
import ds3231        # Librería para comunicarse con el reloj DS3231.

# --- CONFIGURACIÓN I2C ---
I2C_BUS = 0          # Canal I2C que se usará (0 o 1 en la Raspberry Pi Pico).
SDA_PIN = 0          # Pin para datos I2C (SDA).
SCL_PIN = 1          # Pin para reloj I2C (SCL).
OLED_WIDTH = 128     # Ancho de la pantalla OLED en píxeles.
OLED_HEIGHT = 64     # Alto de la pantalla OLED en píxeles.

# Inicializar bus I2C
try:
    i2c = machine.I2C(
        I2C_BUS,
        sda=machine.Pin(SDA_PIN),
        scl=machine.Pin(SCL_PIN),
        freq=400000      # Velocidad de comunicación (400kHz).
    )
    print("Bus I2C inicializado:", i2c.scan())  # Muestra los dispositivos conectados.
except Exception as e:
    print("Error al inicializar I2C:", e)
    while True:          # Si falla, queda detenido mostrando el error.
        utime.sleep(1)

# Inicializar pantalla OLED
try:
    oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)  # Crea el objeto OLED.
    oled.fill(0)            # Limpia la pantalla.
    oled.show()             # Actualiza la pantalla.
    print("OLED lista.")
except Exception as e:
    print("Error OLED:", e)
    oled = None             # Si falla, no se usa OLED.

# Inicializar reloj DS3231
try:
    rtc = ds3231.DS3231(i2c_bus=I2C_BUS, scl_pin=SCL_PIN, sda_pin=SDA_PIN)
    print("RTC DS3231 inicializado.")
except Exception as e:
    print("Error RTC:", e)
    while True:             # Si falla el RTC, detiene el programa.
        utime.sleep(1)


# --- FUNCIÓN PRINCIPAL ---
def actualizar_pantalla(rtc_obj, oled_obj):
    datos = rtc_obj.obtener_hora()        # Lee la hora y fecha del RTC.
    temp = rtc_obj.obtener_temperatura()  # Lee la temperatura del sensor DS3231.

    if not datos or temp is None:         # Si falla la lectura:
        oled_obj.fill(0)
        oled_obj.text("Error RTC", 0, 0)
        oled_obj.show()
        return

    # Formato de hora con dos puntos fijos
    hora = f"{datos['hora']:02d}:{datos['minuto']:02d}:{datos['segundo']:02d}"

    # Formato de fecha abreviada
    fecha = f"{datos['dia_semana_texto']}, {datos['dia_mes']:02d}/{datos['mes']:02d}/{str(datos['año'])[-2:]}"
    temperatura = f"{temp:.1f}C"  # Formato temperatura con un decimal

    oled_obj.fill(0)  # Limpia pantalla antes de dibujar nuevos datos.

    # --- Fecha en la parte superior ---
    oled_obj.text(fecha, 0, 0)

    # --- Hora centrada ---
    ancho_hora = len(hora) * 8                # Calcula ancho aproximado del texto.
    x_inicio = (OLED_WIDTH - ancho_hora) // 2 # Centra horizontalmente.
    y_inicio = 22                             # Posición vertical de la hora.
    oled_obj.text(hora, x_inicio, y_inicio)

    # --- Temperatura abajo ---
    oled_obj.text("Temp:", 0, 50)
    oled_obj.text(temperatura, 45, 50)

    oled_obj.show()  # Muestra todo en la pantalla.

    print(f"Hora: {hora} | Fecha: {fecha} | Temp: {temperatura}")  # También lo muestra por consola.


# --- BUCLE PRINCIPAL ---
print("\n--- Iniciando reloj OLED ---")
try:
    while True:
        actualizar_pantalla(rtc, oled)  # Actualiza cada segundo.
        utime.sleep(1)
except KeyboardInterrupt:
    print("Programa detenido.")
    oled.fill(0)
    oled.show()
