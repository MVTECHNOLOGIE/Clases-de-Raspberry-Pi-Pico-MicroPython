import machine
import utime

class DS3231:
    """
    Libreria profesional para modulo RTC DS3231
    Version mejorada con soporte para formato 12h/24h y AM/PM corregido.
    Incluye método para devolver la hora como string.
    """
    
    def __init__(self, i2c_bus=0, scl_pin=1, sda_pin=0, i2c_freq=400000):
        try:
            self.i2c = machine.I2C(i2c_bus, 
                                 scl=machine.Pin(scl_pin), 
                                 sda=machine.Pin(sda_pin), 
                                 freq=i2c_freq)
            self.address = 0x68
            self.dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
            self.meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"]
            self.formato_24h = True  # Por defecto formato 24h
            
            dispositivos = self.i2c.scan()
            if self.address not in dispositivos:
                print(f"Advertencia: DS3231 no encontrado en 0x{self.address:02X}")
            else:
                print(f"DS3231 inicializado - Bus I2C{i2c_bus}, SCL:GPIO{scl_pin}, SDA:GPIO{sda_pin}")
                
        except Exception as e:
            print(f"Error inicializando DS3231: {e}")
            raise
    
    def _bcd_a_dec(self, bcd):
        return (bcd // 16) * 10 + (bcd % 16)
    
    def _dec_a_bcd(self, dec):
        return (dec // 10) * 16 + (dec % 10)
    
    def configurar_auto(self, formato_24h=True):
        try:
            tiempo_actual = utime.time()
            tiempo_tuple = utime.localtime(tiempo_actual)
            
            segundo = tiempo_tuple[5]
            minuto = tiempo_tuple[4]
            hora = tiempo_tuple[3]
            dia_semana = tiempo_tuple[6] + 1
            dia_mes = tiempo_tuple[2]
            mes = tiempo_tuple[1]
            año = tiempo_tuple[0] % 100
            
            self.formato_24h = formato_24h
            return self.configurar_manual(segundo, minuto, hora, dia_semana, dia_mes, mes, año, formato_24h)
            
        except Exception as e:
            print(f"Error en configuracion automatica: {e}")
            return False
    
    def configurar_manual(self, segundo, minuto, hora, dia_semana, dia_mes, mes, año, formato_24h=True):
        try:
            data = bytearray([
                self._dec_a_bcd(segundo),
                self._dec_a_bcd(minuto),
                self._dec_a_bcd(hora),
                self._dec_a_bcd(dia_semana),
                self._dec_a_bcd(dia_mes),
                self._dec_a_bcd(mes),
                self._dec_a_bcd(año)
            ])
            
            self.i2c.writeto_mem(self.address, 0x00, data)
            self.formato_24h = formato_24h
            print("Hora configurada correctamente")
            return True
            
        except Exception as e:
            print(f"Error en configuracion manual: {e}")
            return False
    
    def obtener_hora(self):
        try:
            data = self.i2c.readfrom_mem(self.address, 0x00, 7)
            
            return {
                'segundo': self._bcd_a_dec(data[0] & 0x7F),
                'minuto': self._bcd_a_dec(data[1]),
                'hora': self._bcd_a_dec(data[2] & 0x3F),
                'dia_semana': self._bcd_a_dec(data[3]),
                'dia_mes': self._bcd_a_dec(data[4]),
                'mes': self._bcd_a_dec(data[5] & 0x1F),
                'año': self._bcd_a_dec(data[6]) + 2000,
                'dia_semana_texto': self.dias_semana[self._bcd_a_dec(data[3]) - 1],
                'mes_texto': self.meses[self._bcd_a_dec(data[5] & 0x1F) - 1]
            }
            
        except Exception as e:
            print(f"Error leyendo hora: {e}")
            return None
    
    def obtener_temperatura(self):
        try:
            data = self.i2c.readfrom_mem(self.address, 0x11, 2)
            temp_raw = (data[0] << 8) | data[1]
            temp_raw = temp_raw >> 6
            
            if temp_raw & 0x200:
                temp_raw = -((temp_raw ^ 0x3FF) + 1)
                
            return temp_raw * 0.25
            
        except Exception as e:
            print(f"Error leyendo temperatura: {e}")
            return None
    
    def hora_formateada(self, mostrar_temperatura=False, formato_24h=None):
        """
        Devuelve la hora como string (para LCD, OLED, archivos, etc.)
        """
        datos = self.obtener_hora()
        if not datos:
            return "Error obteniendo hora"
        
        if formato_24h is None:
            formato_24h = self.formato_24h
        
        # Fecha
        texto = f"{datos['dia_mes']:02d}/{datos['mes']:02d}/{datos['año']} "
        
        # Hora
        if formato_24h:
            texto += f"{datos['hora']:02d}:{datos['minuto']:02d}:{datos['segundo']:02d}"
        else:
            if datos['hora'] == 0:
                hora_12h = 12
                am_pm = "AM"
            elif datos['hora'] < 12:
                hora_12h = datos['hora']
                am_pm = "AM"
            elif datos['hora'] == 12:
                hora_12h = 12
                am_pm = "PM"
            else:
                hora_12h = datos['hora'] - 12
                am_pm = "PM"
            texto += f"{hora_12h:02d}:{datos['minuto']:02d}:{datos['segundo']:02d} {am_pm}"
        
        # Temperatura
        if mostrar_temperatura:
            temp = self.obtener_temperatura()
            if temp is not None:
                texto += f"  {temp:.1f}°C"
        
        return texto
    
    def mostrar_hora(self, mostrar_temperatura=False, formato_24h=None):
        """
        Ejemplo: imprime en consola la hora formateada
        """
        print("=" * 50)
        print(self.hora_formateada(mostrar_temperatura, formato_24h))
        print("=" * 50)
        return True
    
    def monitoreo_continuo(self, intervalo=1, mostrar_temperatura=False, formato_24h=None):
        """
        Monitoreo continuo de la hora en consola.
        """
        print("Iniciando monitoreo continuo...")
        print("Presiona Ctrl+C para detener")
        print()
        
        try:
            while True:
                self.mostrar_hora(mostrar_temperatura, formato_24h)
                utime.sleep(intervalo)
                
        except KeyboardInterrupt:
            print("Monitoreo detenido por el usuario")

