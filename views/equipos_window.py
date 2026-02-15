from PySide6.QtWidgets import QTableWidgetSelectionRange
from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog, QTableWidgetItem
from PySide6.QtCore import QByteArray
from views.ui_equipos_window import Ui_Form
from controllers.equipo_controller import EquipoController
from utils.icon_helper import set_button_icon

class EquiposWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui= Ui_Form()
        self.ui.setupUi(self)

        self.setup_icons()
        
        self.setup_tooltips()

        self.equipo_seleccionado_id=None
        self.escudo_bytes = None

        self.ui.btn_crear.clicked.connect(self.crear_equipo)
        self.ui.btn_actualizar.clicked.connect(self.actualizar_equipo)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_equipo)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.ui.btn_volver.clicked.connect(self.close)
        self.ui.btn_seleccionar_escudo.clicked.connect(self.seleccionar_escudo)
        
        self.ui.table_equipos.itemSelectionChanged.connect(self.cargar_equipo_seleccionado)
        
        self.cargar_equipos()

    def cargar_equipos(self):
        equipos = EquipoController.obtener_todos()
        table = self.ui.table_equipos

        table.setRowCount(0)
        table.setColumnCount(4)

        for equipo in equipos:
            row = table.rowCount()
            table.insertRow(row)

            table.setItem(row, 0, QTableWidgetItem(str(equipo.id)))
            table.setItem(row, 1, QTableWidgetItem(equipo.nombre))
            table.setItem(row, 2, QTableWidgetItem(equipo.curso))
            table.setItem(row, 3, QTableWidgetItem(equipo.color_camiseta))

    def cargar_equipo_seleccionado(self):
        """Carga los datos del equipo seleccionado en el formulario"""
        selected_items = self.ui.table_equipos.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            self.equipo_seleccionado_id = int(self.ui.table_equipos.item(row, 0).text())
            
            equipo = EquipoController.obtener_por_id(self.equipo_seleccionado_id)
            if equipo:
                self.ui.input_nombre.setText(equipo.nombre)
                self.ui.input_curso.setText(equipo.curso)
                self.ui.input_color.setText(equipo.color_camiseta or "")
                
                if equipo.escudo and len(equipo.escudo) > 0:
                    self.escudo_bytes = equipo.escud
                    self.ui.input_escudo.setText(f"Imagen cargada ({len(equipo.escudo)} bytes)")
                else:
                    self.escudo_bytes = None
                    self.ui.input_escudo.setText("")

    def crear_equipo(self):
        nombre=self.ui.input_nombre.text().strip()
        curso=self.ui.input_curso.text().strip()
        color_camiseta=self.ui.input_color.text().strip()
        escudo=self.ui.input_escudo.text().strip()

        estado,mensaje=EquipoController.crear_equipo(nombre,curso,color_camiseta,escudo)

        if estado:
            QMessageBox.information(self,"Éxito",mensaje)
            self.limpiar_campos()
            self.cargar_equipos()
        else:
            QMessageBox.warning(self,"Error",mensaje)

    def actualizar_equipo(self):
        """Actualiza el equipo seleccionado"""
        if not self.equipo_seleccionado_id:
            QMessageBox.warning(self, "Advertencia", "Selecciona un equipo de la tabla")
            return
        
        nombre = self.ui.input_nombre.text().strip()
        curso = self.ui.input_curso.text().strip()
        color = self.ui.input_color.text().strip()
        
        estado, mensaje = EquipoController.actualizar_equipo(self.equipo_seleccionado_id,nombre,curso,color,self.escudo_bytes)
        
        if estado:
            QMessageBox.information(self, "Éxito", mensaje)
            self.limpiar_campos()
            self.cargar_equipos()
        else:
            QMessageBox.warning(self, "Error", mensaje)

    def eliminar_equipo(self):
        if not self.equipo_seleccionado_id:
            QMessageBox.warning(self, "Advertencia", "Selecciona un equipo de la tabla")
            return
        
        respuesta=QMessageBox.question(self,"Confirmación","¿Estás seguro de eliminar este equipo?",QMessageBox.Yes | QMessageBox.No)

        if respuesta==QMessageBox.Yes:
            estado,mensaje=EquipoController.eliminar_equipo(self.equipo_seleccionado_id)

            if estado:
                QMessageBox.information(self, "Éxito", mensaje)
                self.limpiar_campos()
                self.cargar_equipos()
            else:
                QMessageBox.warning(self, "Error", mensaje)
    
    def limpiar_campos(self):
        self.ui.input_nombre.clear()
        self.ui.input_curso.clear()
        self.ui.input_color.clear()
        self.ui.input_escudo.clear()
        self.equipo_seleccionado_id=None
        self.escudo_bytes = None

    def seleccionar_escudo(self):
        """Abre un diálogo para seleccionar la imagen del escudo"""
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Escudo", "","Imágenes (*.png *.jpg *.jpeg *.bmp)")
        if archivo:
            try:
                with open(archivo, 'rb') as f:
                    imagen_data = f.read()
                    self.escudo_bytes = QByteArray(imagen_data)
                    
                    self.ui.input_escudo.setText(f"Imagen cargada ({len(imagen_data)} bytes)")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo cargar la imagen: {str(e)}")

    def setup_icons(self):
        """Configura los iconos de los botones"""
        set_button_icon(self.ui.btn_crear, "crear.png", 20)
        set_button_icon(self.ui.btn_actualizar, "editar.png", 20)
        set_button_icon(self.ui.btn_eliminar, "eliminar.png", 20)
        set_button_icon(self.ui.btn_limpiar, "limpiar.png", 20)
        set_button_icon(self.ui.btn_volver, "volver.png", 20)
        set_button_icon(self.ui.btn_seleccionar_escudo, "imagen.png", 20)
    
    def setup_tooltips(self):
        """Configura los tooltips"""
        self.ui.btn_crear.setToolTip("Crear un nuevo equipo")
        self.ui.btn_actualizar.setToolTip("Actualizar el equipo seleccionado")
        self.ui.btn_eliminar.setToolTip("Eliminar el equipo seleccionado")
        self.ui.btn_limpiar.setToolTip("Limpiar todos los campos del formulario")
        self.ui.btn_volver.setToolTip("Volver al menú principal")
        self.ui.btn_seleccionar_escudo.setToolTip("Seleccionar imagen del escudo")
        
        self.ui.input_nombre.setToolTip("Nombre del equipo")
        self.ui.input_curso.setToolTip("Curso al que pertenece el equipo")
        self.ui.input_color.setToolTip("Color de la camiseta del equipo")
        self.ui.input_escudo.setToolTip("Ruta o información del escudo cargado")