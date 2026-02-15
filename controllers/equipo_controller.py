from models.equipo import Equipo
from PySide6.QtWidgets import QMessageBox

class EquipoController:
    @staticmethod
    def crear_equipo(nombre, curso, color_camiseta, escudo):
        if not nombre or not curso:
            return False, "EL nombre y el curso son obligatorios"

        if Equipo.crear(nombre, curso,color_camiseta,escudo):
            return True, "Equipo creado exitosamente"
        return False, "Error al crear equipo"
    
    @staticmethod
    def obtener_todos():
        return Equipo.obtener_todos()
    
    @staticmethod
    def obtener_por_id(id):
        return Equipo.obtener_por_id(id)

    @staticmethod
    def actualizar_equipo(id,nombre,curso,color_camiseta,escudo):
        if not nombre or not curso:
            return False, "El nombre y el curso son obligatorios"
        
        if Equipo.actualizar(id,nombre,curso,color_camiseta,escudo):
            return True, "Equipo actualizado correctamente"
        
        return False, "Error al actualizar equipo"
    
    @staticmethod
    def eliminar_equipo(id):
        if Equipo.eliminar(id):
            return True, "Equipo eliminado correctamente"
        
        return False, "Error al eliminar el equipo"