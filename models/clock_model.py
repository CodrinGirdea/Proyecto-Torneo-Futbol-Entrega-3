from enum import Enum
from datetime import datetime, time


class ClockMode(Enum):
    """Enumeración para los modos del reloj"""
    CLOCK = "clock"
    TIMER = "timer"


class ClockModel:
    """Modelo que contiene la lógica de negocio del reloj"""
    
    def __init__(self):
        # Propiedades del reloj
        self._mode = ClockMode.CLOCK
        self._formato_24h = True
        self._alarma_activada = False
        self._alarma_hora = 0
        self._alarma_minuto = 0
        self._alarma_mensaje = "¡Alarma!"
        
        # Propiedades del temporizador
        self._timer_segundos = 0
        self._timer_duracion = 60  # Duración en segundos
        self._timer_regresivo = True
        self._timer_en_pausa = True
        
    # Getters y Setters para el modo
    def get_mode(self):
        return self._mode
    
    def set_mode(self, mode):
        if isinstance(mode, ClockMode):
            self._mode = mode
        else:
            raise ValueError("El modo debe ser de tipo RelojMode")
    
    # Getters y Setters para formato de hora
    def get_formato_24h(self):
        return self._formato_24h
    
    def set_formato_24h(self, formato_24h):
        self._formato_24h = bool(formato_24h)
    
    # Getters y Setters para alarma
    def get_alarma_activada(self):
        return self._alarma_activada
    
    def set_alarma_activada(self, activada):
        self._alarma_activada = bool(activada)
    
    def get_alarma_hora(self):
        return self._alarma_hora
    
    def set_alarma_hora(self, hora):
        if 0 <= hora <= 23:
            self._alarma_hora = hora
        else:
            raise ValueError("La hora debe estar entre 0 y 23")
    
    def get_alarma_minuto(self):
        return self._alarma_minuto
    
    def set_alarma_minuto(self, minuto):
        if 0 <= minuto <= 59:
            self._alarma_minuto = minuto
        else:
            raise ValueError("El minuto debe estar entre 0 y 59")
    
    def get_alarma_mensaje(self):
        return self._alarma_mensaje
    
    def set_alarma_mensaje(self, mensaje):
        self._alarma_mensaje = str(mensaje)
    
    # Getters y Setters para temporizador
    def get_timer_segundos(self):
        return self._timer_segundos
    
    def set_timer_segundos(self, segundos):
        self._timer_segundos = int(segundos)
    
    def get_timer_duracion(self):
        return self._timer_duracion
    
    def set_timer_duracion(self, duracion):
        self._timer_duracion = int(duracion)
    
    def get_timer_regresivo(self):
        return self._timer_regresivo
    
    def set_timer_regresivo(self, regresivo):
        self._timer_regresivo = bool(regresivo)
    
    def get_timer_en_pausa(self):
        return self._timer_en_pausa
    
    def set_timer_en_pausa(self, pausa):
        self._timer_en_pausa = bool(pausa)
    
    # Métodos de lógica de negocio
    def obtener_hora_actual(self):
        """Devuelve la hora actual formateada"""
        ahora = datetime.now()
        if self._formato_24h:
            return ahora.strftime("%H:%M:%S")
        else:
            return ahora.strftime("%I:%M:%S %p")
    
    def verificar_alarma(self):
        """Verifica si la alarma debe dispararse"""
        if not self._alarma_activada:
            return False
        
        ahora = datetime.now()
        return (ahora.hour == self._alarma_hora and 
                ahora.minute == self._alarma_minuto and
                ahora.second == 0)
    
    def incrementar_timer(self):
        """Incrementa el temporizador en 1 segundo"""
        if self._timer_regresivo:
            self._timer_segundos -= 1
            if self._timer_segundos < 0:
                self._timer_segundos = 0
        else:
            self._timer_segundos += 1
    
    def formatear_tiempo_timer(self):
        """Formatea el tiempo del temporizador como HH:MM:SS"""
        horas = self._timer_segundos // 3600
        minutos = (self._timer_segundos % 3600) // 60
        segundos = self._timer_segundos % 60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    
    def timer_completado(self):
        """Verifica si el temporizador ha completado"""
        if self._timer_regresivo:
            return self._timer_segundos <= 0
        else:
            return self._timer_segundos >= self._timer_duracion
    
    def reiniciar_timer(self):
        """Reinicia el temporizador"""
        if self._timer_regresivo:
            self._timer_segundos = self._timer_duracion
        else:
            self._timer_segundos = 0
        self._timer_en_pausa = True
        
    def get_timer_segundos_actuales(self):
        """Obtiene los segundos actuales del timer"""
        return self._timer_segundos