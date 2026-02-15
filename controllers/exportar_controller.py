import csv
import os
from datetime import datetime
from PySide6.QtSql import QSqlQuery
from models.equipo import Equipo
from models.participante import Participante
from models.partido import Partido
from models.gol_partido import GolPartido
from models.tarjeta_partido import TarjetaPartido


class ExportController:
    """Controlador para exportar datos del torneo a archivos CSV"""
    
    @staticmethod
    def exportar_clasificacion(ruta_archivo):
        """
        Exporta la clasificación de equipos a CSV
        Columnas: Posición, Equipo, Curso, Partidos Jugados, Partidos Ganados, 
                  Goles a Favor, Goles en Contra, Diferencia de Goles
        """
        try:
            # Obtener estadísticas de equipos
            equipos = Equipo.obtener_todos()
            estadisticas = []
            
            for equipo in equipos:
                # Contar partidos del equipo
                query = QSqlQuery()
                query.prepare("""
                    SELECT COUNT(*) FROM partidos 
                    WHERE (equipo_local_id = ? OR equipo_visitante_id = ?) 
                    AND jugado = 1
                """)
                query.addBindValue(equipo.id)
                query.addBindValue(equipo.id)
                query.exec()
                partidos_jugados = query.value(0) if query.next() else 0
                
                # Contar partidos ganados
                query.prepare("""
                    SELECT COUNT(*) FROM partidos 
                    WHERE jugado = 1 AND (
                        (equipo_local_id = ? AND goles_local > goles_visitante) OR
                        (equipo_visitante_id = ? AND goles_visitante > goles_local)
                    )
                """)
                query.addBindValue(equipo.id)
                query.addBindValue(equipo.id)
                query.exec()
                partidos_ganados = query.value(0) if query.next() else 0
                
                # Calcular goles a favor y en contra
                query.prepare("""
                    SELECT 
                        SUM(CASE WHEN equipo_local_id = ? THEN goles_local ELSE 0 END) +
                        SUM(CASE WHEN equipo_visitante_id = ? THEN goles_visitante ELSE 0 END) as goles_favor,
                        SUM(CASE WHEN equipo_local_id = ? THEN goles_visitante ELSE 0 END) +
                        SUM(CASE WHEN equipo_visitante_id = ? THEN goles_local ELSE 0 END) as goles_contra
                    FROM partidos 
                    WHERE (equipo_local_id = ? OR equipo_visitante_id = ?) 
                    AND jugado = 1
                """)
                query.addBindValue(equipo.id)
                query.addBindValue(equipo.id)
                query.addBindValue(equipo.id)
                query.addBindValue(equipo.id)
                query.addBindValue(equipo.id)
                query.addBindValue(equipo.id)
                query.exec()
                
                goles_favor = 0
                goles_contra = 0
                if query.next():
                    goles_favor = query.value(0) if query.value(0) else 0
                    goles_contra = query.value(1) if query.value(1) else 0
                
                diferencia = goles_favor - goles_contra
                
                estadisticas.append({
                    'equipo': equipo.nombre,
                    'curso': equipo.curso,
                    'partidos_jugados': partidos_jugados,
                    'partidos_ganados': partidos_ganados,
                    'goles_favor': goles_favor,
                    'goles_contra': goles_contra,
                    'diferencia': diferencia
                })
            
            # Ordenar por partidos ganados y diferencia de goles
            estadisticas.sort(key=lambda x: (x['partidos_ganados'], x['diferencia']), reverse=True)
            
            # Escribir CSV
            with open(ruta_archivo, 'w', newline='', encoding='utf-8-sig') as archivo:
                escritor = csv.writer(archivo, delimiter=";")
                
                # Cabecera
                escritor.writerow([
                    'Posición', 'Equipo', 'Curso', 'Partidos Jugados', 
                    'Partidos Ganados', 'Goles a Favor', 'Goles en Contra', 
                    'Diferencia de Goles'
                ])
                
                # Datos
                for i, stats in enumerate(estadisticas, 1):
                    escritor.writerow([
                        i,
                        stats['equipo'],
                        stats['curso'],
                        stats['partidos_jugados'],
                        stats['partidos_ganados'],
                        stats['goles_favor'],
                        stats['goles_contra'],
                        stats['diferencia']
                    ])
            
            return True, f"Clasificación exportada exitosamente a:\n{ruta_archivo}"
        
        except Exception as e:
            return False, f"Error al exportar clasificación: {str(e)}"
    
    @staticmethod
    def exportar_goleadores(ruta_archivo):
        """
        Exporta la tabla de goleadores a CSV
        Columnas: Posición, Jugador, Equipo, Curso, Goles
        """
        try:
            # Obtener jugadores con goles
            query = QSqlQuery()
            query.exec("""
                SELECT p.nombre, p.goles, p.equipo_id, e.nombre, e.curso
                FROM participantes p
                LEFT JOIN equipos e ON p.equipo_id = e.id
                WHERE p.es_jugador = 1 AND p.goles > 0
                ORDER BY p.goles DESC, p.nombre ASC
            """)
            
            goleadores = []
            while query.next():
                goleadores.append({
                    'nombre': query.value(0),
                    'goles': query.value(1),
                    'equipo': query.value(3) if query.value(3) else 'Sin equipo',
                    'curso': query.value(4) if query.value(4) else 'N/A'
                })
            
            # Escribir CSV
            with open(ruta_archivo, 'w', newline='', encoding='utf-8-sig') as archivo:
                escritor = csv.writer(archivo, delimiter=";")
                
                # Cabecera
                escritor.writerow(['Posición', 'Jugador', 'Equipo', 'Curso', 'Goles'])
                
                # Datos
                for i, goleador in enumerate(goleadores, 1):
                    escritor.writerow([
                        i,
                        goleador['nombre'],
                        goleador['equipo'],
                        goleador['curso'],
                        goleador['goles']
                    ])
            
            return True, f"Goleadores exportados exitosamente a:\n{ruta_archivo}"
        
        except Exception as e:
            return False, f"Error al exportar goleadores: {str(e)}"
    
    @staticmethod
    def exportar_tarjetas(ruta_archivo):
        """
        Exporta estadísticas de tarjetas a CSV
        Columnas: Jugador, Equipo, Curso, Tarjetas Amarillas, Tarjetas Rojas, Total
        """
        try:
            # Obtener jugadores con tarjetas
            query = QSqlQuery()
            query.exec("""
                SELECT p.nombre, p.t_amarillas, p.t_rojas, e.nombre, e.curso
                FROM participantes p
                LEFT JOIN equipos e ON p.equipo_id = e.id
                WHERE p.es_jugador = 1 AND (p.t_amarillas > 0 OR p.t_rojas > 0)
                ORDER BY (p.t_rojas * 2 + p.t_amarillas) DESC, p.nombre ASC
            """)
            
            jugadores_tarjetas = []
            while query.next():
                amarillas = query.value(1)
                rojas = query.value(2)
                jugadores_tarjetas.append({
                    'nombre': query.value(0),
                    'amarillas': amarillas,
                    'rojas': rojas,
                    'total': amarillas + rojas,
                    'equipo': query.value(3) if query.value(3) else 'Sin equipo',
                    'curso': query.value(4) if query.value(4) else 'N/A'
                })
            
            # Escribir CSV
            with open(ruta_archivo, 'w', newline='', encoding='utf-8-sig') as archivo:
                escritor = csv.writer(archivo, delimiter=";")
                
                # Cabecera
                escritor.writerow(['Jugador', 'Equipo', 'Curso', 'Tarjetas Amarillas', 'Tarjetas Rojas', 'Total'])
                
                # Datos
                for jugador in jugadores_tarjetas:
                    escritor.writerow([
                        jugador['nombre'],
                        jugador['equipo'],
                        jugador['curso'],
                        jugador['amarillas'],
                        jugador['rojas'],
                        jugador['total']
                    ])
            
            return True, f"Estadísticas de tarjetas exportadas exitosamente a:\n{ruta_archivo}"
        
        except Exception as e:
            return False, f"Error al exportar tarjetas: {str(e)}"
    
    @staticmethod
    def exportar_partidos_jugados(ruta_archivo):
        """
        Exporta todos los partidos jugados a CSV
        Columnas: Fecha, Hora, Equipo Local, Equipo Visitante, Resultado, Eliminatoria, Árbitro
        """
        try:
            partidos = Partido.obtener_todos()
            equipos_dict = {eq.id: eq for eq in Equipo.obtener_todos()}
            arbitros_dict = {arb.id: arb for arb in Participante.obtener_arbitros()}
            
            # Filtrar solo partidos jugados
            partidos_jugados = [p for p in partidos if p.jugado == 1]
            
            # Ordenar por fecha y hora
            partidos_jugados.sort(key=lambda p: (p.fecha, p.hora))
            
            # Escribir CSV
            with open(ruta_archivo, 'w', newline='', encoding='utf-8-sig') as archivo:
                escritor = csv.writer(archivo, delimiter=";")
                
                # Cabecera
                escritor.writerow([
                    'Fecha', 'Hora', 'Equipo Local', 'Equipo Visitante', 
                    'Resultado', 'Eliminatoria', 'Árbitro'
                ])
                
                # Datos
                for partido in partidos_jugados:
                    equipo_local = equipos_dict.get(partido.equipo_local_id)
                    equipo_visitante = equipos_dict.get(partido.equipo_visitante_id)
                    arbitro = arbitros_dict.get(partido.arbitro_id)
                    
                    escritor.writerow([
                        partido.fecha,
                        partido.hora,
                        equipo_local.nombre if equipo_local else 'Desconocido',
                        equipo_visitante.nombre if equipo_visitante else 'Desconocido',
                        f"{partido.goles_local} - {partido.goles_visitante}",
                        partido.eliminatoria,
                        arbitro.nombre if arbitro else 'Desconocido'
                    ])
            
            return True, f"Partidos jugados exportados exitosamente a:\n{ruta_archivo}"
        
        except Exception as e:
            return False, f"Error al exportar partidos: {str(e)}"
    
    @staticmethod
    def exportar_calendario_completo(ruta_archivo):
        """
        Exporta el calendario completo (jugados y pendientes) a CSV
        Columnas: Fecha, Hora, Equipo Local, Equipo Visitante, Eliminatoria, Estado, Resultado, Árbitro
        """
        try:
            partidos = Partido.obtener_todos()
            equipos_dict = {eq.id: eq for eq in Equipo.obtener_todos()}
            arbitros_dict = {arb.id: arb for arb in Participante.obtener_arbitros()}
            
            # Ordenar por fecha y hora
            partidos.sort(key=lambda p: (p.fecha, p.hora))
            
            # Escribir CSV
            with open(ruta_archivo, 'w', newline='', encoding='utf-8-sig') as archivo:
                escritor = csv.writer(archivo, delimiter=";")
                
                # Cabecera
                escritor.writerow([
                    'Fecha', 'Hora', 'Equipo Local', 'Equipo Visitante', 
                    'Eliminatoria', 'Estado', 'Resultado', 'Árbitro'
                ])
                
                # Datos
                for partido in partidos:
                    equipo_local = equipos_dict.get(partido.equipo_local_id)
                    equipo_visitante = equipos_dict.get(partido.equipo_visitante_id)
                    arbitro = arbitros_dict.get(partido.arbitro_id)
                    
                    estado = "Jugado" if partido.jugado == 1 else "Pendiente"
                    resultado = f"{partido.goles_local} - {partido.goles_visitante}" if partido.jugado == 1 else "-"
                    
                    escritor.writerow([
                        partido.fecha,
                        partido.hora,
                        equipo_local.nombre if equipo_local else 'Desconocido',
                        equipo_visitante.nombre if equipo_visitante else 'Desconocido',
                        partido.eliminatoria,
                        estado,
                        resultado,
                        arbitro.nombre if arbitro else 'Desconocido'
                    ])
            
            return True, f"Calendario completo exportado exitosamente a:\n{ruta_archivo}"
        
        except Exception as e:
            return False, f"Error al exportar calendario: {str(e)}"
    
    @staticmethod
    def exportar_jugadores(ruta_archivo):
        """
        Exporta todos los jugadores con sus estadísticas a CSV
        Columnas: Nombre, Fecha Nacimiento, Curso, Equipo, Posición, Goles, Tarjetas Amarillas, Tarjetas Rojas
        """
        try:
            participantes = Participante.obtener_todos()
            equipos_dict = {eq.id: eq for eq in Equipo.obtener_todos()}
            
            # Filtrar solo jugadores
            jugadores = [p for p in participantes if p.es_jugador == 1]
            
            # Ordenar por nombre
            jugadores.sort(key=lambda j: j.nombre)
            
            # Escribir CSV
            with open(ruta_archivo, 'w', newline='', encoding='utf-8-sig') as archivo:
                escritor = csv.writer(archivo, delimiter=";")
                
                # Cabecera
                escritor.writerow([
                    'Nombre', 'Fecha Nacimiento', 'Curso', 'Equipo', 'Posición', 
                    'Goles', 'Tarjetas Amarillas', 'Tarjetas Rojas'
                ])
                
                # Datos
                for jugador in jugadores:
                    equipo = equipos_dict.get(jugador.equipo_id)
                    
                    escritor.writerow([
                        jugador.nombre,
                        jugador.fecha_nacimiento,
                        jugador.curso,
                        equipo.nombre if equipo else 'Sin equipo',
                        jugador.posicion if jugador.posicion else 'N/A',
                        jugador.goles,
                        jugador.t_amarillas,
                        jugador.t_rojas
                    ])
            
            return True, f"Jugadores exportados exitosamente a:\n{ruta_archivo}"
        
        except Exception as e:
            return False, f"Error al exportar jugadores: {str(e)}"
    
    @staticmethod
    def obtener_ruta_exportacion(nombre_base):
        """
        Genera una ruta de archivo CSV con timestamp
        """
        carpeta_exportacion = os.path.join(os.path.expanduser("~"), "Desktop")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"{nombre_base}_{timestamp}.csv"
        return os.path.join(carpeta_exportacion, nombre_archivo)