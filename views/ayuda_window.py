from PySide6.QtWidgets import QWidget
from views.ui_ayuda_window import Ui_Form

class AyudaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Ayuda")
        
        # Conectar botón cerrar
        self.ui.btn_cerrar.clicked.connect(self.close)