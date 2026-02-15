from PySide6.QtWidgets import QMainWindow
from views.ui_main_window import Ui_MainWindow
from views.equipos_window import EquiposWindow
from views.participantes_window import ParticipantesWindow
from views.partidos_window import PartidoWindow
from views.creditos_window import CreditosWindow
from views.ayuda_window import AyudaWindow
from views.resultados_window import ResultadoWindow
from views.clasificacion_window import ClasificacionWindow
from views.exportar_window import ExportarWindow
from views.informes_window import InformesWindow
from utils.icon_helper import set_button_icon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_icons()

        self.setup_tooltips()

        self.ui.btn_equipos.clicked.connect(self.abrir_equipos)
        self.ui.btn_participantes.clicked.connect(self.abrir_participantes)
        self.ui.btn_partidos.clicked.connect(self.abrir_partidos)
        self.ui.btn_resultados.clicked.connect(self.abrir_resultados)
        self.ui.btn_clasificacion.clicked.connect(self.abrir_clasificacion)
        self.ui.btn_creditos.clicked.connect(self.abrir_creditos)
        self.ui.btn_ayuda.clicked.connect(self.abrir_ayuda)
        self.ui.btn_exportar.clicked.connect(self.abrir_exportar)
        self.ui.btn_informes.clicked.connect(self.abrir_informes)
        self.ui.btn_salir.clicked.connect(self.salir)
    
    def abrir_equipos(self):
        self.ventana_equipos=EquiposWindow()
        self.ventana_equipos.show()
    
    def abrir_participantes(self):
        self.ventana_participantes=ParticipantesWindow()
        self.ventana_participantes.show()
    
    def abrir_partidos(self):
        self.ventana_partidos=PartidoWindow()
        self.ventana_partidos.show()
    
    def abrir_resultados(self):
        self.resultados_window=ResultadoWindow()
        self.resultados_window.show()
    
    def abrir_clasificacion(self):
        self.clasificacion_window=ClasificacionWindow()
        self.clasificacion_window.show()
    
    def abrir_creditos(self):
        self.ventana_creditos=CreditosWindow()
        self.ventana_creditos.show()
    
    def abrir_ayuda(self):
        self.ayuda_window=AyudaWindow()
        self.ayuda_window.show()
    
    def abrir_exportar(self):
        self.exportar_window=ExportarWindow()
        self.exportar_window.show()
    
    def abrir_informes(self):
        self.informes_window = InformesWindow()
        self.informes_window.show()

    def salir(self):
        self.close()

    def setup_icons(self):
        set_button_icon(self.ui.btn_equipos, "equipo.png", 32)
        set_button_icon(self.ui.btn_participantes, "participante.png", 32)
        set_button_icon(self.ui.btn_partidos, "partido.png", 32)
        set_button_icon(self.ui.btn_resultados, "resultados.png", 32)
        set_button_icon(self.ui.btn_clasificacion, "clasificacion.png", 32)
        set_button_icon(self.ui.btn_creditos, "creditos.png", 32)
        set_button_icon(self.ui.btn_ayuda, "ayuda.png", 32)
        set_button_icon(self.ui.btn_exportar, "datos.png", 32)
        set_button_icon(self.ui.btn_informes, "datos.png", 32)
        set_button_icon(self.ui.btn_salir, "volver.png", 32)
    
    def setup_tooltips(self):
        """Configura los tooltips de los botones"""
        self.ui.btn_equipos.setToolTip("Crear, editar y eliminar equipos del torneo")
        self.ui.btn_participantes.setToolTip("Gestionar jugadores y árbitros")
        self.ui.btn_partidos.setToolTip("Programar y gestionar partidos")
        self.ui.btn_resultados.setToolTip("Registrar goles y tarjetas de los partidos")
        self.ui.btn_clasificacion.setToolTip("Ver el bracket de eliminatorias")
        self.ui.btn_creditos.setToolTip("Información sobre el programa")
        self.ui.btn_ayuda.setToolTip("Ayuda para usar la aplicación")
        self.ui.btn_exportar.setToolTip("Exportar datos sobre el torneo")
        self.ui.btn_informes.setToolTip("Exportar datos sobre el torneo en PDF")
        self.ui.btn_salir.setToolTip("Cerrar la aplicación")