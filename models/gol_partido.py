from PySide6.QtSql import QSqlQuery

class GolPartido:
    def __init__(self,id,partido_id,jugador_id,minuto):
        self.id=id
        self.partido_id=partido_id
        self.jugador_id=jugador_id
        self.minuto=minuto

    @staticmethod
    def crear (partido_id,jugador_id,minuto):
        query=QSqlQuery()
        query.prepare("INSERT INTO goles_partido (partido_id,jugador_id,minuto) VALUES (?,?,?)")

        query.addBindValue(partido_id)
        query.addBindValue(jugador_id)
        query.addBindValue(minuto)

        return query.exec()

    @staticmethod
    def obtener_por_partido(partido_id):
        goles=[]
        query=QSqlQuery()
        query.prepare("SELECT id, partido_id, jugador_id, minuto FROM goles_partido WHERE partido_id= ?")

        query.addBindValue(partido_id)
        query.exec()

        while query.next():
            gol= GolPartido(
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3)
            )
            goles.append(gol)

        return goles

    @staticmethod
    def eliminar(id):
        query=QSqlQuery()
        query.prepare("DELETE FROM goles_partido WHERE id=?")

        query.addBindValue(id)

        return query.exec()