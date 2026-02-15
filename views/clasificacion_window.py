from PySide6.QtWidgets import QWidget,QGraphicsScene, QGraphicsRectItem, QGraphicsTextItem, QGraphicsLineItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QBrush, QColor, QFont, QPixmap
from views.ui_clasificacion_window import Ui_Eliminatoria
from controllers.partido_controller import PartidoController
from utils.icon_helper import set_button_icon

class ClasificacionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Eliminatoria()
        self.ui.setupUi(self)

        self.setup_icons()

        self.setup_tooltips()

        self.setWindowTitle("Eliminatorias")

        self.scene=QGraphicsScene()
        self.ui.graphics_view_bracket.setScene(self.scene)

        self.ui.btn_actualizar.clicked.connect(self.dibujar_bracket)
        self.ui.btn_volver.clicked.connect(self.close)
        
        self.dibujar_bracket()

    def dibujar_bracket(self):
        """Dibuja el árbol completo de eliminatorias"""
        self.scene.clear()
        
        todos_partidos = PartidoController.obtener_todos_partidos()
        equipos = PartidoController.obtener_todos_los_equipos()
        
        partidos_octavos = [p for p in todos_partidos if p.eliminatoria == "Octavos"]
        partidos_cuartos = [p for p in todos_partidos if p.eliminatoria == "Cuartos"]
        partidos_semifinal = [p for p in todos_partidos if p.eliminatoria == "Semifinal"]
        partidos_final = [p for p in todos_partidos if p.eliminatoria == "Final"]
        
        margen_x = 50
        margen_y = 50
        ancho_caja = 150
        alto_caja = 60
        espacio_horizontal = 200
        
        num_columnas = 0
        if len(partidos_octavos) >0:
            num_columnas = 2
        if len(partidos_cuartos) >0:
            num_columnas = 4
        if len(partidos_semifinal) >0:
            num_columnas = 6
        if len(partidos_final) >0:
            num_columnas = 8
        
        if len(partidos_octavos) > 0:
            self.dibujar_titulo("OCTAVOS", margen_x, 10)
        if len(partidos_cuartos) > 0:
            self.dibujar_titulo("CUARTOS", margen_x + espacio_horizontal, 10)
        if len(partidos_semifinal) > 0:
            self.dibujar_titulo("SEMIFINAL", margen_x + espacio_horizontal * 2, 10)
        if len(partidos_final) > 0:
            self.dibujar_titulo("FINAL", margen_x + espacio_horizontal * 3, 10)
        
        y_octavos=margen_y
        espacio_vertical_octavos=100
        
        for i,partido in enumerate(partidos_octavos):
            if i >= 8:
                break
            y=y_octavos+i*espacio_vertical_octavos
            self.dibujar_partido(partido,equipos,margen_x,y,ancho_caja,alto_caja)
        
        if len(partidos_cuartos) > 0:
            y_cuartos = margen_y + espacio_vertical_octavos / 2
            espacio_vertical_cuartos = espacio_vertical_octavos * 2
            
            for i, partido in enumerate(partidos_cuartos):
                if i >= 4: 
                    break
                y = y_cuartos + i * espacio_vertical_cuartos
                x = margen_x + espacio_horizontal
                self.dibujar_partido(partido, equipos, x, y, ancho_caja, alto_caja)
                
                if len(partidos_octavos) >= i * 2 + 1:
                    self.dibujar_linea_conexion(margen_x+ancho_caja,y_octavos+i*2*espacio_vertical_octavos+alto_caja/2,x,y+alto_caja/2)
                if len(partidos_octavos) >= i * 2 + 2:
                    self.dibujar_linea_conexion(margen_x+ancho_caja,y_octavos+(i*2+1)*espacio_vertical_octavos+alto_caja/2,x,y+alto_caja/2)
        
        if len(partidos_semifinal) >0:
            y_semi=margen_y+espacio_vertical_octavos*1.5
            espacio_vertical_semi=espacio_vertical_octavos*4
            
            for i, partido in enumerate(partidos_semifinal):
                if i >=2: 
                    break
                y=y_semi+i*espacio_vertical_semi
                x=margen_x+espacio_horizontal*2
                self.dibujar_partido(partido,equipos,x,y,ancho_caja,alto_caja)
                
                if len(partidos_cuartos) >= i + 1:
                    y_cuartos_base = margen_y + espacio_vertical_octavos / 2
                    espacio_vertical_cuartos = espacio_vertical_octavos * 2
                    
                    self.dibujar_linea_conexion(margen_x+espacio_horizontal+ancho_caja,y_cuartos_base+i*espacio_vertical_cuartos+alto_caja/2,x,y+alto_caja/2)
        
        if len(partidos_final) >0:
            y_semi_base=margen_y+espacio_vertical_octavos*1.5
            espacio_vertical_semi=espacio_vertical_octavos*4
            
            y=y_semi_base+espacio_vertical_semi/2
            x=margen_x+espacio_horizontal*3
            self.dibujar_partido(partidos_final[0],equipos,x,y,ancho_caja,alto_caja)
            
            if len(partidos_semifinal) >= 1:
                self.dibujar_linea_conexion(margen_x+espacio_horizontal*2+ancho_caja,y_semi_base+alto_caja/2,x,y+alto_caja/2)
            if len(partidos_semifinal)>=2:
                self.dibujar_linea_conexion(margen_x+espacio_horizontal*2+ancho_caja,y_semi_base+espacio_vertical_semi+alto_caja/2,x,y+alto_caja/2)
            
            if partidos_final[0].jugado:
                equipo_campeon = self.obtener_ganador_con_escudo(partidos_final[0], equipos)
                if equipo_campeon:
                    self.dibujar_campeon(equipo_campeon.nombre,equipo_campeon.escudo,x+ancho_caja+50,y+alto_caja/2-40)

    def dibujar_titulo(self, texto, x, y):
        texto_item=QGraphicsTextItem(texto)
        font=QFont("Arial", 12, QFont.Bold)
        texto_item.setFont(font)
        texto_item.setPos(x, y)
        self.scene.addItem(texto_item)

    def dibujar_partido(self, partido, equipos, x, y, ancho, alto):
        equipo_local = ""
        equipo_visitante = ""
        for eq in equipos:
            if eq.id == partido.equipo_local_id:
                equipo_local = eq.nombre
            if eq.id == partido.equipo_visitante_id:
                equipo_visitante = eq.nombre
        
        ganador_local = False
        ganador_visitante = False
        if partido.jugado:
            if partido.goles_local > partido.goles_visitante:
                ganador_local = True
            elif partido.goles_visitante > partido.goles_local:
                ganador_visitante = True
        
        pen = QPen(QColor(100, 100, 100), 2)
        brush = QBrush(QColor(255, 255, 255))
        rect = QGraphicsRectItem(x, y, ancho, alto)
        rect.setPen(pen)
        rect.setBrush(brush)
        self.scene.addItem(rect)
        
        color_local = QColor(0, 150, 0) if ganador_local else QColor(0, 0, 0)
        texto_local = f"{equipo_local[:15]}"
        if partido.jugado:
            texto_local += f" ({partido.goles_local})"
        
        texto_item_local = QGraphicsTextItem(texto_local)
        font = QFont("Arial", 9, QFont.Bold if ganador_local else QFont.Normal)
        texto_item_local.setFont(font)
        texto_item_local.setDefaultTextColor(color_local)
        texto_item_local.setPos(x + 5, y + 5)
        self.scene.addItem(texto_item_local)
        
        color_visitante = QColor(0, 150, 0) if ganador_visitante else QColor(0, 0, 0)
        texto_visitante = f"{equipo_visitante[:15]}"
        
        if partido.jugado:
            texto_visitante += f" ({partido.goles_visitante})"
        
        texto_item_visitante = QGraphicsTextItem(texto_visitante)
        font = QFont("Arial", 9, QFont.Bold if ganador_visitante else QFont.Normal)
        texto_item_visitante.setFont(font)
        texto_item_visitante.setDefaultTextColor(color_visitante)
        texto_item_visitante.setPos(x + 5, y + 30)
        self.scene.addItem(texto_item_visitante)

    def dibujar_linea_conexion(self, x1, y1, x2, y2):
        pen = QPen(QColor(150, 150, 150), 2)
        
        linea1 = QGraphicsLineItem(x1, y1, x1 + 30, y1)
        linea1.setPen(pen)
        self.scene.addItem(linea1)
        
        linea2 = QGraphicsLineItem(x1 + 30, y1, x1 + 30, y2)
        linea2.setPen(pen)
        self.scene.addItem(linea2)
        
        linea3 = QGraphicsLineItem(x1 + 30, y2, x2, y2)
        linea3.setPen(pen)
        self.scene.addItem(linea3)
    
    def obtener_ganador(self, partido, equipos):
        if not partido.jugado:
            return None
        
        ganador_id = None
        if partido.goles_local > partido.goles_visitante:
            ganador_id = partido.equipo_local_id
        elif partido.goles_visitante > partido.goles_local:
            ganador_id = partido.equipo_visitante_id
        
        if ganador_id:
            for eq in equipos:
                if eq.id == ganador_id:
                    return eq.nombre
        return None
    
    def obtener_ganador_con_escudo(self, partido, equipos):
        """Obtiene el equipo ganador completo (con escudo)"""
        if not partido.jugado:
            return None
        
        ganador_id = None
        if partido.goles_local > partido.goles_visitante:
            ganador_id = partido.equipo_local_id
        elif partido.goles_visitante > partido.goles_local:
            ganador_id = partido.equipo_visitante_id
        
        if ganador_id:
            for eq in equipos:
                if eq.id == ganador_id:
                    return eq  # Devuelve el objeto equipo completo
        return None

    def dibujar_campeon(self, nombre_equipo, escudo_bytes, x, y):
        """Dibuja el trofeo del campeón con su escudo"""
        
        # ← AÑADIR PRINTS DE DEPURACIÓN
        print(f"[DEBUG] dibujar_campeon llamado")
        print(f"[DEBUG] nombre_equipo: {nombre_equipo}")
        print(f"[DEBUG] escudo_bytes tipo: {type(escudo_bytes)}")
        print(f"[DEBUG] escudo_bytes valor: {escudo_bytes}")
        
        # Verificar si escudo_bytes es válido y no es string
        if escudo_bytes and not isinstance(escudo_bytes, str) and len(escudo_bytes) > 0:
            print(f"[DEBUG] Intentando cargar escudo, tamaño: {len(escudo_bytes)} bytes")
            
            # Convertir bytes a QPixmap
            pixmap = QPixmap()
            
            # Asegurar que sea QByteArray
            from PySide6.QtCore import QByteArray
            if isinstance(escudo_bytes, bytes):
                escudo_bytes = QByteArray(escudo_bytes)
            
            resultado_carga = pixmap.loadFromData(escudo_bytes)
            print(f"[DEBUG] pixmap.loadFromData() resultado: {resultado_carga}")
            
            if resultado_carga:
                print(f"[DEBUG] ✓ Escudo cargado correctamente")
                # Escalar imagen
                pixmap_escalado = pixmap.scaled(
                    80, 80, 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                
                # Añadir imagen
                escudo_item = self.scene.addPixmap(pixmap_escalado)
                escudo_item.setPos(x, y)
                
                # Texto del campeón debajo del escudo
                texto = QGraphicsTextItem(f"🏆 CAMPEÓN\n{nombre_equipo}")
                font = QFont("Arial", 12, QFont.Bold)
                texto.setFont(font)
                texto.setDefaultTextColor(QColor(255, 215, 0))
                texto.setPos(x - 20, y + 90)
                self.scene.addItem(texto)
            else:
                print(f"[DEBUG] ✗ Error al cargar escudo, mostrando solo texto")
                # Si falla la carga, mostrar solo texto
                self.dibujar_campeon_sin_escudo(nombre_equipo, x, y)
        else:
            print(f"[DEBUG] No hay escudo válido, mostrando solo texto")
            # Sin escudo, solo texto
            self.dibujar_campeon_sin_escudo(nombre_equipo, x, y)

    def dibujar_campeon_sin_escudo(self, nombre_equipo, x, y):
        """Dibuja solo el texto del campeón sin escudo"""
        texto = f"🏆 CAMPEÓN\n{nombre_equipo}"
        texto_item = QGraphicsTextItem(texto)
        font = QFont("Arial", 14, QFont.Bold)
        texto_item.setFont(font)
        texto_item.setDefaultTextColor(QColor(255, 215, 0))
        texto_item.setPos(x, y)
        self.scene.addItem(texto_item)

    def setup_icons(self):
        """Configura los iconos de los botones"""
        set_button_icon(self.ui.btn_actualizar, "refrescar.png", 20)
        set_button_icon(self.ui.btn_volver, "volver.png", 20)

    def setup_tooltips(self):
        """Configura los tooltips"""
        self.ui.btn_actualizar.setToolTip("Actualizar el árbol del torneo")
        self.ui.btn_volver.setToolTip("Volver al menú principal")
