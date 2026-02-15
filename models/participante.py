from PySide6.QtSql import QSqlQuery

class Participante:
    def __init__(self, id, nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.curso = curso
        self.es_jugador = es_jugador
        self.es_arbitro = es_arbitro
        self.posicion = posicion
        self.equipo_id = equipo_id
        self.t_amarillas = t_amarillas
        self.t_rojas = t_rojas
        self.goles = goles

    @staticmethod
    def crear(nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles):
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO participantes (nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """)
        query.addBindValue(nombre)
        query.addBindValue(fecha_nacimiento)
        query.addBindValue(curso)
        query.addBindValue(es_jugador)
        query.addBindValue(es_arbitro)
        query.addBindValue(posicion)
        query.addBindValue(equipo_id)
        query.addBindValue(t_amarillas)
        query.addBindValue(t_rojas)
        query.addBindValue(goles)
        return query.exec()

    @staticmethod
    def obtener_todos():
        participantes = []
        query = QSqlQuery()
        query.exec("SELECT id, nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles FROM participantes")
        while query.next():
            participante = Participante(
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3),
                query.value(4),
                query.value(5),
                query.value(6),
                query.value(7),
                query.value(8) or 0,
                query.value(9) or 0,
                query.value(10) or 0
            )
            participantes.append(participante)
        return participantes

    @staticmethod
    def obtener_por_id(id):
        query = QSqlQuery()
        query.prepare("SELECT id, nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles FROM participantes WHERE id = ?")
        query.addBindValue(id)
        query.exec()
        if query.next():
            return Participante(
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3),
                query.value(4),
                query.value(5),
                query.value(6),
                query.value(7),
                query.value(8),
                query.value(9),
                query.value(10)
            )
        return None

    @staticmethod
    def obtener_por_equipo(equipo_id):
        participantes = []
        query = QSqlQuery()
        query.prepare("SELECT id, nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles FROM participantes WHERE equipo_id = ?")
        query.addBindValue(equipo_id)
        query.exec()
        while query.next():
            participante = Participante(
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3),
                query.value(4),
                query.value(5),
                query.value(6),
                query.value(7),
                query.value(8),
                query.value(9),
                query.value(10)
            )
            participantes.append(participante)
        return participantes

    @staticmethod
    def obtener_arbitros():
        arbitros = []
        query = QSqlQuery()
        query.exec("SELECT id, nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles FROM participantes WHERE es_arbitro = 1")
        while query.next():
            arbitro = Participante(
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3),
                query.value(4),
                query.value(5),
                query.value(6),
                query.value(7),
                query.value(8),
                query.value(9),
                query.value(10)
            )
            arbitros.append(arbitro)
        return arbitros

    @staticmethod
    def actualizar(id, nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles):
        query = QSqlQuery()
        query.prepare("UPDATE participantes SET nombre = ?, fecha_nacimiento = ?, curso = ?, es_jugador = ?, es_arbitro = ?, posicion = ?, equipo_id = ?, t_amarillas = ?, t_rojas = ?, goles = ? WHERE id = ?")
        query.addBindValue(nombre)
        query.addBindValue(fecha_nacimiento)
        query.addBindValue(curso)
        query.addBindValue(es_jugador)
        query.addBindValue(es_arbitro)
        query.addBindValue(posicion)
        query.addBindValue(equipo_id)
        query.addBindValue(t_amarillas)
        query.addBindValue(t_rojas)
        query.addBindValue(goles)
        query.addBindValue(id)
        return query.exec()

    @staticmethod
    def eliminar(id):
        query = QSqlQuery()
        query.prepare("DELETE FROM participantes WHERE id = ?")
        query.addBindValue(id)
        return query.exec()