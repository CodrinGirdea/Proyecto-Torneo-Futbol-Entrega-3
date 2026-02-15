from PySide6.QtSql import QSqlQuery

class TarjetaPartido:
    def __init__(self, id, partido_id, jugador_id, tipo, minuto):
        self.id = id
        self.partido_id = partido_id
        self.jugador_id = jugador_id
        self.tipo = tipo
        self.minuto = minuto
    
    @staticmethod
    def crear(partido_id, jugador_id, tipo, minuto):
        query = QSqlQuery()
        query.prepare("INSERT INTO tarjetas_partido (partido_id, jugador_id, tipo, minuto) VALUES (?, ?, ?, ?)")
        query.addBindValue(partido_id)
        query.addBindValue(jugador_id)
        query.addBindValue(tipo)
        query.addBindValue(minuto)
        
        return query.exec()
    
    @staticmethod
    def obtener_por_partido(partido_id):
        tarjetas = []
        query = QSqlQuery()
        query.prepare("SELECT id, partido_id, jugador_id, tipo, minuto FROM tarjetas_partido WHERE partido_id=?")
        query.addBindValue(partido_id)
        query.exec()
        
        while query.next():
            tarjeta = TarjetaPartido(
                query.value(0),
                query.value(1),
                query.value(2),
                query.value(3),
                query.value(4)
            )
            tarjetas.append(tarjeta)
        
        return tarjetas
    
    @staticmethod
    def eliminar(id):
        query = QSqlQuery()
        query.prepare("DELETE FROM tarjetas_partido WHERE id=?")
        query.addBindValue(id)
        
        return query.exec()