from PySide6.QtWidgets import QWidget,QMessageBox,QTableWidgetItem,QTableWidget
from PySide6.QtCore import QDate, QTime
from views.ui_partidos_window import Ui_Gestion_de_partidos
from controllers.partido_controller import PartidoController  
from utils.icon_helper import set_button_icon

class PartidoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Gestion_de_partidos()
        self.ui.setupUi(self)

        self.setup_icons()

        self.setup_tooltips()

        self.setWindowTitle("Gestión de partidos")

        self.partido_seleccionado_id=None

        self.ui.input_fecha.setDate(QDate.currentDate())
        self.ui.input_hora.setTime(QTime.currentTime())

        self.ui.btn_crear.clicked.connect(self.crear_partido)
        self.ui.btn_actualizar.clicked.connect(self.actualizar_partido)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_partido)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.ui.btn_volver.clicked.connect(self.close)

        self.ui.table_partidos.itemSelectionChanged.connect(self.cargar_partido_seleccionado)
        self.ui.table_partidos.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.cargar_equipos()
        self.cargar_arbitros()
        self.cargar_partidos()

    def cargar_equipos(self):
        self.ui.combo_equipo_local.clear()
        self.ui.combo_equipo_visitante.clear()

        self.ui.combo_equipo_local.addItem("Seleccionar equipo", None)
        self.ui.combo_equipo_visitante.addItem("Seleccionar equipo", None)

        equipos=PartidoController.obtener_todos_los_equipos()

        for equipo in equipos:
            self.ui.combo_equipo_local.addItem(equipo.nombre,equipo.id)
            self.ui.combo_equipo_visitante.addItem(equipo.nombre,equipo.id)

    def cargar_arbitros(self):
        self.ui.combo_arbitro.clear()

        self.ui.combo_arbitro.addItem("Seleccionar arbitro",None)

        arbitros=PartidoController.obtener_arbitros()

        for arbitro in arbitros:
            self.ui.combo_arbitro.addItem(arbitro.nombre,arbitro.id)

    def cargar_partidos(self):
        partidos=PartidoController.obtener_todos_partidos()
        self.ui.table_partidos.setRowCount(0)

        equipos=PartidoController.obtener_todos_los_equipos()
        arbitros=PartidoController.obtener_arbitros()

        for partido in partidos:
            row =self.ui.table_partidos.rowCount()
            self.ui.table_partidos.insertRow(row)

            equipo_local_nombre=""
            equipo_visitante_nombre=""

            for equipo in equipos:
                if equipo.id==partido.equipo_local_id:
                    equipo_local_nombre=equipo.nombre
                if equipo.id==partido.equipo_visitante_id:
                    equipo_visitante_nombre=equipo.nombre

            arbitro_nombre=""

            for arbitro in arbitros:
                if arbitro.id==partido.arbitro_id:
                    arbitro_nombre=arbitro.nombre
                    break
            
            resultado=f"{partido.goles_local} - {partido.goles_visitante}"

            estado="Jugado" if partido.jugado else "Pendiente"

            self.ui.table_partidos.setItem(row, 0, QTableWidgetItem(str(partido.id)))
            self.ui.table_partidos.setItem(row, 1, QTableWidgetItem(equipo_local_nombre))
            self.ui.table_partidos.setItem(row, 2, QTableWidgetItem(equipo_visitante_nombre))
            self.ui.table_partidos.setItem(row, 3, QTableWidgetItem(arbitro_nombre))
            self.ui.table_partidos.setItem(row, 4, QTableWidgetItem(partido.fecha))
            self.ui.table_partidos.setItem(row, 5, QTableWidgetItem(partido.hora))
            self.ui.table_partidos.setItem(row, 6, QTableWidgetItem(partido.eliminatoria))
            self.ui.table_partidos.setItem(row, 7, QTableWidgetItem(resultado))
            self.ui.table_partidos.setItem(row, 8, QTableWidgetItem(estado))

    def cargar_partido_seleccionado(self):
        seleccionado = self.ui.table_partidos.selectedItems()
        if seleccionado:
            row = seleccionado[0].row()
            self.partido_seleccionado_id = int(self.ui.table_partidos.item(row, 0).text())
            
            partido = PartidoController.obtener_partido_por_id(self.partido_seleccionado_id)
            if partido:
                for i in range(self.ui.combo_equipo_local.count()):
                    if self.ui.combo_equipo_local.itemData(i) == partido.equipo_local_id:
                        self.ui.combo_equipo_local.setCurrentIndex(i)
                        break
                
                for i in range(self.ui.combo_equipo_visitante.count()):
                    if self.ui.combo_equipo_visitante.itemData(i) == partido.equipo_visitante_id:
                        self.ui.combo_equipo_visitante.setCurrentIndex(i)
                        break
                
                for i in range(self.ui.combo_arbitro.count()):
                    if self.ui.combo_arbitro.itemData(i) == partido.arbitro_id:
                        self.ui.combo_arbitro.setCurrentIndex(i)
                        break
                
                fecha_parts = partido.fecha.split('-')
                if len(fecha_parts) == 3:
                    qdate = QDate(int(fecha_parts[0]), int(fecha_parts[1]), int(fecha_parts[2]))
                    self.ui.input_fecha.setDate(qdate)
                
                hora_parts = partido.hora.split(':')
                if len(hora_parts) >= 2:
                    qtime = QTime(int(hora_parts[0]), int(hora_parts[1]))
                    self.ui.input_hora.setTime(qtime)
                
                index = self.ui.combo_eliminatoria.findText(partido.eliminatoria)
                self.ui.combo_eliminatoria.setCurrentIndex(index if index >= 0 else 0)
                
                self.ui.spin_goles_local.setValue(partido.goles_local)
                self.ui.spin_goles_visitante.setValue(partido.goles_visitante)
                
                self.ui.check_jugado.setChecked(bool(partido.jugado))

    def crear_partido(self):
        equipo_local_id = self.ui.combo_equipo_local.currentData()
        equipo_visitante_id = self.ui.combo_equipo_visitante.currentData()
        arbitro_id = self.ui.combo_arbitro.currentData()
        fecha = self.ui.input_fecha.date().toString("yyyy-MM-dd")
        hora = self.ui.input_hora.time().toString("HH:mm")
        eliminatoria = self.ui.combo_eliminatoria.currentText()
        goles_local = self.ui.spin_goles_local.value()
        goles_visitante = self.ui.spin_goles_visitante.value()
        jugado = 1 if self.ui.check_jugado.isChecked() else 0
        
        exito, mensaje = PartidoController.crear_partido(
            equipo_local_id, equipo_visitante_id, arbitro_id, fecha, hora,
            eliminatoria, goles_local, goles_visitante, jugado
        )
        
        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.limpiar_campos()
            self.cargar_partidos()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def actualizar_partido(self):
        if not self.partido_seleccionado_id:
            QMessageBox.warning(self, "Advertencia", "Selecciona un partido de la tabla")
            return
        
        equipo_local_id = self.ui.combo_equipo_local.currentData()
        equipo_visitante_id = self.ui.combo_equipo_visitante.currentData()
        arbitro_id = self.ui.combo_arbitro.currentData()
        fecha = self.ui.input_fecha.date().toString("yyyy-MM-dd")
        hora = self.ui.input_hora.time().toString("HH:mm")
        eliminatoria = self.ui.combo_eliminatoria.currentText()
        goles_local = self.ui.spin_goles_local.value()
        goles_visitante = self.ui.spin_goles_visitante.value()
        jugado = 1 if self.ui.check_jugado.isChecked() else 0
        
        exito, mensaje = PartidoController.actualizar_partido(
            self.partido_seleccionado_id, equipo_local_id, equipo_visitante_id,
            arbitro_id, fecha, hora, eliminatoria, goles_local, goles_visitante, jugado
        )
        
        if exito:
            QMessageBox.information(self, "Éxito", mensaje)
            self.limpiar_campos()
            self.cargar_partidos()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def eliminar_partido(self):
        if not self.partido_seleccionado_id:
            QMessageBox.warning(self, "Advertencia", "Selecciona un partido de la tabla")
            return
        
        respuesta = QMessageBox.question(
            self, "Confirmar", "¿Estás seguro de eliminar este partido?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if respuesta == QMessageBox.Yes:
            exito, mensaje = PartidoController.eliminar_partido(self.partido_seleccionado_id)
            
            if exito:
                QMessageBox.information(self, "Éxito", mensaje)
                self.limpiar_campos()
                self.cargar_partidos()
            else:
                QMessageBox.warning(self, "Error", mensaje)

    def limpiar_campos(self):
        self.ui.combo_equipo_local.setCurrentIndex(0)
        self.ui.combo_equipo_visitante.setCurrentIndex(0)
        self.ui.combo_arbitro.setCurrentIndex(0)
        self.ui.input_fecha.setDate(QDate.currentDate())
        self.ui.input_hora.setTime(QTime.currentTime())
        self.ui.combo_eliminatoria.setCurrentIndex(0)
        self.ui.spin_goles_local.setValue(0)
        self.ui.spin_goles_visitante.setValue(0)
        self.ui.check_jugado.setChecked(False)
        self.partido_seleccionado_id = None

    def setup_icons(self):
        """Configura los iconos de los botones"""
        set_button_icon(self.ui.btn_crear, "crear.png", 20)
        set_button_icon(self.ui.btn_actualizar, "editar.png", 20)
        set_button_icon(self.ui.btn_eliminar, "eliminar.png", 20)
        set_button_icon(self.ui.btn_limpiar, "limpiar.png", 20)
        set_button_icon(self.ui.btn_volver, "volver.png", 20)

    def setup_tooltips(self):
        """Configura los tooltips"""
        self.ui.btn_crear.setToolTip("Añadir un nuevo participante")
        self.ui.btn_actualizar.setToolTip("Actualizar el participante seleccionado")
        self.ui.btn_eliminar.setToolTip("Eliminar el participante seleccionado")
        self.ui.btn_limpiar.setToolTip("Limpiar todos los campos del formulario")
        self.ui.btn_volver.setToolTip("Volver al menú principal")
        
        self.ui.input_fecha.setToolTip("Fecha cuando se disputará el partido")
        self.ui.input_hora.setToolTip("Hora cuando se disputará el partido")
        self.ui.combo_equipo_local.setToolTip("Equipo local del partido")
        self.ui.combo_equipo_visitante.setToolTip("Equipo visitante del partido")
        self.ui.combo_arbitro.setToolTip("Arbitro asignado al partido")
        self.ui.combo_eliminatoria.setToolTip("Eliminatoria del partido")
        self.ui.spin_goles_local.setToolTip("Goles del equipo local")
        self.ui.spin_goles_visitante.setToolTip("Goles del equipo visitante")