from PySide6.QtWidgets import QMessageBox


class ClockController:
    """
    Controlador para gestionar la interacción entre la vista y el modelo
    """
    
    def __init__(self, reloj_widget):
        self.reloj = reloj_widget
        
        # Conectar señales
        self.reloj.alarma_disparada.connect(self.manejar_alarma)
        self.reloj.timer_completado.connect(self.manejar_timer_completado)
    
    def manejar_alarma(self, mensaje):
        """Maneja el evento de alarma"""
        QMessageBox.information(None, "Alarma", mensaje)
    
    def manejar_timer_completado(self):
        """Maneja el evento de temporizador completado"""
        QMessageBox.information(None, "Temporizador", "¡Tiempo completado!")
    
    def cambiar_a_modo_reloj(self):
        """Cambia el componente a modo reloj"""
        self.reloj.mode = "clock"
    
    def cambiar_a_modo_timer(self):
        """Cambia el componente a modo temporizador"""
        self.reloj.mode = "timer"
    
    def configurar_alarma(self, hora, minuto, mensaje):
        """Configura la alarma"""
        self.reloj.configurar_alarma(hora, minuto, mensaje)
    
    def iniciar_temporizador(self):
        """Inicia el temporizador"""
        self.reloj.iniciar_timer()
    
    def pausar_temporizador(self):
        """Pausa el temporizador"""
        self.reloj.pausar_timer()
    
    def reiniciar_temporizador(self):
        """Reinicia el temporizador"""
        self.reloj.reiniciar_timer()
    
    def cambiar_formato_hora(self, formato_24h):
        """Cambia el formato de visualización de la hora"""
        self.reloj.formato24h = formato_24h