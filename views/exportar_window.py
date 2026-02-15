from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from views.ui_exportar_window import Ui_ExportarWindow
from controllers.exportar_controller import ExportController
from utils.icon_helper import set_button_icon



class ExportarWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ExportarWindow()
        self.ui.setupUi(self)
        
        self.setup_icons()

        self.ui.btn_clasificacion.clicked.connect(self.exportar_clasificacion)
        self.ui.btn_goleadores.clicked.connect(self.exportar_goleadores)
        self.ui.btn_tarjetas.clicked.connect(self.exportar_tarjetas)
        self.ui.btn_partidos_jugados.clicked.connect(self.exportar_partidos_jugados)
        self.ui.btn_calendario.clicked.connect(self.exportar_calendario)
        self.ui.btn_jugadores.clicked.connect(self.exportar_jugadores)
        self.ui.btn_volver.clicked.connect(self.close)
    
    
    def setup_icons(self):
        set_button_icon(self.ui.btn_clasificacion, "clasificacion_ex.png", 20)
        set_button_icon(self.ui.btn_goleadores, "goleadores.png", 20)
        set_button_icon(self.ui.btn_tarjetas, "tarjetas.png", 20)
        set_button_icon(self.ui.btn_partidos_jugados, "partidos_completados.png", 20)
        set_button_icon(self.ui.btn_calendario, "calendario_ex.png",20)
        set_button_icon(self.ui.btn_jugadores, "jugadores.png", 20)
        set_button_icon(self.ui.btn_volver, "volver.png", 20)


    
    def exportar_clasificacion(self):
        ruta, _ = QFileDialog.getSaveFileName(self,"Guardar Clasificación",ExportController.obtener_ruta_exportacion("clasificacion_torneo"),"Archivos CSV (*.csv)")
        
        if ruta:
            if not ruta.endswith('.csv'):
                ruta += '.csv'
            
            exito, mensaje = ExportController.exportar_clasificacion(ruta)
            self.mostrar_resultado(exito, mensaje)
    
    def exportar_goleadores(self):
        ruta, _ = QFileDialog.getSaveFileName(self,"Guardar Goleadores",ExportController.obtener_ruta_exportacion("goleadores_torneo"),"Archivos CSV (*.csv)")
        
        if ruta:
            if not ruta.endswith('.csv'):
                ruta += '.csv'
            
            exito, mensaje = ExportController.exportar_goleadores(ruta)
            self.mostrar_resultado(exito, mensaje)
    
    def exportar_tarjetas(self):
        """Exporta las estadísticas de tarjetas"""
        ruta, _ = QFileDialog.getSaveFileName(self,"Guardar Tarjetas",ExportController.obtener_ruta_exportacion("tarjetas_torneo"),"Archivos CSV (*.csv)")
        
        if ruta:
            if not ruta.endswith('.csv'):
                ruta += '.csv'
            
            exito, mensaje = ExportController.exportar_tarjetas(ruta)
            self.mostrar_resultado(exito, mensaje)
    
    def exportar_partidos_jugados(self):
        ruta, _ = QFileDialog.getSaveFileName(self,"Guardar Partidos Jugados",ExportController.obtener_ruta_exportacion("partidos_jugados"),"Archivos CSV (*.csv)")
        
        if ruta:
            if not ruta.endswith('.csv'):
                ruta += '.csv'
            
            exito, mensaje = ExportController.exportar_partidos_jugados(ruta)
            self.mostrar_resultado(exito, mensaje)
    
    def exportar_calendario(self):
        """Exporta el calendario completo de partidos"""
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar Calendario Completo",
            ExportController.obtener_ruta_exportacion("calendario_completo"),
            "Archivos CSV (*.csv)"
        )
        
        if ruta:
            if not ruta.endswith('.csv'):
                ruta += '.csv'
            
            exito, mensaje = ExportController.exportar_calendario_completo(ruta)
            self.mostrar_resultado(exito, mensaje)
    
    def exportar_jugadores(self):
        """Exporta la lista de jugadores con estadísticas"""
        ruta, _ = QFileDialog.getSaveFileName(self,"Guardar Jugadores",ExportController.obtener_ruta_exportacion("jugadores_torneo"),"Archivos CSV (*.csv)")
        
        if ruta:
            if not ruta.endswith('.csv'):
                ruta += '.csv'
            
            exito, mensaje = ExportController.exportar_jugadores(ruta)
            self.mostrar_resultado(exito, mensaje)
    
    def mostrar_resultado(self, exito, mensaje):
        if exito:
            QMessageBox.information(self,"Exportación Exitosa", "Exito al exportar")
        else:
            QMessageBox.critical(self,"Error en la Exportación",mensaje)
    
    