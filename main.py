import sys, os
from PySide6.QtWidgets import QApplication
from models.database import conectar
from views.main_window import MainWindow

def get_data_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.dirname(os.path.abspath(__file__))


def load_stylesheet(ruta_qss):
    try:
        ruta_completa = os.path.join(get_data_path(), ruta_qss)
        with open(ruta_completa, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("No se encontró el archivo QSS:", ruta_completa)
        return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = conectar()
    qss = load_stylesheet("resources/qss/style.qss")
    app.setStyleSheet(qss)
    
    # Crear y mostrar la ventana principal
    ventana = MainWindow()
    ventana.show()
    
    sys.exit(app.exec())