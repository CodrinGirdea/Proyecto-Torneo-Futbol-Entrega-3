from PySide6.QtSql import QSqlDatabase,QSqlQuery 
import os, sys

def get_db_path():
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, "torneoFutbol.db")


def conectar():
    ruta_db = get_db_path()
    es_primera_vez = not os.path.exists(ruta_db)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(ruta_db)

    if not db.open():
        raise Exception("No se pudo abrir la BD")

    query = QSqlQuery()
    query.exec("PRAGMA foreign_keys = ON;")

    crear_tablas(query)

    if es_primera_vez:
        cargar_datos_ejemplo(query)

    return db

def crear_tablas(query):
    query.exec("""
    CREATE TABLE IF NOT EXISTS equipos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    curso TEXT NOT NULL,
    color_camiseta TEXT,
    escudo BLOB
    )""")

    query.exec("""
    CREATE TABLE IF NOT EXISTS participantes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    fecha_nacimiento TEXT NOT NULL,
    curso TEXT NOT NULL,
    es_jugador INTEGER DEFAULT 0,
    es_arbitro INTEGER DEFAULT 0,
    posicion TEXT,
    equipo_id INTEGER,
    t_amarillas INTEGER DEFAULT 0,
    t_rojas INTEGER DEFAULT 0,
    goles INTEGER DEFAULT 0,
    FOREIGN KEY (equipo_id) REFERENCES equipos(id) ON DELETE CASCADE
    )""")

    query.exec("""
    CREATE TABLE IF NOT EXISTS partidos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipo_local_id INTEGER NOT NULL,
    equipo_visitante_id INTEGER NOT NULL,
    arbitro_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    hora TEXT NOT NULL,
    eliminatoria TEXT NOT NULL,
    goles_local INTEGER DEFAULT 0,
    goles_visitante INTEGER DEFAULT 0,
    jugado INTEGER DEFAULT 0,
    FOREIGN KEY (equipo_local_id) REFERENCES equipos(id) ON DELETE RESTRICT,
    FOREIGN KEY (equipo_visitante_id) REFERENCES equipos(id) ON DELETE RESTRICT,
    FOREIGN KEY (arbitro_id) REFERENCES participantes(id) ON DELETE RESTRICT
    )""")

    query.exec("""
    CREATE TABLE IF NOT EXISTS goles_partido(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    partido_id INTEGER NOT NULL,
    jugador_id INTEGER NOT NULL,
    minuto INTEGER NOT NULL,
    FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE,
    FOREIGN KEY (jugador_id) REFERENCES participantes(id) ON DELETE CASCADE
    )""")

    query.exec("""
    CREATE TABLE IF NOT EXISTS tarjetas_partido(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    partido_id INTEGER NOT NULL,
    jugador_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    minuto INTEGER NOT NULL,
    FOREIGN KEY (partido_id) REFERENCES partidos(id) ON DELETE CASCADE,
    FOREIGN KEY (jugador_id) REFERENCES participantes(id) ON DELETE CASCADE
    )
    """)

