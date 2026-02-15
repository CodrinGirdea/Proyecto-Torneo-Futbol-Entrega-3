from PySide6.QtWidgets import QWidget,QMessageBox,QTableWidgetItem,QTableWidget
from PySide6.QtCore import QDate
from views.ui_participantes_window import Ui_Gestion_de_participantes
from controllers.participante_controller import ParticipanteController  
from utils.icon_helper import set_button_icon

class ParticipantesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Gestion_de_participantes()
        self.ui.setupUi(self)

        self.setup_icons()

        self.setup_tooltips()

        self.setWindowTitle("Gestion de participantes")

        self.participante_seleccionado_id=None

        self.ui.input_fecha_nac.setDate(QDate.currentDate())

        self.ui.btn_crear.clicked.connect(self.crear_participante)
        self.ui.btn_actualizar.clicked.connect(self.actualizar_participante)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_participante)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.ui.btn_volver.clicked.connect(self.close)

        self.ui.check_es_jugador.stateChanged.connect(self.actualizar_campos_jugador)

        self.ui.table_participantes.itemSelectionChanged.connect(self.cargar_participante_seleccionado)
        self.ui.table_participantes.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.cargar_equipos()
        self.cargar_participantes()

    def cargar_equipos(self):
        self.ui.combo_equipo.clear()

        self.ui.combo_equipo.addItem("Seleccionar equipo",None)

        equipos=ParticipanteController.obtener_todos_equipos()

        for equipo in equipos:
            self.ui.combo_equipo.addItem(equipo.nombre,equipo.id)

    def cargar_participantes(self):
        participantes=ParticipanteController.obtener_todos_participantes()
        self.ui.table_participantes.setRowCount(0)

        for participante in participantes:
            row=self.ui.table_participantes.rowCount()

            self.ui.table_participantes.insertRow(row)

            tipo=""

            if participante.es_jugador and participante.es_arbitro:
                tipo="Jugador/Arbitro"
            elif participante.es_jugador:
                tipo="Jugador"
            else:
                tipo="Arbitro"

            nombre_equipo=""

            if participante.equipo_id:
                equipos=ParticipanteController.obtener_todos_equipos()
                for equipo in equipos:
                    if equipo.id == participante.equipo_id:
                        nombre_equipo=equipo.nombre
                        break
            self.ui.table_participantes.setItem(row, 0, QTableWidgetItem(str(participante.id)))
            self.ui.table_participantes.setItem(row, 1, QTableWidgetItem(participante.nombre))
            self.ui.table_participantes.setItem(row, 2, QTableWidgetItem(participante.fecha_nacimiento))
            self.ui.table_participantes.setItem(row, 3, QTableWidgetItem(participante.curso))
            self.ui.table_participantes.setItem(row, 4, QTableWidgetItem(tipo))
            self.ui.table_participantes.setItem(row, 5, QTableWidgetItem(participante.posicion or ""))
            self.ui.table_participantes.setItem(row, 6, QTableWidgetItem(nombre_equipo))
    
    def cargar_participante_seleccionado(self):
        seleccionado=self.ui.table_participantes.selectedItems()

        if seleccionado:
            row=seleccionado[0].row()
            self.participante_seleccionado_id=int(self.ui.table_participantes.item(row,0).text())

            participante=ParticipanteController.obtener_participante_por_id(self.participante_seleccionado_id)

            if participante:
                self.ui.input_nombre.setText(participante.nombre)

                fecha=participante.fecha_nacimiento.split('-')

                if len(fecha)==3:
                    fechaQDate= QDate(int(fecha[0]),int(fecha[1]),int(fecha[2]))
                    self.ui.input_fecha_nac.setDate(fechaQDate)

                self.ui.input_curso.setText(participante.curso)
                self.ui.check_es_arbitro.setChecked(bool(participante.es_arbitro))
                self.ui.check_es_jugador.setChecked(bool(participante.es_jugador))

                indice=self.ui.combo_posicion.findText(participante.posicion or "")
                self.ui.combo_posicion.setCurrentIndex(indice if indice > 0 else 0)

                if participante.equipo_id:
                    for i in range(self.ui.combo_equipo.count()):
                        if self.ui.combo_equipo.itemData(i) == participante.equipo_id:
                            self.ui.combo_equipo.setCurrentIndex(i)
                            break
                else:
                    self.ui.combo_equipo.setCurrentIndex(0)
                
                self.ui.spin_t_amarillas.setValue(participante.t_amarillas)
                self.ui.spin_t_rojas.setValue(participante.t_rojas)
                self.ui.spin_goles.setValue(participante.goles)
    
    def actualizar_campos_jugador(self):
        es_jugador=self.ui.check_es_jugador.isChecked()
        self.ui.combo_posicion.setEnabled(es_jugador)
        self.ui.combo_equipo.setEnabled(es_jugador)

    def crear_participante(self):
        nombre = self.ui.input_nombre.text().strip()
        fecha = self.ui.input_fecha_nac.date().toString("yyyy-MM-dd")
        curso = self.ui.input_curso.text().strip()
        es_jugador = 1 if self.ui.check_es_jugador.isChecked() else 0
        es_arbitro = 1 if self.ui.check_es_arbitro.isChecked() else 0
        posicion = self.ui.combo_posicion.currentText() if es_jugador else None
        equipo_id = self.ui.combo_equipo.currentData()
        t_amarillas = self.ui.spin_t_amarillas.value()
        t_rojas = self.ui.spin_t_rojas.value()
        goles = self.ui.spin_goles.value()

        estado,mensaje=ParticipanteController.crear_participante(nombre, fecha, curso, es_jugador, es_arbitro, posicion,equipo_id, t_amarillas, t_rojas, goles)

        if estado:
            QMessageBox.information(self,"Éxito",mensaje)
            self.limpiar_campos()
            self.cargar_participantes()
        else:
            QMessageBox.warning(self,"Error",mensaje)

    def actualizar_participante(self):
        if not self.participante_seleccionado_id:
            QMessageBox.warning(self,"Advertencia","Selecciona un participante")
            return
        
        nombre = self.ui.input_nombre.text().strip()
        fecha = self.ui.input_fecha_nac.date().toString("yyyy-MM-dd")
        curso = self.ui.input_curso.text().strip()
        es_jugador = 1 if self.ui.check_es_jugador.isChecked() else 0
        es_arbitro = 1 if self.ui.check_es_arbitro.isChecked() else 0
        posicion = self.ui.combo_posicion.currentText()
        equipo_id = self.ui.combo_equipo.currentData()
        t_amarillas = self.ui.spin_t_amarillas.value()
        t_rojas = self.ui.spin_t_rojas.value()
        goles = self.ui.spin_goles.value()

        estado,mensaje=ParticipanteController.actualizar_participante(self.participante_seleccionado_id ,nombre, fecha, curso, es_jugador, es_arbitro, posicion,equipo_id, t_amarillas, t_rojas, goles)

        if estado:
            QMessageBox.information(self,"Éxito",mensaje)
            self.limpiar_campos()
            self.cargar_participantes()
        else:
            QMessageBox.warning(self,"Error",mensaje)
        
    def eliminar_participante(self):
        if not self.participante_seleccionado_id:
            QMessageBox.warning(self,"Advertencia","Selecciona un participante")
            return

        respuesta = QMessageBox.question(self, "Confirmar", "¿Estás seguro de eliminar este participante?",QMessageBox.Yes | QMessageBox.No)

        if respuesta == QMessageBox.Yes:
            estado,mensaje=ParticipanteController.eliminar_participante(self.participante_seleccionado_id)

            if estado:
                QMessageBox.information(self,"Éxito",mensaje)
                self.limpiar_campos()
                self.cargar_participantes()
            else:
                QMessageBox.warning(self,"Error",mensaje)

    def limpiar_campos(self):
        self.ui.input_nombre.clear()
        self.ui.input_fecha_nac.setDate(QDate.currentDate())
        self.ui.input_curso.clear()
        self.ui.check_es_jugador.setChecked(False)
        self.ui.check_es_arbitro.setChecked(False)
        self.ui.combo_posicion.setCurrentIndex(0)
        self.ui.combo_equipo.setCurrentIndex(0)
        self.ui.spin_t_amarillas.setValue(0)
        self.ui.spin_t_rojas.setValue(0)
        self.ui.spin_goles.setValue(0)
        self.participante_seleccionado_id = None
    
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
        
        self.ui.input_nombre.setToolTip("Nombre del participante")
        self.ui.input_curso.setToolTip("Curso al que pertenece el participante")
        self.ui.input_fecha_nac.setToolTip("Fecha de nacimiento del participante")
        self.ui.combo_posicion.setToolTip("Posicion dentro del equipo")
        self.ui.combo_equipo.setToolTip("Equipo al que pertence el participante")
        self.ui.spin_t_amarillas.setToolTip("Tarjetas amarillas recibidas")
        self.ui.spin_t_rojas.setToolTip("Tarjetas rojas recibidas")
        self.ui.spin_goles.setToolTip("Goles realizados")

