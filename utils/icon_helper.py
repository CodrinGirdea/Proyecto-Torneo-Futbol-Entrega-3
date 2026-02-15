import os
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, Qt

def get_icon_path(icon_name):
    base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    icon_path=os.path.join(base_path,"resources","iconos",icon_name)
    return icon_path

def set_button_icon(button, icon_name, size=24):
    icon_path=get_icon_path(icon_name)
    if os.path.exists(icon_path):
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(size,size))
    else:
        print(f"Icono no encontrado: {icon_path}")