def cargar_datos_ejemplo(query):
    
    # ====== EQUIPOS (16 equipos para Octavos de Final) ======
    equipos = [
        ("Los Tigres", "2º DAM A", "Rojo", None),
        ("Águilas FC", "2º DAM A", "Azul", None),
        ("Leones United", "2º DAM B", "Verde", None),
        ("Lobos FC", "2º DAM B", "Amarillo", None),
        ("Dragones", "1º DAM A", "Naranja", None),
        ("Halcones", "1º DAM A", "Negro", None),
        ("Panteras", "1º DAM B", "Blanco", None),
        ("Titanes", "1º DAM B", "Morado", None),
        ("Guerreros", "2º ASIR A", "Rojo Oscuro", None),
        ("Fénix FC", "2º ASIR A", "Dorado", None),
        ("Spartanos", "2º ASIR B", "Verde Oscuro", None),
        ("Vikingos", "2º ASIR B", "Azul Marino", None),
        ("Cóndores", "1º ASIR A", "Gris", None),
        ("Toros FC", "1º ASIR A", "Marrón", None),
        ("Pumas", "1º ASIR B", "Negro y Oro", None),
        ("Jaguares", "1º ASIR B", "Verde Lima", None)
    ]
    
    for equipo in equipos:
        query.prepare("INSERT INTO equipos (nombre, curso, color_camiseta, escudo) VALUES (?, ?, ?, ?)")
        query.addBindValue(equipo[0])
        query.addBindValue(equipo[1])
        query.addBindValue(equipo[2])
        query.addBindValue(equipo[3])
        query.exec()
    
    # ====== JUGADORES (4 por equipo = 64 jugadores) ======
    jugadores = [
        # Los Tigres (equipo_id = 1)
        ("Carlos Martínez", "2005-03-15", "2º DAM A", 1, 0, "Portero", 1),
        ("Jorge López", "2005-06-20", "2º DAM A", 1, 0, "Defensa", 1),
        ("Pedro García", "2005-01-10", "2º DAM A", 1, 0, "Centrocampista", 1),
        ("Luis Fernández", "2005-08-05", "2º DAM A", 1, 0, "Delantero", 1),
        
        # Águilas FC (equipo_id = 2)
        ("Miguel Sánchez", "2005-04-12", "2º DAM A", 1, 0, "Portero", 2),
        ("Andrés Ruiz", "2005-07-18", "2º DAM A", 1, 0, "Defensa", 2),
        ("Pablo Moreno", "2005-02-22", "2º DAM A", 1, 0, "Centrocampista", 2),
        ("David Torres", "2005-09-30", "2º DAM A", 1, 0, "Delantero", 2),
        
        # Leones United (equipo_id = 3)
        ("Javier Díaz", "2006-05-08", "2º DAM B", 1, 0, "Portero", 3),
        ("Roberto Pérez", "2006-11-14", "2º DAM B", 1, 0, "Defensa", 3),
        ("Alberto Gómez", "2006-03-25", "2º DAM B", 1, 0, "Centrocampista", 3),
        ("Sergio Ramírez", "2006-12-01", "2º DAM B", 1, 0, "Delantero", 3),
        
        # Lobos FC (equipo_id = 4)
        ("Fernando Castro", "2006-06-17", "2º DAM B", 1, 0, "Portero", 4),
        ("Daniel Ortiz", "2006-10-09", "2º DAM B", 1, 0, "Defensa", 4),
        ("Raúl Navarro", "2006-04-13", "2º DAM B", 1, 0, "Centrocampista", 4),
        ("Antonio Jiménez", "2006-08-28", "2º DAM B", 1, 0, "Delantero", 4),
        
        # Dragones (equipo_id = 5)
        ("Francisco Herrera", "2005-02-19", "1º DAM A", 1, 0, "Portero", 5),
        ("Alejandro Vega", "2005-07-07", "1º DAM A", 1, 0, "Defensa", 5),
        ("Ricardo Molina", "2005-12-11", "1º DAM A", 1, 0, "Centrocampista", 5),
        ("Marcos Silva", "2005-05-23", "1º DAM A", 1, 0, "Delantero", 5),
        
        # Halcones (equipo_id = 6)
        ("Gabriel Romero", "2005-09-16", "1º DAM A", 1, 0, "Portero", 6),
        ("Iván Méndez", "2005-03-29", "1º DAM A", 1, 0, "Defensa", 6),
        ("Oscar Vargas", "2005-11-02", "1º DAM A", 1, 0, "Centrocampista", 6),
        ("Adrián Campos", "2005-06-06", "1º DAM A", 1, 0, "Delantero", 6),
        
        # Panteras (equipo_id = 7)
        ("Hugo Fuentes", "2006-01-21", "1º DAM B", 1, 0, "Portero", 7),
        ("Mario Cortés", "2006-08-14", "1º DAM B", 1, 0, "Defensa", 7),
        ("Víctor Reyes", "2006-04-05", "1º DAM B", 1, 0, "Centrocampista", 7),
        ("Samuel Blanco", "2006-10-18", "1º DAM B", 1, 0, "Delantero", 7),
        
        # Titanes (equipo_id = 8)
        ("Rubén Medina", "2006-07-26", "1º DAM B", 1, 0, "Portero", 8),
        ("Ángel Pascual", "2006-02-08", "1º DAM B", 1, 0, "Defensa", 8),
        ("Cristian Domínguez", "2006-09-19", "1º DAM B", 1, 0, "Centrocampista", 8),
        ("Manuel Iglesias", "2006-05-31", "1º DAM B", 1, 0, "Delantero", 8),
        
        # Guerreros (equipo_id = 9)
        ("Rodrigo Santos", "2005-04-22", "2º ASIR A", 1, 0, "Portero", 9),
        ("Julián Herrero", "2005-09-11", "2º ASIR A", 1, 0, "Defensa", 9),
        ("Mateo Cruz", "2005-01-30", "2º ASIR A", 1, 0, "Centrocampista", 9),
        ("Lucas Rojas", "2005-07-19", "2º ASIR A", 1, 0, "Delantero", 9),
        
        # Fénix FC (equipo_id = 10)
        ("Diego Flores", "2005-11-08", "2º ASIR A", 1, 0, "Portero", 10),
        ("Emilio Prieto", "2005-05-27", "2º ASIR A", 1, 0, "Defensa", 10),
        ("Bruno Castillo", "2005-12-14", "2º ASIR A", 1, 0, "Centrocampista", 10),
        ("Adriano Vidal", "2005-03-03", "2º ASIR A", 1, 0, "Delantero", 10),
        
        # Spartanos (equipo_id = 11)
        ("Nicolás León", "2006-02-17", "2º ASIR B", 1, 0, "Portero", 11),
        ("Tomás Gil", "2006-08-06", "2º ASIR B", 1, 0, "Defensa", 11),
        ("Simón Parra", "2006-04-25", "2º ASIR B", 1, 0, "Centrocampista", 11),
        ("Marcos Ibáñez", "2006-10-13", "2º ASIR B", 1, 0, "Delantero", 11),
        
        # Vikingos (equipo_id = 12)
        ("Santiago Mora", "2006-06-02", "2º ASIR B", 1, 0, "Portero", 12),
        ("Esteban Rivas", "2006-12-21", "2º ASIR B", 1, 0, "Defensa", 12),
        ("Gonzalo Peña", "2006-01-09", "2º ASIR B", 1, 0, "Centrocampista", 12),
        ("Benjamín Luna", "2006-07-28", "2º ASIR B", 1, 0, "Delantero", 12),
        
        # Cóndores (equipo_id = 13)
        ("Felipe Bravo", "2005-03-18", "1º ASIR A", 1, 0, "Portero", 13),
        ("Maximiliano Soto", "2005-09-07", "1º ASIR A", 1, 0, "Defensa", 13),
        ("Sebastián Arias", "2005-05-26", "1º ASIR A", 1, 0, "Centrocampista", 13),
        ("Lorenzo Núñez", "2005-11-15", "1º ASIR A", 1, 0, "Delantero", 13),
        
        # Toros FC (equipo_id = 14)
        ("Ignacio Mendoza", "2005-01-04", "1º ASIR A", 1, 0, "Portero", 14),
        ("Valentín Aguilar", "2005-07-23", "1º ASIR A", 1, 0, "Defensa", 14),
        ("Joaquín Salazar", "2005-02-11", "1º ASIR A", 1, 0, "Centrocampista", 14),
        ("Damián Cabrera", "2005-08-30", "1º ASIR A", 1, 0, "Delantero", 14),
        
        # Pumas (equipo_id = 15)
        ("Martín Guerrero", "2006-04-09", "1º ASIR B", 1, 0, "Portero", 15),
        ("Facundo Delgado", "2006-10-28", "1º ASIR B", 1, 0, "Defensa", 15),
        ("Leandro Ortega", "2006-06-17", "1º ASIR B", 1, 0, "Centrocampista", 15),
        ("Thiago Varela", "2006-12-05", "1º ASIR B", 1, 0, "Delantero", 15),
        
        # Jaguares (equipo_id = 16)
        ("Ezequiel Montoya", "2006-02-24", "1º ASIR B", 1, 0, "Portero", 16),
        ("Agustín Serrano", "2006-08-13", "1º ASIR B", 1, 0, "Defensa", 16),
        ("Renato Campos", "2006-03-02", "1º ASIR B", 1, 0, "Centrocampista", 16),
        ("Valentino Suárez", "2006-09-21", "1º ASIR B", 1, 0, "Delantero", 16),
    ]
    
    for jugador in jugadores:
        query.prepare("""
            INSERT INTO participantes (nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles) 
            VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, 0)
        """)
        query.addBindValue(jugador[0])
        query.addBindValue(jugador[1])
        query.addBindValue(jugador[2])
        query.addBindValue(jugador[3])
        query.addBindValue(jugador[4])
        query.addBindValue(jugador[5])
        query.addBindValue(jugador[6])
        query.exec()
    
    # ====== ÁRBITROS (8 árbitros) ======
    arbitros = [
        ("Juan Carlos Ref", "1990-05-15", "Profesor", 0, 1),
        ("María González Ref", "1988-08-22", "Profesor", 0, 1),
        ("Antonio Pérez Ref", "1992-11-10", "Profesor", 0, 1),
        ("Laura Martín Ref", "1995-03-18", "Profesor", 0, 1),
        ("Roberto Silva Ref", "1991-07-05", "Profesor", 0, 1),
        ("Carmen López Ref", "1989-12-28", "Profesor", 0, 1),
        ("Francisco Torres Ref", "1993-06-14", "Profesor", 0, 1),
        ("Elena Ruiz Ref", "1994-02-09", "Profesor", 0, 1),
    ]
    
    for arbitro in arbitros:
        query.prepare("""
            INSERT INTO participantes (nombre, fecha_nacimiento, curso, es_jugador, es_arbitro, posicion, equipo_id, t_amarillas, t_rojas, goles) 
            VALUES (?, ?, ?, ?, ?, NULL, NULL, 0, 0, 0)
        """)
        query.addBindValue(arbitro[0])
        query.addBindValue(arbitro[1])
        query.addBindValue(arbitro[2])
        query.addBindValue(arbitro[3])
        query.addBindValue(arbitro[4])
        query.exec()
    
    # ====== PARTIDOS DE OCTAVOS DE FINAL (8 partidos) ======
    partidos_octavos = [
        (1, 2, 65, "2026-01-20", "16:00", "Octavos"),   # Los Tigres vs Águilas FC
        (3, 4, 66, "2026-01-20", "17:30", "Octavos"),   # Leones vs Lobos
        (5, 6, 67, "2026-01-21", "16:00", "Octavos"),   # Dragones vs Halcones
        (7, 8, 68, "2026-01-21", "17:30", "Octavos"),   # Panteras vs Titanes
        (9, 10, 69, "2026-01-22", "16:00", "Octavos"),  # Guerreros vs Fénix
        (11, 12, 70, "2026-01-22", "17:30", "Octavos"), # Spartanos vs Vikingos
        (13, 14, 71, "2026-01-23", "16:00", "Octavos"), # Cóndores vs Toros
        (15, 16, 72, "2026-01-23", "17:30", "Octavos"), # Pumas vs Jaguares
    ]
    
    for partido in partidos_octavos:
        query.prepare("""
            INSERT INTO partidos (equipo_local_id, equipo_visitante_id, arbitro_id, fecha, hora, eliminatoria, goles_local, goles_visitante, jugado) 
            VALUES (?, ?, ?, ?, ?, ?, 0, 0, 0)
        """)
        query.addBindValue(partido[0])
        query.addBindValue(partido[1])
        query.addBindValue(partido[2])
        query.addBindValue(partido[3])
        query.addBindValue(partido[4])
        query.addBindValue(partido[5])
        query.exec()
    
    print("✓ Datos de ejemplo cargados correctamente")
    print("✓ 16 equipos, 64 jugadores, 8 árbitros")
    print("✓ 8 partidos de Octavos de Final programados")