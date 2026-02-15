from models.participante import Participante
from models.equipo import Equipo

class ParticipanteController:

    @staticmethod
    def crear_participante(nombre,fecha_nacimiento,curso,es_jugador,es_arbitro,posicion,equipo_id,t_amarillas,t_rojas,goles):
        if not nombre or not fecha_nacimiento or not curso:
            return False,"Nombre, fecha de nacimiento y curso son campos obligatorios"

        if not es_jugador and not es_arbitro:
            return False,"El participante debe ser arbitro, jugador o ambos"

        if es_jugador and not equipo_id:
            return False,"El participante debe estar en algun equipo"
        
        if not es_jugador:
            equipo_id=None
        
        if Participante.crear(nombre,fecha_nacimiento,curso,es_jugador,es_arbitro,posicion,equipo_id,t_amarillas,t_rojas,goles):
            return True,"Participante creado con exito"
        
        return False,"Error al crear el participante"

    @staticmethod
    def actualizar_participante(id,nombre,fecha_nacimiento,curso,es_jugador,es_arbitro,posicion,equipo_id,t_amarillas,t_rojas,goles):
        if not nombre or not fecha_nacimiento or not curso:
            return False,"Nombre, fecha de nacimiento y curso son campos obligatorios"

        if not es_jugador and not es_arbitro:
            return False,"El participante debe ser arbitro, jugador o ambos"

        if es_jugador and not equipo_id:
            return False,"El participante debe estar en algun equipo"
        
        if not es_jugador:
            equipo_id=None
        
        if Participante.actualizar(id,nombre,fecha_nacimiento,curso,es_jugador,es_arbitro,posicion,equipo_id,t_amarillas,t_rojas,goles):
            return True,"Participante acualizado con exito"
        
        return False,"Error al actualizar el participante"

    @staticmethod
    def obtener_todos_participantes():
        return Participante.obtener_todos()

    @staticmethod
    def obtener_participantes_por_equipo(equipo_id):
        return Participante.obtener_por_equipo(equipo_id)

    @staticmethod
    def obtener_participante_por_id(participante_id):
        return Participante.obtener_por_id(participante_id)

    @staticmethod
    def obtener_partidos_por_equipo(equipo_id):
        return Participante.obtener_por_equipo(equipo_id)
    
    @staticmethod
    def obtener_todos_por_equipo(equipo_id):
        return Participante.obtener_por_equipo(equipo_id)

    @staticmethod
    def obtener_arbitros():
        return Participante.obtener_arbitros()

    @staticmethod
    def eliminar_participante(participante_id):
        if Participante.eliminar(participante_id):
            return True,"Participante eliminado correctamente"

        return False,"Error al eliminar el participante"

    @staticmethod
    def obtener_todos_equipos():
        return Equipo.obtener_todos()

    