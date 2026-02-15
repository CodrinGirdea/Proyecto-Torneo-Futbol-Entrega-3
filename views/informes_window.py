from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from PySide6.QtCore import QThread, Signal
from views.ui_informes_window import Ui_InformesWindow
from controllers.jasper_controller import (
    generar_informe_equipos,
    generar_informe_partidos,
    generar_informe_clasificacion
)
from controllers.equipo_controller import EquipoController
from utils.icon_helper import set_button_icon
import os
from pathlib import Path


class GeneradorThread(QThread):
    """Thread para generar informes en segundo plano"""
    finished = Signal(bool, str)  # (éxito, mensaje/ruta)
    
    def __init__(self, funcion_generadora, *args, **kwargs):
        super().__init__()
        self.funcion_generadora = funcion_generadora
        self.args = args
        self.kwargs = kwargs
    
    def run(self):
        try:
            resultado = self.funcion_generadora(*self.args, **self.kwargs)
            self.finished.emit(True, str(resultado))
        except Exception as e:
            self.finished.emit(False, str(e))


class InformesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_InformesWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Generación de Informes")
        
        self.thread_generador = None
        self.ruta_guardado = None  # Ruta personalizada de guardado
        
        # Configurar iconos
        self.setup_icons()
        
        # Configurar tooltips
        self.setup_tooltips()
        
        # Cargar equipos en el combo
        self.cargar_equipos()
        
        # Conectar señales
        self.conectar_senales()
        
        # Establecer ruta por defecto
        self.establecer_ruta_defecto()
    
    def setup_icons(self):
        """Configura los iconos de los botones"""
        try:
            set_button_icon(self.ui.btn_generar_equipos, "equipo.png", 24)
            set_button_icon(self.ui.btn_generar_partidos, "partido.png", 24)
            set_button_icon(self.ui.btn_generar_clasificacion, "clasificacion.png", 24)
            set_button_icon(self.ui.btn_volver, "volver.png", 24)
            set_button_icon(self.ui.btn_seleccionar_ruta, "carpeta.png", 20)
        except:
            # Si no encuentra los iconos, continuar sin ellos
            pass
    
    def setup_tooltips(self):
        """Configura los tooltips"""
        self.ui.btn_generar_equipos.setToolTip(
            "Genera un informe en PDF con todos los equipos, jugadores y estadísticas.\n"
            "Puedes filtrar por equipo específico si activas el checkbox."
        )
        self.ui.btn_generar_partidos.setToolTip(
            "Genera un informe en PDF con el calendario de partidos y resultados.\n"
            "Puedes filtrar por eliminatoria si activas el checkbox."
        )
        self.ui.btn_generar_clasificacion.setToolTip(
            "Genera un informe en PDF con la tabla de clasificación y eliminatorias.\n"
            "Puedes filtrar por eliminatoria si activas el checkbox."
        )
        self.ui.check_filtro_equipo.setToolTip(
            "Activa este checkbox para generar el informe solo de un equipo específico"
        )
        self.ui.check_filtro_partidos.setToolTip(
            "Activa este checkbox para filtrar partidos por eliminatoria"
        )
        self.ui.check_filtro_clasificacion.setToolTip(
            "Activa este checkbox para filtrar clasificación por eliminatoria"
        )
        self.ui.btn_seleccionar_ruta.setToolTip(
            "Selecciona una carpeta personalizada donde guardar los informes PDF.\n"
            "Por defecto se guardan en la carpeta 'informes/'"
        )
    
    def cargar_equipos(self):
        """Carga los equipos en el combo"""
        self.ui.combo_equipo.clear()
        self.ui.combo_equipo.addItem("-- Seleccionar equipo --", None)
        
        try:
            equipos = EquipoController.obtener_todos()
            for equipo in equipos:
                self.ui.combo_equipo.addItem(equipo.nombre, equipo.id)
        except Exception as e:
            print(f"Error al cargar equipos: {e}")
    
    def establecer_ruta_defecto(self):
        """Establece la ruta de guardado por defecto"""
        base_dir = Path(__file__).parent.parent
        self.ruta_guardado = str(base_dir / "informes")
        self.ui.input_ruta.setText(self.ruta_guardado)
        
        # Crear carpeta si no existe
        Path(self.ruta_guardado).mkdir(exist_ok=True)
    
    def conectar_senales(self):
        """Conecta todas las señales"""
        # Checkboxes para habilitar/deshabilitar filtros
        self.ui.check_filtro_equipo.stateChanged.connect(
            lambda state: self.ui.combo_equipo.setEnabled(state == 2)
        )
        self.ui.check_filtro_partidos.stateChanged.connect(
            lambda state: self.ui.combo_eliminatoria_partidos.setEnabled(state == 2)
        )
        self.ui.check_filtro_clasificacion.stateChanged.connect(
            lambda state: self.ui.combo_eliminatoria_clasificacion.setEnabled(state == 2)
        )
        
        # Botón seleccionar ruta
        self.ui.btn_seleccionar_ruta.clicked.connect(self.seleccionar_ruta_guardado)
        
        # Botones de generación
        self.ui.btn_generar_equipos.clicked.connect(self.generar_informe_equipos)
        self.ui.btn_generar_partidos.clicked.connect(self.generar_informe_partidos)
        self.ui.btn_generar_clasificacion.clicked.connect(self.generar_informe_clasificacion)
        
        # Botón volver
        self.ui.btn_volver.clicked.connect(self.close)
    
    def seleccionar_ruta_guardado(self):
        """Permite seleccionar una carpeta personalizada para guardar los informes"""
        carpeta = QFileDialog.getExistingDirectory(
            self,
            "Seleccionar carpeta para guardar informes",
            self.ruta_guardado,
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        
        if carpeta:
            self.ruta_guardado = carpeta
            self.ui.input_ruta.setText(carpeta)
            QMessageBox.information(
                self,
                "Ruta actualizada",
                f"Los informes se guardarán en:\n{carpeta}"
            )
    
    def generar_informe_equipos(self):
        """Genera el informe de equipos y jugadores"""
        # Obtener filtro si está activado
        equipo_id = None
        filtro_texto = "todos los equipos"
        
        if self.ui.check_filtro_equipo.isChecked():
            equipo_id = self.ui.combo_equipo.currentData()
            if not equipo_id:
                QMessageBox.warning(
                    self,
                    "Selección requerida",
                    "Por favor selecciona un equipo del desplegable o desactiva el filtro"
                )
                return
            filtro_texto = f"el equipo: {self.ui.combo_equipo.currentText()}"
        
        # Confirmar generación
        respuesta = QMessageBox.question(
            self,
            "Confirmar generación",
            f"¿Deseas generar el informe de Equipos y Jugadores?\n\n"
            f"📊 Informe de: {filtro_texto}\n"
            f"📁 Se guardará en: {self.ruta_guardado}",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.No:
            return
        
        # Deshabilitar botones durante la generación
        self.deshabilitar_botones(True)
        
        # Mostrar mensaje de progreso
        self.mostrar_mensaje_progreso("equipos", "Generando informe de equipos...")
        
        # Generar en segundo plano
        self.thread_generador = GeneradorThread(
            generar_informe_equipos,
            equipo_id=equipo_id,
            output_dir=self.ruta_guardado
        )
        self.thread_generador.finished.connect(self.on_informe_generado)
        self.thread_generador.start()
    
    def generar_informe_partidos(self):
        """Genera el informe de partidos y resultados"""
        # Obtener filtro si está activado
        eliminatoria = None
        filtro_texto = "todas las eliminatorias"
        
        if self.ui.check_filtro_partidos.isChecked():
            eliminatoria_idx = self.ui.combo_eliminatoria_partidos.currentIndex()
            if eliminatoria_idx == 0:  # "-- Todas las eliminatorias --"
                QMessageBox.warning(
                    self,
                    "Selección requerida",
                    "Por favor selecciona una eliminatoria específica o desactiva el filtro"
                )
                return
            eliminatoria = self.ui.combo_eliminatoria_partidos.currentText()
            filtro_texto = f"eliminatoria: {eliminatoria}"
        
        # Confirmar generación
        respuesta = QMessageBox.question(
            self,
            "Confirmar generación",
            f"¿Deseas generar el informe de Partidos y Resultados?\n\n"
            f"⚽ Informe de: {filtro_texto}\n"
            f"📁 Se guardará en: {self.ruta_guardado}",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.No:
            return
        
        # Deshabilitar botones durante la generación
        self.deshabilitar_botones(True)
        
        # Mostrar mensaje de progreso
        self.mostrar_mensaje_progreso("partidos", "Generando informe de partidos...")
        
        # Generar en segundo plano
        self.thread_generador = GeneradorThread(
            generar_informe_partidos,
            eliminatoria=eliminatoria,
            output_dir=self.ruta_guardado
        )
        self.thread_generador.finished.connect(self.on_informe_generado)
        self.thread_generador.start()
    
    def generar_informe_clasificacion(self):
        """Genera el informe de clasificación y eliminatorias"""
        # Obtener filtro si está activado
        eliminatoria = None
        filtro_texto = "todas las eliminatorias"
        
        if self.ui.check_filtro_clasificacion.isChecked():
            eliminatoria_idx = self.ui.combo_eliminatoria_clasificacion.currentIndex()
            if eliminatoria_idx == 0:  # "-- Todas las eliminatorias --"
                QMessageBox.warning(
                    self,
                    "Selección requerida",
                    "Por favor selecciona una eliminatoria específica o desactiva el filtro"
                )
                return
            eliminatoria = self.ui.combo_eliminatoria_clasificacion.currentText()
            filtro_texto = f"eliminatoria: {eliminatoria}"
        
        # Confirmar generación
        respuesta = QMessageBox.question(
            self,
            "Confirmar generación",
            f"¿Deseas generar el informe de Clasificación y Eliminatorias?\n\n"
            f"🏆 Informe de: {filtro_texto}\n"
            f"📁 Se guardará en: {self.ruta_guardado}",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.No:
            return
        
        # Deshabilitar botones durante la generación
        self.deshabilitar_botones(True)
        
        # Mostrar mensaje de progreso
        self.mostrar_mensaje_progreso("clasificacion", "Generando informe de clasificación...")
        
        # Generar en segundo plano
        self.thread_generador = GeneradorThread(
            generar_informe_clasificacion,
            eliminatoria=eliminatoria,
            output_dir=self.ruta_guardado
        )
        self.thread_generador.finished.connect(self.on_informe_generado)
        self.thread_generador.start()
    
    def on_informe_generado(self, exito, mensaje):
        """Callback cuando termina la generación del informe"""
        # Rehabilitar botones
        self.deshabilitar_botones(False)
        
        # Restaurar títulos de grupos
        self.ui.groupBox_equipos.setTitle("1. Informe de Equipos y Jugadores")
        self.ui.groupBox_partidos.setTitle("2. Informe de Partidos y Resultados")
        self.ui.groupBox_clasificacion.setTitle("3. Informe de Clasificación y Eliminatorias")
        
        if exito:
            # Éxito
            pdf_path = Path(mensaje)
            
            respuesta = QMessageBox.information(
                self,
                "✓ Informe generado",
                f"El informe se generó correctamente:\n\n"
                f"📄 {pdf_path.name}\n"
                f"📁 {pdf_path.parent}\n\n"
                f"¿Deseas abrir el archivo?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if respuesta == QMessageBox.Yes:
                self.abrir_pdf(pdf_path)
        else:
            # Error
            QMessageBox.critical(
                self,
                "Error al generar informe",
                f"No se pudo generar el informe:\n\n{mensaje}\n\n"
                f"Verifica que:\n"
                f"• Los archivos JRXML estén en la carpeta reports/\n"
                f"• Los archivos JAR estén en reports/lib/\n"
                f"• Java esté instalado y en el PATH\n"
                f"• La base de datos tenga datos"
            )
    
    def abrir_pdf(self, pdf_path):
        """Abre el PDF con el visor predeterminado"""
        try:
            os.startfile(str(pdf_path))
        except AttributeError:
            # Linux/Mac
            import subprocess
            subprocess.call(["xdg-open", str(pdf_path)])
        except Exception as e:
            QMessageBox.warning(
                self,
                "No se pudo abrir el PDF",
                f"El PDF se generó correctamente pero no se pudo abrir automáticamente.\n\n"
                f"Abre manualmente: {pdf_path}\n\n"
                f"Error: {e}"
            )
    
    def deshabilitar_botones(self, deshabilitar):
        """Deshabilita/habilita los botones durante la generación"""
        self.ui.btn_generar_equipos.setEnabled(not deshabilitar)
        self.ui.btn_generar_partidos.setEnabled(not deshabilitar)
        self.ui.btn_generar_clasificacion.setEnabled(not deshabilitar)
        self.ui.btn_seleccionar_ruta.setEnabled(not deshabilitar)
        self.ui.btn_volver.setEnabled(not deshabilitar)
        
        # También deshabilitar filtros
        self.ui.check_filtro_equipo.setEnabled(not deshabilitar)
        self.ui.check_filtro_partidos.setEnabled(not deshabilitar)
        self.ui.check_filtro_clasificacion.setEnabled(not deshabilitar)
        
        if not deshabilitar:
            # Restaurar estado de combos según checkboxes
            self.ui.combo_equipo.setEnabled(self.ui.check_filtro_equipo.isChecked())
            self.ui.combo_eliminatoria_partidos.setEnabled(self.ui.check_filtro_partidos.isChecked())
            self.ui.combo_eliminatoria_clasificacion.setEnabled(self.ui.check_filtro_clasificacion.isChecked())
    
    def mostrar_mensaje_progreso(self, tipo, mensaje):
        """Muestra un mensaje de progreso en la ventana"""
        if tipo == "equipos":
            self.ui.groupBox_equipos.setTitle(f"1. Informe de Equipos y Jugadores - {mensaje}")
        elif tipo == "partidos":
            self.ui.groupBox_partidos.setTitle(f"2. Informe de Partidos y Resultados - {mensaje}")
        elif tipo == "clasificacion":
            self.ui.groupBox_clasificacion.setTitle(f"3. Informe de Clasificación y Eliminatorias - {mensaje}")
    
    def closeEvent(self, event):
        """Maneja el evento de cierre de la ventana"""
        # Si hay un thread en ejecución, preguntar
        if self.thread_generador and self.thread_generador.isRunning():
            respuesta = QMessageBox.question(
                self,
                "Generación en progreso",
                "Hay un informe generándose. ¿Deseas cancelar?",
                QMessageBox.Yes | QMessageBox.No
            )
            
            if respuesta == QMessageBox.No:
                event.ignore()
                return
            
            # Terminar el thread
            self.thread_generador.terminate()
            self.thread_generador.wait()
        
        event.accept()
