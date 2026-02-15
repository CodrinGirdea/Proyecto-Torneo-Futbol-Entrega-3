from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QTableWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from views.ui_resultados_window import Ui_Resultados
from controllers.resultado_controller import ResultadoController
from controllers.partido_controller import PartidoController
from controllers.participante_controller import ParticipanteController
from utils.icon_helper import set_button_icon
from views.clock_main_window import ClockMainWidget  # Importar el widget completo del reloj
import math

class ResultadoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Resultados()
        self.ui.setupUi(self)
        
        # ==================== INTEGRACIÓN DEL WIDGET COMPLETO DEL RELOJ ====================
        # Crear el widget completo del reloj (con todos sus controles)
        self.clock_widget = ClockMainWidget()
        
        # Crear un layout para el contenedor del reloj y añadir el widget
        reloj_layout = QVBoxLayout(self.ui.widget_reloj_container)
        reloj_layout.setContentsMargins(0, 0, 0, 0)
        reloj_layout.addWidget(self.clock_widget)
        
        # Acceso directo al reloj y controlador
        self.reloj = self.clock_widget.reloj
        self.controller = self.clock_widget.controller
        
        # Conectar señales del reloj
        self.reloj.alarma_disparada.connect(self.cuando_alarma)
        self.reloj.timer_completado.connect(self.cuando_termina_partido)
        
        # ====================================================================

        self.setup_icons()
        self.setup_tooltips()
        self.setWindowTitle("Actualización de resultados")
        self.partido_actual_id = None

        self.ui.combo_partidos.currentIndexChanged.connect(self.cargar_partido_seleccionado)
        self.ui.btn_anadir_gol.clicked.connect(self.anadir_gol)
        self.ui.btn_anadir_tarjetas.clicked.connect(self.anadir_tarjeta)
        self.ui.btn_finalizar_partido.clicked.connect(self.finalizar_partido)
        self.ui.btn_volver.clicked.connect(self.close)

        self.ui.table_goles.itemDoubleClicked.connect(self.eliminar_gol_seleccionado)
        self.ui.table_tarjetas.itemDoubleClicked.connect(self.eliminar_tarjeta_seleccionada)
        self.ui.table_goles.setColumnHidden(0, True)
        self.ui.table_tarjetas.setColumnHidden(0, True)

        self.cargar_partidos_pendientes()
    
    # ==================== MÉTODOS DEL RELOJ COMPLETO ====================
    
    def cuando_alarma(self, mensaje):
        """Se ejecuta cuando se dispara la alarma del reloj"""
        QMessageBox.information(
            self,
            "⏰ ALARMA",
            f"¡ALARMA ACTIVADA!\n\n{mensaje}"
        )
    
    def obtener_minuto_actual(self):
        """
        Obtiene el minuto actual del cronómetro redondeado hacia arriba.
        Si está en 1:23 (1 minuto 23 segundos), devuelve 2.
        """
        try:
            # Acceder al modelo del reloj
            segundos_totales = self.reloj._model.get_timer_segundos()
            
            # Convertir segundos a minutos y redondear hacia arriba
            minutos = math.ceil(segundos_totales / 60)
            
            return minutos
        except Exception as e:
            QMessageBox.warning(
                self,
                "Error",
                f"No se pudo obtener el minuto del cronómetro.\nAsegúrate de que el cronómetro esté en modo Timer.\n\nError: {str(e)}"
            )
            return 0
    
    def cuando_termina_partido(self):
        """Se ejecuta cuando el cronómetro llega al tiempo configurado"""
        QMessageBox.information(
            self,
            "⏱️ Tiempo de Partido",
            "¡El tiempo del partido ha finalizado!\n\n"
            "Recuerda finalizar el partido para registrar el resultado."
        )
    
    def reiniciar_cronometro_para_nuevo_partido(self):
        """Reinicia el cronómetro cuando se selecciona un nuevo partido"""
        try:
            # Configurar como cronómetro progresivo (NO regresivo)
            self.clock_widget.ui.check_regresivo.setChecked(False)
            
            # Configurar duración a 90 minutos (5400 segundos)
            self.clock_widget.ui.spin_duracion.setValue(5400)
            
            # Activar modo timer
            self.clock_widget.activar_modo_timer()
            
            # El cronómetro estará listo para iniciar manualmente
        except Exception as e:
            print(f"Error al reiniciar cronómetro: {e}")
    
    # ==============================================================

    def cargar_partidos_pendientes(self):
        self.ui.combo_partidos.clear()
        self.ui.combo_partidos.addItem("Seleccionar partido", None)
        
        partidos = ResultadoController.obtener_partidos_pendientes()
        equipos = PartidoController.obtener_todos_los_equipos()
        
        for partido in partidos:
            equipo_local = ""
            equipo_visitante = ""
            for eq in equipos:
                if eq.id == partido.equipo_local_id:
                    equipo_local = eq.nombre
                if eq.id == partido.equipo_visitante_id:
                    equipo_visitante = eq.nombre
            
            texto = f"ID:{partido.id} - {equipo_local} vs {equipo_visitante} - {partido.fecha} {partido.hora} ({partido.eliminatoria})"
            self.ui.combo_partidos.addItem(texto, partido.id)

    def cargar_partido_seleccionado(self):
        self.partido_actual_id = self.ui.combo_partidos.currentData()
        
        if not self.partido_actual_id:
            self.limpiar_todo()
            return
        
        self.reiniciar_cronometro_para_nuevo_partido()
        
        partido = PartidoController.obtener_partido_por_id(self.partido_actual_id)
        if not partido:
            return
        
        self.cargar_jugadores_partido(partido.equipo_local_id, partido.equipo_visitante_id)
        self.cargar_goles()
        self.cargar_tarjetas()

    def cargar_jugadores_partido(self, equipo_local_id, equipo_visitante_id):
        self.ui.combo_jugador_gol.clear()
        self.ui.combo_jugador_tarjeta.clear()
        
        self.ui.combo_jugador_gol.addItem("Seleccionar Jugador", None)
        self.ui.combo_jugador_tarjeta.addItem("Seleccionar Jugador", None)
        
        jugadores_local = ParticipanteController.obtener_participantes_por_equipo(equipo_local_id)
        equipos = PartidoController.obtener_todos_los_equipos()
        equipo_local_nombre = ""
        for eq in equipos:
            if eq.id == equipo_local_id:
                equipo_local_nombre = eq.nombre
                break
        
        for jugador in jugadores_local:
            texto = f"{jugador.nombre} ({equipo_local_nombre})"
            self.ui.combo_jugador_gol.addItem(texto, jugador.id)
            self.ui.combo_jugador_tarjeta.addItem(texto, jugador.id)
        
        jugadores_visitante = ParticipanteController.obtener_participantes_por_equipo(equipo_visitante_id)
        equipo_visitante_nombre = ""
        for eq in equipos:
            if eq.id == equipo_visitante_id:
                equipo_visitante_nombre = eq.nombre
                break
        
        for jugador in jugadores_visitante:
            texto = f"{jugador.nombre} ({equipo_visitante_nombre})"
            self.ui.combo_jugador_gol.addItem(texto, jugador.id)
            self.ui.combo_jugador_tarjeta.addItem(texto, jugador.id)

    def cargar_goles(self):
        self.ui.table_goles.setRowCount(0)
        self.ui.table_goles.setColumnCount(3)
        self.ui.table_goles.setHorizontalHeaderLabels(["ID", "Jugador", "Minuto"])
        if not self.partido_actual_id:
            return
            
        goles = ResultadoController.obtener_goles_partido(self.partido_actual_id)
            
        for gol in goles:
            row = self.ui.table_goles.rowCount()
            self.ui.table_goles.insertRow(row)
                
            jugador = ParticipanteController.obtener_participante_por_id(gol.jugador_id)
            nombre_jugador = ""
            if jugador:
                nombre_jugador = jugador.nombre  
            else:
                nombre_jugador = "Desconocido"
                
            self.ui.table_goles.setItem(row, 0, QTableWidgetItem(str(gol.id)))
            self.ui.table_goles.setItem(row, 1, QTableWidgetItem(nombre_jugador))
            self.ui.table_goles.setItem(row, 2, QTableWidgetItem(str(gol.minuto)))

        self.ui.table_goles.setColumnHidden(0, True)

    def cargar_tarjetas(self):
        self.ui.table_tarjetas.setRowCount(0)
        self.ui.table_tarjetas.setColumnCount(4)
        self.ui.table_tarjetas.setHorizontalHeaderLabels(["ID", "Jugador", "Tipo", "Minuto"])
        
        if not self.partido_actual_id:
            return
        
        tarjetas = ResultadoController.obtener_tarjetas_partido(self.partido_actual_id)
        
        for tarjeta in tarjetas:
            row = self.ui.table_tarjetas.rowCount()
            self.ui.table_tarjetas.insertRow(row)
            
            jugador = ParticipanteController.obtener_participante_por_id(tarjeta.jugador_id)
            nombre_jugador = ""
            if jugador:
                nombre_jugador = jugador.nombre
            else:
                nombre_jugador = "Desconocido"
            
            self.ui.table_tarjetas.setItem(row, 0, QTableWidgetItem(str(tarjeta.id)))
            self.ui.table_tarjetas.setItem(row, 1, QTableWidgetItem(nombre_jugador))
            self.ui.table_tarjetas.setItem(row, 2, QTableWidgetItem(tarjeta.tipo.capitalize()))
            self.ui.table_tarjetas.setItem(row, 3, QTableWidgetItem(str(tarjeta.minuto)))

        self.ui.table_tarjetas.setColumnHidden(0, True)

    def anadir_gol(self):
        """Añade un gol capturando automáticamente el minuto del cronómetro"""
        if self.partido_actual_id is None:
            QMessageBox.warning(self, "Advertencia", "Selecciona un partido")
            return
        
        jugador_id = self.ui.combo_jugador_gol.currentData()
        
        if not jugador_id:
            QMessageBox.warning(self, "Advertencia", "Selecciona un jugador")
            return
        
        # ⚽ CAPTURAR MINUTO DEL CRONÓMETRO AUTOMÁTICAMENTE
        minuto = self.obtener_minuto_actual()
        
        if minuto == 0:
            return  # Ya se mostró el error
        
        estado, mensaje = ResultadoController.registrar_gol(self.partido_actual_id, jugador_id, minuto)
        
        if estado:
            jugador = ParticipanteController.obtener_participante_por_id(jugador_id)
            nombre_jugador = jugador.nombre if jugador else "Jugador"
            
            QMessageBox.information(
                self, 
                "⚽ Gol Registrado", 
                f"Gol de {nombre_jugador}\nMinuto: {minuto}'"
            )
            self.cargar_goles()
            self.ui.combo_jugador_gol.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def anadir_tarjeta(self):
        """Añade una tarjeta capturando automáticamente el minuto del cronómetro"""
        if not self.partido_actual_id:
            QMessageBox.warning(self, "Advertencia", "Selecciona un partido")
            return
        
        jugador_id = self.ui.combo_jugador_tarjeta.currentData()
        tipo = self.ui.combo_tipo_tarjeta.currentText().lower()
        
        if not jugador_id:
            QMessageBox.warning(self, "Advertencia", "Selecciona un jugador")
            return
        
        if not tipo:
            QMessageBox.warning(self, "Advertencia", "Selecciona el tipo de tarjeta")
            return
        
        # 🟨🟥 CAPTURAR MINUTO DEL CRONÓMETRO AUTOMÁTICAMENTE
        minuto = self.obtener_minuto_actual()
        
        if minuto == 0:
            return  # Ya se mostró el error
        
        estado, mensaje = ResultadoController.registrar_tarjeta(self.partido_actual_id, jugador_id, tipo, minuto)
        
        if estado:
            jugador = ParticipanteController.obtener_participante_por_id(jugador_id)
            nombre_jugador = jugador.nombre if jugador else "Jugador"
            
            emoji_tarjeta = "🟨" if tipo.lower() == "amarilla" else "🟥"
            
            QMessageBox.information(
                self, 
                f"{emoji_tarjeta} Tarjeta Registrada", 
                f"Tarjeta {tipo} para {nombre_jugador}\nMinuto: {minuto}'"
            )
            self.cargar_tarjetas()
            self.ui.combo_jugador_tarjeta.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def eliminar_gol_seleccionado(self):
        selected_items = self.ui.table_goles.selectedItems()
        if not selected_items:
            return
        
        row = selected_items[0].row()
        gol_id = int(self.ui.table_goles.item(row, 0).text())
        nombre_jugador = self.ui.table_goles.item(row, 1).text()
        
        respuesta = QMessageBox.question(self, "Confirmar", f"¿Eliminar gol de {nombre_jugador}?", QMessageBox.Yes | QMessageBox.No)
        
        if respuesta == QMessageBox.Yes:
            goles = ResultadoController.obtener_goles_partido(self.partido_actual_id)
            jugador_id = None
            for gol in goles:
                if gol.id == gol_id:
                    jugador_id = gol.jugador_id
                    break
            
            if jugador_id:
                exito, mensaje = ResultadoController.eliminar_gol(gol_id, jugador_id)
                if exito:
                    self.cargar_goles()

    def eliminar_tarjeta_seleccionada(self):
        selected_items = self.ui.table_tarjetas.selectedItems()
        if not selected_items:
            return
        
        row = selected_items[0].row()
        tarjeta_id = int(self.ui.table_tarjetas.item(row, 0).text())
        nombre_jugador = self.ui.table_tarjetas.item(row, 1).text()
        
        respuesta = QMessageBox.question(self, "Confirmar", f"¿Eliminar tarjeta de {nombre_jugador}?", QMessageBox.Yes | QMessageBox.No)
        
        if respuesta == QMessageBox.Yes:
            tarjetas = ResultadoController.obtener_tarjetas_partido(self.partido_actual_id)
            jugador_id = None
            for tarjeta in tarjetas:
                if tarjeta.id == tarjeta_id:
                    jugador_id = tarjeta.jugador_id
                    break
            
            if jugador_id:
                exito, mensaje = ResultadoController.eliminar_tarjeta(tarjeta_id, jugador_id)
                if exito:
                    self.cargar_tarjetas()
    
    def finalizar_partido(self):
        """Marca el partido como jugado"""
        if not self.partido_actual_id:
            QMessageBox.warning(self, "Advertencia", "Selecciona un partido")
            return
    
        partido = PartidoController.obtener_partido_por_id(self.partido_actual_id)
        if not partido:
            QMessageBox.warning(self, "Error", "No se pudo obtener el partido")
            return
        
        ResultadoController.actualizar_resultado_partido(self.partido_actual_id)
        
        partido = PartidoController.obtener_partido_por_id(self.partido_actual_id)
        
        if partido.goles_local == partido.goles_visitante:
            QMessageBox.warning(self, "Empate no permitido", "El partido no puede terminar en empate, debe haber un ganador")
            return
        
        respuesta = QMessageBox.question(self, "Confirmar", f"Resultado: {partido.goles_local} - {partido.goles_visitante}\n\n¿Marcar este partido como finalizado? No podrás editarlo después.", QMessageBox.Yes | QMessageBox.No)
        
        if respuesta == QMessageBox.Yes:
            estado, mensaje = ResultadoController.finalizar_partido(self.partido_actual_id)
            
            if estado:
                QMessageBox.information(self, "Éxito", mensaje)
                self.cargar_partidos_pendientes()
                self.limpiar_todo()
            else:
                QMessageBox.warning(self, "Error", mensaje)
    
    def limpiar_todo(self):
        self.partido_actual_id = None
        self.ui.combo_jugador_gol.clear()
        self.ui.combo_jugador_tarjeta.clear()
        self.ui.table_goles.setRowCount(0)
        self.ui.table_tarjetas.setRowCount(0)
        
        # Reiniciar también el cronómetro
        self.reiniciar_cronometro_para_nuevo_partido()

    def setup_icons(self):
        """Configura los iconos de los botones"""
        set_button_icon(self.ui.btn_anadir_gol, "crear.png", 20)
        set_button_icon(self.ui.btn_anadir_tarjetas, "crear.png", 20)
        set_button_icon(self.ui.btn_finalizar_partido, "editar.png", 20)
        set_button_icon(self.ui.btn_volver, "volver.png", 20)

    def setup_tooltips(self):
        """Configura los tooltips"""
        self.ui.btn_anadir_gol.setToolTip("Añadir gol")
        self.ui.btn_anadir_tarjetas.setToolTip("Añadir tarjeta")
        self.ui.btn_finalizar_partido.setToolTip("Marcar el partido como terminado")
        self.ui.btn_volver.setToolTip("Volver al menú principal")
        
        self.ui.combo_jugador_gol.setToolTip("Seleccionar el autor del gol")
        self.ui.combo_jugador_tarjeta.setToolTip("Seleccionar el autor de la tarjeta")
        self.ui.combo_tipo_tarjeta.setToolTip("Seleccionar tipo de tarjeta")
        self.ui.combo_partidos.setToolTip("Seleccionar partido a gestionar")