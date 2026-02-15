from typing import List
from models.gol_partido import GolPartido
from models.partido import Partido
from models.participante import Participante
from models.gol_partido import GolPartido
from models.tarjeta_partido import TarjetaPartido
from PySide6.QtSql import QSqlQuery

class ResultadoController:
    
    @staticmethod
    def obtener_partidos_pendientes():
        partidos=[]
        query=QSqlQuery()
        query.exec("SELECT id, equipo_local_id, equipo_visitante_id, arbitro_id, fecha, hora, eliminatoria, goles_local, goles_visitante, jugado FROM partidos WHERE jugado = 0")

        while query.next():
            partido=Partido(
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3),
                query.value(4),
                query.value(5),
                query.value(6),
                query.value(7),
                query.value(8),
                query.value(9)
            )
            partidos.append(partido)

        return partidos

    @staticmethod
    def registrar_gol(partido_id, jugador_id, minuto):
        if not jugador_id:
            return False, "Debes seleccionar un jugador"

        if GolPartido.crear(partido_id, jugador_id, minuto):
            ResultadoController.actualizar_estadisticas_jugador(jugador_id)  
            return True, "Gol registrado correctamente"

        return False, "Error al registrar el gol"
    
    @staticmethod
    def registrar_tarjeta(partido_id,jugador_id,tipo,minuto):
        if not jugador_id:
            return False, "Debes seleccionar un jugador"

        if TarjetaPartido.crear(partido_id,jugador_id,tipo,minuto):
            ResultadoController.actualizar_estadisticas_jugador(jugador_id)
            return True, "Tarjeta registrada correctamente"

        return False, "Error al registrar la tarjeta"

    @staticmethod
    def actualizar_estadisticas_jugador(jugador_id):
        query = QSqlQuery()
        query.prepare("SELECT COUNT(*) FROM goles_partido WHERE jugador_id = ?")
        query.addBindValue(jugador_id)
        query.exec()
        goles = 0
        if query.next():
            goles = query.value(0)

        query.prepare("SELECT COUNT(*) FROM tarjetas_partido WHERE jugador_id = ? AND tipo = 'amarilla'")
        query.addBindValue(jugador_id)
        query.exec()
        tarjetas_amarillas = 0
        if query.next():
            tarjetas_amarillas = query.value(0)
        
        query.prepare("SELECT COUNT(*) FROM tarjetas_partido WHERE jugador_id = ? AND tipo = 'roja'")
        query.addBindValue(jugador_id)
        query.exec()
        tarjetas_rojas = 0
        if query.next():
            tarjetas_rojas = query.value(0)

        query.prepare("UPDATE participantes SET goles = ?, t_amarillas = ?, t_rojas = ? WHERE id = ?")
        query.addBindValue(goles)
        query.addBindValue(tarjetas_amarillas)
        query.addBindValue(tarjetas_rojas)
        query.addBindValue(jugador_id)
        query.exec()

    @staticmethod
    def actualizar_resultado_partido(partido_id):
        partido=Partido.obtener_por_id(partido_id)

        if not partido:
            return False, "Partido no encontrado"

        goles_local=0

        goles=GolPartido.obtener_por_partido(partido_id)
        for gol in goles:
            jugador=Participante.obtener_por_id(gol.jugador_id)
            if jugador and jugador.equipo_id== partido.equipo_local_id:
                goles_local+=1

        goles_visitante= len(goles)-goles_local

        query = QSqlQuery()
        query.prepare("UPDATE partidos SET goles_local = ?, goles_visitante = ? WHERE id = ?")
        query.addBindValue(goles_local)
        query.addBindValue(goles_visitante)
        query.addBindValue(partido_id)

        if query.exec():
            return True, "Resultado actualizado"
        return False, "Error al actualizar resultado"

    @staticmethod
    def finalizar_partido(partido_id):
        ResultadoController.actualizar_resultado_partido(partido_id)
        
        partido = Partido.obtener_por_id(partido_id)
        if not partido:
            return False, "Partido no encontrado"
        
        if partido.goles_local == partido.goles_visitante:
            return False, "No puede haber empate en eliminatorias. Debe haber un ganador."

        query = QSqlQuery()
        query.prepare("UPDATE partidos SET jugado = 1 WHERE id = ?")
        query.addBindValue(partido_id)
        
        if query.exec():
            return True, "Partido marcado como jugado"
        return False, "Error al finalizar el partido"

    @staticmethod
    def obtener_goles_partido(partido_id):
        return GolPartido.obtener_por_partido(partido_id)
    
    @staticmethod
    def obtener_tarjetas_partido(partido_id):
        return TarjetaPartido.obtener_por_partido(partido_id)
    
    @staticmethod
    def eliminar_gol(gol_id, jugador_id):
        if GolPartido.eliminar(gol_id):
            ResultadoController.actualizar_estadisticas_jugador(jugador_id)
            return True, "Gol eliminado"
        return False, "Error al eliminar gol"
    
    @staticmethod
    def eliminar_tarjeta(tarjeta_id, jugador_id):
        if TarjetaPartido.eliminar(tarjeta_id):
            ResultadoController.actualizar_estadisticas_jugador(jugador_id)
            return True, "Tarjeta eliminada"
        return False, "Error al eliminar tarjeta"
