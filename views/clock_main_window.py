import os, sys
from PySide6.QtWidgets import (QApplication, QWidget, QMessageBox,)
from PySide6.QtCore import QTranslator
from views.clock_window import RelojDigitalWidget
from controllers.clock_controller import ClockController
from views.ui_clock_main_window import Ui_MainWindow

class ClockMainWidget(QWidget):
    """
    Widget de reloj completo con todos los controles
    (puede ser incrustado en otras ventanas)
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.translator = QTranslator()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.reloj = RelojDigitalWidget()

        self.reloj.setParent(self.ui.centralwidget)
        self.reloj.setGeometry(10, 40, 781, 95)
        
        self.controller = ClockController(self.reloj)
        
        self._conectar_senales()
        
        self.reloj.alarma_disparada.connect(self.mostrar_alarma_en_label)
        self.reloj.timer_completado.connect(self.mostrar_timer_completado)
    
    def _conectar_senales(self):
        """Conecta las señales de los controles"""
        self.ui.combo_idioma.currentIndexChanged.connect(self.cambiar_idioma)
        
        self.ui.check_24h.stateChanged.connect(self.cambiar_formato)
        self.ui.btn_configurar_alarma.clicked.connect(self.configurar_alarma)
        self.ui.btn_modo_reloj.clicked.connect(self.activar_modo_reloj)
        
        self.ui.btn_modo_timer.clicked.connect(self.activar_modo_timer)
        self.ui.btn_iniciar.clicked.connect(self.iniciar_timer)
        self.ui.btn_pausar.clicked.connect(self.pausar_timer)
        self.ui.btn_reiniciar.clicked.connect(self.reiniciar_timer)
    
    def cambiar_formato(self, state):
        """Cambia el formato de visualización de la hora"""
        self.controller.cambiar_formato_hora(state == 2)
    
    def configurar_alarma(self):
        """Configura la alarma con los valores actuales"""
        hora = self.ui.spin_hora.value()
        minuto = self.ui.spin_minuto.value()
        mensaje = self.ui.input_mensaje.text()
        
        if not mensaje:
            mensaje = self.ui.input_mensaje.placeholderText()
        
        self.controller.configurar_alarma(hora, minuto, mensaje)
        QMessageBox.information(self, self.tr("Alarma"), 
                               self.tr("Alarma configurada para las {0}:{1}").format(
                                   f"{hora:02d}", f"{minuto:02d}"))
    
    def activar_modo_reloj(self):
        """Activa el modo reloj"""
        self.controller.cambiar_a_modo_reloj()
        self.ui.label_eventos.setText(self.tr("Modo: RELOJ"))
    
    def activar_modo_timer(self):
        """Activa el modo temporizador"""
        self.controller.cambiar_a_modo_timer()
        
        self.reloj.timerRegresivo = self.ui.check_regresivo.isChecked()
        self.reloj.timerDuracion = self.ui.spin_duracion.value()

        self.controller.reiniciar_temporizador()
        
        self.ui.label_eventos.setText(self.tr("Modo: TEMPORIZADOR"))
    
    def iniciar_timer(self):
        """Inicia el temporizador"""
        self.controller.iniciar_temporizador()
        self.ui.label_eventos.setText(self.tr("Temporizador iniciado"))
    
    def pausar_timer(self):
        """Pausa el temporizador"""
        self.controller.pausar_temporizador()
        self.ui.label_eventos.setText(self.tr("Temporizador pausado"))
    
    def reiniciar_timer(self):
        """Reinicia el temporizador"""
        self.controller.reiniciar_temporizador()
        self.ui.label_eventos.setText(self.tr("Temporizador reiniciado"))
    
    def mostrar_alarma_en_label(self, mensaje):
        """Muestra el mensaje de alarma en el label"""
        self.ui.label_eventos.setText(self.tr("ALARMA: {0}").format(mensaje))
        self.ui.label_eventos.setStyleSheet("padding: 10px; background-color: #ffcccc;")
    
    def mostrar_timer_completado(self):
        """Muestra mensaje cuando el temporizador se completa"""
        self.ui.label_eventos.setText(self.tr("TEMPORIZADOR COMPLETADO"))
    
    def cambiar_idioma(self, index):
        """Cambia el idioma de la aplicación"""
        app = QApplication.instance()
        app.removeTranslator(self.translator)

        if index == 1:
            if hasattr(sys,'_MEIPASS'):
                ruta=os.path.join(sys._MEIPASS,"resources/translations/clock_en.qm")
            else:
                ruta=os.path.join(os.path.abspath("."), "resources/translations/clock_en.qm")
            

            if self.translator.load(ruta):
                print(f"Traducción cargada correctamente: {ruta}")
                app.installTranslator(self.translator)
            else:
                print("ERROR: No se pudo cargar el traductor")
                print("Ruta usada:", ruta)
                print("¿Existe?", os.path.exists(ruta))
        else:
            print("Cambiando a español (sin traductor)")

        self.ui.retranslateUi(self)


# Mantener compatibilidad con la clase original (si se usa como ventana principal)
class VentanaPrincipal(QWidget):
    """Alias para compatibilidad hacia atrás"""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Redirigir a ClockWidget
        self.clock_widget = ClockMainWidget(self)