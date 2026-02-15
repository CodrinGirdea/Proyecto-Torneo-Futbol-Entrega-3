from models.partido import Partido
from models.equipo import Equipo
from models.participante import Participante

class PartidoController:
    
    @staticmethod
    def crear_partido(equipo_local_id, equipo_visitante_id, arbitro_id, fecha, hora, eliminatoria, goles_local, goles_visitante, jugado):
        if not equipo_local_id or not equipo_visitante_id:
            return False, "Debes seleccionar ambos equipos"

        if equipo_local_id==equipo_visitante_id:
            return False, "Un equipo no puede jugar contra sí mismo"

        if not arbitro_id:
            return False, "Debe haber un arbitro asignado al partido"

        if not fecha or not hora or not eliminatoria:
            return False, "La fecha, la hora y la eliminatoria son obligatorios"
        
        print(f"[CONTROLADOR] crear_partido llamado")
        print(f"  Equipos: {equipo_local_id} vs {equipo_visitante_id}")

        if Partido.crear(equipo_local_id, equipo_visitante_id, arbitro_id, fecha, hora, eliminatoria, goles_local, goles_visitante, jugado):
            return True, "Partido creado correctamente"
        
        return False, "Error al crear el partido"

    @staticmethod
    def obtener_todos_partidos():
        return Partido.obtener_todos()

    @staticmethod
    def obtener_partido_por_id(id):
        return Partido.obtener_por_id(id)

    def obtener_partidos_por_eliminatoria(eliminatoria):
        return Partido.obtener_por_eliminatoria(eliminatoria)
    
    @staticmethod
    def actualizar_partido(id,equipo_local_id, equipo_visitante_id, arbitro_id, fecha, hora, eliminatoria, goles_local, goles_visitante, jugado):
        if not equipo_local_id or not equipo_visitante_id:
            return False, "Debes seleccionar ambos equipos"

        if equipo_local_id==equipo_visitante_id:
            return False, "Un equipo no puede jugar contra sí mismo"

        if not arbitro_id:
            return False, "Debe haber un arbitro asignado al partido"

        if not fecha or not hora or not eliminatoria:
            return False, "La fecha, la hora y la eliminatoria son obligatorios"

        if goles_local==goles_visitante:
            return False, "No puede haber empate, debe haber un ganador"
        
        if Partido.actualizar(id,equipo_local_id, equipo_visitante_id, arbitro_id, fecha, hora, eliminatoria, goles_local, goles_visitante, jugado):
            return True, "Partido actualizado correctamente"
        
        return False, "Error al actualizar el partido"
    
    @staticmethod
    def eliminar_partido(id):
        if Partido.eliminar(id):
            return True, "Partido eliminado correctamente"

        return False, "Error al eliminar el partido"

    @staticmethod
    def obtener_todos_los_equipos():
        return Equipo.obtener_todos()
    
    def obtener_arbitros():
        return Participante.obtener_arbitros()