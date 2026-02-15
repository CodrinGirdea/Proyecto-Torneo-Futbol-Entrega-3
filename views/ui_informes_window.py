# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'informes_window.ui'
##
## UI MEJORADA CON FILTROS Y SELECCIÓN DE RUTA
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget, QHBoxLayout, QCheckBox, QFrame, QLineEdit)

class Ui_InformesWindow(object):
    def setupUi(self, InformesWindow):
        if not InformesWindow.objectName():
            InformesWindow.setObjectName(u"InformesWindow")
        InformesWindow.resize(750, 700)
        InformesWindow.setMinimumSize(QSize(750, 700))
        InformesWindow.setMaximumSize(QSize(750, 700))
        self.verticalLayout = QVBoxLayout(InformesWindow)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 25, 25, 25)
        
        # TÍTULO
        self.label_titulo = QLabel(InformesWindow)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout.addWidget(self.label_titulo)
        
        # Separador
        self.line = QFrame(InformesWindow)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout.addWidget(self.line)

        # ==========================================
        # SECCIÓN: RUTA DE GUARDADO
        # ==========================================
        self.groupBox_ruta = QGroupBox(InformesWindow)
        self.groupBox_ruta.setObjectName(u"groupBox_ruta")
        self.horizontalLayout_ruta = QHBoxLayout(self.groupBox_ruta)
        
        self.label_ruta = QLabel(self.groupBox_ruta)
        self.label_ruta.setObjectName(u"label_ruta")
        self.label_ruta.setText("Carpeta de destino:")
        self.horizontalLayout_ruta.addWidget(self.label_ruta)
        
        self.input_ruta = QLineEdit(self.groupBox_ruta)
        self.input_ruta.setObjectName(u"input_ruta")
        self.input_ruta.setReadOnly(True)
        self.input_ruta.setPlaceholderText("informes/")
        self.horizontalLayout_ruta.addWidget(self.input_ruta)
        
        self.btn_seleccionar_ruta = QPushButton(self.groupBox_ruta)
        self.btn_seleccionar_ruta.setObjectName(u"btn_seleccionar_ruta")
        self.btn_seleccionar_ruta.setMinimumSize(QSize(120, 30))
        self.horizontalLayout_ruta.addWidget(self.btn_seleccionar_ruta)
        
        self.verticalLayout.addWidget(self.groupBox_ruta)

        # ==========================================
        # GRUPO 1: EQUIPOS Y JUGADORES
        # ==========================================
        self.groupBox_equipos = QGroupBox(InformesWindow)
        self.groupBox_equipos.setObjectName(u"groupBox_equipos")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_equipos)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.label_desc_equipos = QLabel(self.groupBox_equipos)
        self.label_desc_equipos.setObjectName(u"label_desc_equipos")
        self.label_desc_equipos.setWordWrap(True)
        self.verticalLayout_2.addWidget(self.label_desc_equipos)
        
        # Filtro por equipo
        self.horizontalLayout_equipos = QHBoxLayout()
        self.horizontalLayout_equipos.setObjectName(u"horizontalLayout_equipos")
        
        self.check_filtro_equipo = QCheckBox(self.groupBox_equipos)
        self.check_filtro_equipo.setObjectName(u"check_filtro_equipo")
        self.horizontalLayout_equipos.addWidget(self.check_filtro_equipo)
        
        self.combo_equipo = QComboBox(self.groupBox_equipos)
        self.combo_equipo.setObjectName(u"combo_equipo")
        self.combo_equipo.setEnabled(False)
        self.combo_equipo.setMinimumHeight(30)
        self.horizontalLayout_equipos.addWidget(self.combo_equipo)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_equipos)
        
        self.btn_generar_equipos = QPushButton(self.groupBox_equipos)
        self.btn_generar_equipos.setObjectName(u"btn_generar_equipos")
        self.btn_generar_equipos.setMinimumSize(QSize(0, 50))
        self.verticalLayout_2.addWidget(self.btn_generar_equipos)

        self.verticalLayout.addWidget(self.groupBox_equipos)

        # ==========================================
        # GRUPO 2: PARTIDOS Y RESULTADOS
        # ==========================================
        self.groupBox_partidos = QGroupBox(InformesWindow)
        self.groupBox_partidos.setObjectName(u"groupBox_partidos")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_partidos)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        
        self.label_desc_partidos = QLabel(self.groupBox_partidos)
        self.label_desc_partidos.setObjectName(u"label_desc_partidos")
        self.label_desc_partidos.setWordWrap(True)
        self.verticalLayout_3.addWidget(self.label_desc_partidos)
        
        # Filtro por eliminatoria
        self.horizontalLayout_partidos = QHBoxLayout()
        self.horizontalLayout_partidos.setObjectName(u"horizontalLayout_partidos")
        
        self.check_filtro_partidos = QCheckBox(self.groupBox_partidos)
        self.check_filtro_partidos.setObjectName(u"check_filtro_partidos")
        self.horizontalLayout_partidos.addWidget(self.check_filtro_partidos)
        
        self.combo_eliminatoria_partidos = QComboBox(self.groupBox_partidos)
        self.combo_eliminatoria_partidos.addItem("-- Todas las eliminatorias --")
        self.combo_eliminatoria_partidos.addItem("Octavos")
        self.combo_eliminatoria_partidos.addItem("Cuartos")
        self.combo_eliminatoria_partidos.addItem("Semifinal")
        self.combo_eliminatoria_partidos.addItem("Final")
        self.combo_eliminatoria_partidos.setObjectName(u"combo_eliminatoria_partidos")
        self.combo_eliminatoria_partidos.setEnabled(False)
        self.combo_eliminatoria_partidos.setMinimumHeight(30)
        self.horizontalLayout_partidos.addWidget(self.combo_eliminatoria_partidos)
        
        self.verticalLayout_3.addLayout(self.horizontalLayout_partidos)
        
        self.btn_generar_partidos = QPushButton(self.groupBox_partidos)
        self.btn_generar_partidos.setObjectName(u"btn_generar_partidos")
        self.btn_generar_partidos.setMinimumSize(QSize(0, 50))
        self.verticalLayout_3.addWidget(self.btn_generar_partidos)

        self.verticalLayout.addWidget(self.groupBox_partidos)

        # ==========================================
        # GRUPO 3: CLASIFICACIÓN Y ELIMINATORIAS
        # ==========================================
        self.groupBox_clasificacion = QGroupBox(InformesWindow)
        self.groupBox_clasificacion.setObjectName(u"groupBox_clasificacion")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_clasificacion)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        
        self.label_desc_clasificacion = QLabel(self.groupBox_clasificacion)
        self.label_desc_clasificacion.setObjectName(u"label_desc_clasificacion")
        self.label_desc_clasificacion.setWordWrap(True)
        self.verticalLayout_4.addWidget(self.label_desc_clasificacion)
        
        # Filtro por eliminatoria
        self.horizontalLayout_clasificacion = QHBoxLayout()
        self.horizontalLayout_clasificacion.setObjectName(u"horizontalLayout_clasificacion")
        
        self.check_filtro_clasificacion = QCheckBox(self.groupBox_clasificacion)
        self.check_filtro_clasificacion.setObjectName(u"check_filtro_clasificacion")
        self.horizontalLayout_clasificacion.addWidget(self.check_filtro_clasificacion)
        
        self.combo_eliminatoria_clasificacion = QComboBox(self.groupBox_clasificacion)
        self.combo_eliminatoria_clasificacion.addItem("-- Todas las eliminatorias --")
        self.combo_eliminatoria_clasificacion.addItem("Octavos")
        self.combo_eliminatoria_clasificacion.addItem("Cuartos")
        self.combo_eliminatoria_clasificacion.addItem("Semifinal")
        self.combo_eliminatoria_clasificacion.addItem("Final")
        self.combo_eliminatoria_clasificacion.setObjectName(u"combo_eliminatoria_clasificacion")
        self.combo_eliminatoria_clasificacion.setEnabled(False)
        self.combo_eliminatoria_clasificacion.setMinimumHeight(30)
        self.horizontalLayout_clasificacion.addWidget(self.combo_eliminatoria_clasificacion)
        
        self.verticalLayout_4.addLayout(self.horizontalLayout_clasificacion)
        
        self.btn_generar_clasificacion = QPushButton(self.groupBox_clasificacion)
        self.btn_generar_clasificacion.setObjectName(u"btn_generar_clasificacion")
        self.btn_generar_clasificacion.setMinimumSize(QSize(0, 50))
        self.verticalLayout_4.addWidget(self.btn_generar_clasificacion)

        self.verticalLayout.addWidget(self.groupBox_clasificacion)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)

        # BOTÓN VOLVER
        self.btn_volver = QPushButton(InformesWindow)
        self.btn_volver.setObjectName(u"btn_volver")
        self.btn_volver.setMinimumSize(QSize(0, 45))
        self.verticalLayout.addWidget(self.btn_volver)

        self.retranslateUi(InformesWindow)
        QMetaObject.connectSlotsByName(InformesWindow)

    def retranslateUi(self, InformesWindow):
        InformesWindow.setWindowTitle(QCoreApplication.translate("InformesWindow", u"Generación de Informes", None))
        self.label_titulo.setText(QCoreApplication.translate("InformesWindow", u"Generación de Informes en PDF", None))
        
        self.groupBox_ruta.setTitle(QCoreApplication.translate("InformesWindow", u"Configuración de Guardado", None))
        self.btn_seleccionar_ruta.setText(QCoreApplication.translate("InformesWindow", u"📁 Seleccionar Carpeta", None))
        
        self.groupBox_equipos.setTitle(QCoreApplication.translate("InformesWindow", u"1. Informe de Equipos y Jugadores", None))
        self.label_desc_equipos.setText(QCoreApplication.translate("InformesWindow", 
            u"Listado de equipos con sus jugadores, posiciones, goles y tarjetas. Incluye estadísticas por equipo.", None))
        self.check_filtro_equipo.setText(QCoreApplication.translate("InformesWindow", u"Filtrar por equipo:", None))
        self.btn_generar_equipos.setText(QCoreApplication.translate("InformesWindow", u"Generar Informe de Equipos", None))
        
        self.groupBox_partidos.setTitle(QCoreApplication.translate("InformesWindow", u"2. Informe de Partidos y Resultados", None))
        self.label_desc_partidos.setText(QCoreApplication.translate("InformesWindow", 
            u"Listado de partidos programados y jugados con equipos, árbitros, fechas y resultados.", None))
        self.check_filtro_partidos.setText(QCoreApplication.translate("InformesWindow", u"Filtrar por eliminatoria:", None))
        self.btn_generar_partidos.setText(QCoreApplication.translate("InformesWindow", u"Generar Informe de Partidos", None))
        
        self.groupBox_clasificacion.setTitle(QCoreApplication.translate("InformesWindow", u"3. Informe de Clasificación y Eliminatorias", None))
        self.label_desc_clasificacion.setText(QCoreApplication.translate("InformesWindow", 
            u"Tabla de clasificación, cuadro de eliminatorias y estadísticas globales del torneo.", None))
        self.check_filtro_clasificacion.setText(QCoreApplication.translate("InformesWindow", u"Filtrar por eliminatoria:", None))
        self.btn_generar_clasificacion.setText(QCoreApplication.translate("InformesWindow", u"Generar Informe de Clasificación", None))
        
        self.btn_volver.setText(QCoreApplication.translate("InformesWindow", u"Volver al Menú Principal", None))
