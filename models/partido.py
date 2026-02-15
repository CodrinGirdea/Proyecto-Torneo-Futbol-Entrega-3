from PySide6.QtSql import QSqlQuery

class Partido:
    def __init__(self,id,equipo_local_id,equipo_visitante_id,arbitro_id,fecha,hora,eliminatoria,goles_local,goles_visitante,jugado):
        self.id=id
        self.equipo_local_id=equipo_local_id
        self.equipo_visitante_id=equipo_visitante_id
        self.arbitro_id=arbitro_id
        self.fecha=fecha
        self.hora=hora
        self.eliminatoria=eliminatoria
        self.goles_local=goles_local
        self.goles_visitante=goles_visitante
        self.jugado=jugado

    @staticmethod
    def crear(equipo_local_id,equipo_visitante_id,arbitro_id,fecha,hora,eliminatoria,goles_local,goles_visitante,jugado):
        print(f"[MODELO] Creando partido:")
        print(f"  Local: {equipo_local_id}, Visitante: {equipo_visitante_id}")
        print(f"  Árbitro: {arbitro_id}, Fecha: {fecha}, Hora: {hora}")
        query=QSqlQuery()
        query.prepare("INSERT INTO partidos (equipo_local_id,equipo_visitante_id,arbitro_id,fecha,hora,eliminatoria,goles_local,goles_visitante,jugado) VALUES (?,?,?,?,?,?,?,?,?)")

        query.addBindValue(equipo_local_id)
        query.addBindValue(equipo_visitante_id)
        query.addBindValue(arbitro_id)
        query.addBindValue(fecha)
        query.addBindValue(hora)
        query.addBindValue(eliminatoria)
        query.addBindValue(goles_local)
        query.addBindValue(goles_visitante)
        query.addBindValue(jugado)

        resultado= query.exec()

        print(f"[MODELO] query.exec() devolvió: {resultado}")
        print(f"[MODELO] Último ID insertado: {query.lastInsertId()}")
        if not resultado:
            print(f"[MODELO] Error SQL: {query.lastError().text()}")

        return resultado

    @staticmethod
    def obtener_todos():
        partidos=[]
        query=QSqlQuery()
        query.exec("SELECT id,equipo_local_id,equipo_visitante_id,arbitro_id,fecha,hora,eliminatoria,goles_local,goles_visitante,jugado FROM partidos")

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
    def obtener_por_id(id):
        query=QSqlQuery()
        query.prepare("SELECT id,equipo_local_id,equipo_visitante_id,arbitro_id,fecha,hora,eliminatoria,goles_local,goles_visitante,jugado FROM partidos WHERE id=?")
        query.addBindValue(id)

        query.exec()

        if query.next():
            return Partido(
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

        return None

    @staticmethod
    def obtener_por_eliminatoria(eliminatoria):
        partidos=[]
        query=QSqlQuery()
        query.prepare("SELECT id,equipo_local_id,equipo_visitante_id,arbitro_id,fecha,hora,eliminatoria,goles_local,goles_visitante,jugado FROM partidos WHERE eliminatoria=?")
        query.addBindValue(eliminatoria)
        query.exec()

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
    def actualizar(id,equipo_local_id,equipo_visitante_id,arbitro_id,fecha,hora,eliminatoria,goles_local,goles_visitante,jugado):
        query=QSqlQuery()
        query.prepare("UPDATE partidos SET equipo_local_id=?, equipo_visitante_id=?, arbitro_id=?, fecha=?, hora=?, eliminatoria=?, goles_local=?, goles_visitante=?, jugado=? WHERE id=?")
        query.addBindValue(equipo_local_id)
        query.addBindValue(equipo_visitante_id)
        query.addBindValue(arbitro_id)
        query.addBindValue(fecha)
        query.addBindValue(hora)
        query.addBindValue(eliminatoria)
        query.addBindValue(goles_local)
        query.addBindValue(goles_visitante)
        query.addBindValue(jugado)
        query.addBindValue(id)

        return query.exec()

    @staticmethod
    def eliminar(id):
        query=QSqlQuery()
        query.prepare("DELETE FROM partidos WHERE id=?")
        query.addBindValue(id)

        return query.exec()