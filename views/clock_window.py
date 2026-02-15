from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Signal, Property, Qt
from PySide6.QtGui import QFont
from models.clock_model import ClockModel, ClockMode
from views.ui_clock import Ui_Clock


class RelojDigitalWidget(QWidget):
    """
    Componente visual reutilizable de reloj digital
    Puede funcionar como reloj o como temporizador/cronómetro
    """
    
    # Señales personalizadas
    alarma_disparada = Signal(str)  # Emite el mensaje de alarma
    timer_completado = Signal()  # Emite cuando el temporizador termina
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_Clock()
        self.ui.setupUi(self)
        # Modelo
        self._model = ClockModel()
        
        # Timer interno para actualización
        self._qtimer = QTimer(self)
        self._qtimer.timeout.connect(self._actualizar)
        self._qtimer.start(1000)  # Actualizar cada segundo
    
    def _actualizar(self):
        """Actualiza el display cada segundo"""
        if self._model.get_mode() == ClockMode.CLOCK:
            # Modo reloj
            hora_actual = self._model.obtener_hora_actual()
            self.ui.label.setText(hora_actual)
            
            # Verificar alarma
            if self._model.verificar_alarma():
                self.alarma_disparada.emit(self._model.get_alarma_mensaje())
                # Desactivar alarma después de dispararla
                self._model.set_alarma_activada(False)
        
        elif self._model.get_mode() == ClockMode.TIMER:
            # Modo temporizador
            if not self._model.get_timer_en_pausa():
                self._model.incrementar_timer()
                
                # Verificar si el temporizador ha completado
                if self._model.timer_completado():
                    self.timer_completado.emit()
                    self._model.set_timer_en_pausa(True)
            
            # Actualizar display
            tiempo_formateado = self._model.formatear_tiempo_timer()
            self.ui.label.setText(tiempo_formateado)
    
    # Propiedades Qt para el diseñador
    @Property(str)
    def mode(self):
        """Propiedad para el modo del reloj"""
        return self._model.get_mode().value
    
    @mode.setter
    def mode(self, value):
        if value == "clock":
            self._model.set_mode(ClockMode.CLOCK)
        elif value == "timer":
            self._model.set_mode(ClockMode.TIMER)
    
    @Property(bool)
    def formato24h(self):
        """Propiedad para el formato de 24 horas"""
        return self._model.get_formato_24h()
    
    @formato24h.setter
    def formato24h(self, value):
        self._model.set_formato_24h(value)
    
    @Property(bool)
    def alarmaActivada(self):
        """Propiedad para activar/desactivar alarma"""
        return self._model.get_alarma_activada()
    
    @alarmaActivada.setter
    def alarmaActivada(self, value):
        self._model.set_alarma_activada(value)
    
    @Property(int)
    def alarmaHora(self):
        """Propiedad para la hora de la alarma"""
        return self._model.get_alarma_hora()
    
    @alarmaHora.setter
    def alarmaHora(self, value):
        self._model.set_alarma_hora(value)
    
    @Property(int)
    def alarmaMinuto(self):
        """Propiedad para el minuto de la alarma"""
        return self._model.get_alarma_minuto()
    
    @alarmaMinuto.setter
    def alarmaMinuto(self, value):
        self._model.set_alarma_minuto(value)
    
    @Property(str)
    def alarmaMensaje(self):
        """Propiedad para el mensaje de la alarma"""
        return self._model.get_alarma_mensaje()
    
    @alarmaMensaje.setter
    def alarmaMensaje(self, value):
        self._model.set_alarma_mensaje(value)
    
    @Property(int)
    def timerDuracion(self):
        """Propiedad para la duración del temporizador (en segundos)"""
        return self._model.get_timer_duracion()
    
    @timerDuracion.setter
    def timerDuracion(self, value):
        self._model.set_timer_duracion(value)
        # Si el timer está en modo regresivo y pausado, actualizar el display
        if self._model.get_mode() == ClockMode.TIMER and self._model.get_timer_en_pausa():
            if self._model.get_timer_regresivo():
                self._model.set_timer_segundos(value)
                tiempo_formateado = self._model.formatear_tiempo_timer()
                self.ui.label.setText(tiempo_formateado)
    
    @Property(bool)
    def timerRegresivo(self):
        """Propiedad para indicar si el temporizador es regresivo"""
        return self._model.get_timer_regresivo()
    
    @timerRegresivo.setter
    def timerRegresivo(self, value):
        self._model.set_timer_regresivo(value)
        # Actualizar el contador cuando se cambia el modo
        if self._model.get_mode() == ClockMode.TIMER:
            self.reiniciar_timer()
    
    # Métodos públicos para controlar el temporizador
    def iniciar_timer(self):
        """Inicia el temporizador"""
        self._model.set_timer_en_pausa(False)
    
    def pausar_timer(self):
        """Pausa el temporizador"""
        self._model.set_timer_en_pausa(True)
    
    def reiniciar_timer(self):
        """Reinicia el temporizador"""
        self._model.reiniciar_timer()
        # Forzar actualización inmediata del display
        tiempo_formateado = self._model.formatear_tiempo_timer()
        self.ui.label.setText(tiempo_formateado)
    
    def configurar_alarma(self, hora, minuto, mensaje="¡Alarma!"):
        """Configura la alarma con hora, minuto y mensaje"""
        self._model.set_alarma_hora(hora)
        self._model.set_alarma_minuto(minuto)
        self._model.set_alarma_mensaje(mensaje)
        self._model.set_alarma_activada(True)