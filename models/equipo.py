from PySide6.QtSql import QSqlQuery

class Equipo:
    def __init__(self,id,nombre,curso,color_camiseta,escudo):
        self.id=id
        self.nombre=nombre
        self.curso=curso
        self.color_camiseta=color_camiseta
        self.escudo=escudo
    
    @staticmethod
    def crear(nombre, curso, color_camiseta, escudo):
        from PySide6.QtCore import QByteArray
        
        query = QSqlQuery()
        query.prepare("INSERT INTO equipos (nombre, curso, color_camiseta, escudo) VALUES (?,?,?,?)")
        query.addBindValue(nombre)
        query.addBindValue(curso)
        query.addBindValue(color_camiseta)

        if escudo is not None:
            if isinstance(escudo, str):
                query.addBindValue(None)
            elif isinstance(escudo, bytes):
                query.addBindValue(QByteArray(escudo))
            else:
                query.addBindValue(escudo) 
        else:
            query.addBindValue(None)

        return query.exec()

    @staticmethod
    def obtener_todos():
        equipos=[]
        query=QSqlQuery()
        query.exec("SELECT id, nombre, curso, color_camiseta, escudo FROM equipos")

        #Se recorre los datos obtenidos del SELECT y se guardan en una variable de tipo equipo para despues introducirlo en la lista y devolverlos
        while query.next():
            equipo= Equipo(query.value(0),
                           query.value(1),
                           query.value(2),
                           query.value(3),
                           query.value(4))
            equipos.append(equipo)
        return equipos

    @staticmethod
    def obtener_por_id(id):
        query=QSqlQuery()
        query.prepare("SELECT id,nombre,curso,color_camiseta,escudo FROM equipos WHERE id=?")
        query.addBindValue(id)
        query.exec()
        if query.next():
            return Equipo(
                query.value(0),
            query.value(1),
            query.value(2),
            query.value(3),
            query.value(4)
            )
        return None
            

    @staticmethod
    def actualizar(id, nombre, curso, color_camiseta, escudo):
        from PySide6.QtCore import QByteArray
        
        query = QSqlQuery()
        query.prepare("""
        UPDATE equipos SET nombre=?, curso=?, color_camiseta=?, escudo=?
        WHERE id= ?
        """)
        query.addBindValue(nombre)
        query.addBindValue(curso)
        query.addBindValue(color_camiseta)
        
        # ← CONVERTIR A QByteArray SI ES NECESARIO
        if escudo is not None:
            if isinstance(escudo, str):
                # Si por error llega como string, convertir a None
                query.addBindValue(None)
            elif isinstance(escudo, bytes):
                query.addBindValue(QByteArray(escudo))
            else:
                query.addBindValue(escudo)  # Ya es QByteArray
        else:
            query.addBindValue(None)
        
        query.addBindValue(id)

        return query.exec()

    @staticmethod
    def eliminar(id):
        query=QSqlQuery()
        query.prepare("DELETE FROM equipos WHERE id = ?")
        query.addBindValue(id)

        return query.exec()