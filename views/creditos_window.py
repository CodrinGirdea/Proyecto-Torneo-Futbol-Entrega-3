from PySide6.QtWidgets import QWidget
from views.ui_creditos_window import Ui_Creditos

class CreditosWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Creditos()
        self.ui.setupUi(self)

        self.setWindowTitle("Créditos")
        
        self.ui.btn_cerrar.clicked.connect(self.close)