# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resultados_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Resultados(object):
    def setupUi(self, Resultados):
        if not Resultados.objectName():
            Resultados.setObjectName(u"Resultados")
        Resultados.resize(1500, 900)
        Resultados.setMinimumSize(QSize(1500, 900))
        self.main_layout = QHBoxLayout(Resultados)
        self.main_layout.setObjectName(u"main_layout")
        self.grupo_gestion_partido = QGroupBox(Resultados)
        self.grupo_gestion_partido.setObjectName(u"grupo_gestion_partido")
        self.grupo_gestion_partido.setMinimumSize(QSize(650, 0))
        self.grupo_gestion_partido.setMaximumSize(QSize(650, 16777215))
        self.gridLayout_gestion = QGridLayout(self.grupo_gestion_partido)
        self.gridLayout_gestion.setObjectName(u"gridLayout_gestion")
        self.btn_anadir_tarjetas = QPushButton(self.grupo_gestion_partido)
        self.btn_anadir_tarjetas.setObjectName(u"btn_anadir_tarjetas")

        self.gridLayout_gestion.addWidget(self.btn_anadir_tarjetas, 10, 5, 1, 1)

        self.label_jugador_gol = QLabel(self.grupo_gestion_partido)
        self.label_jugador_gol.setObjectName(u"label_jugador_gol")
        self.label_jugador_gol.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_gestion.addWidget(self.label_jugador_gol, 6, 0, 1, 1)

        self.label_goles_registrados = QLabel(self.grupo_gestion_partido)
        self.label_goles_registrados.setObjectName(u"label_goles_registrados")

        self.gridLayout_gestion.addWidget(self.label_goles_registrados, 7, 0, 1, 2)

        self.label_tarjetas_registradas = QLabel(self.grupo_gestion_partido)
        self.label_tarjetas_registradas.setObjectName(u"label_tarjetas_registradas")

        self.gridLayout_gestion.addWidget(self.label_tarjetas_registradas, 11, 0, 1, 2)

        self.combo_partidos = QComboBox(self.grupo_gestion_partido)
        self.combo_partidos.setObjectName(u"combo_partidos")

        self.gridLayout_gestion.addWidget(self.combo_partidos, 3, 1, 1, 5)

        self.combo_jugador_gol = QComboBox(self.grupo_gestion_partido)
        self.combo_jugador_gol.setObjectName(u"combo_jugador_gol")
        self.combo_jugador_gol.setMaximumSize(QSize(218, 16777215))

        self.gridLayout_gestion.addWidget(self.combo_jugador_gol, 6, 1, 1, 2)

        self.label_jugador_tarjeta = QLabel(self.grupo_gestion_partido)
        self.label_jugador_tarjeta.setObjectName(u"label_jugador_tarjeta")

        self.gridLayout_gestion.addWidget(self.label_jugador_tarjeta, 10, 0, 1, 1)

        self.combo_jugador_tarjeta = QComboBox(self.grupo_gestion_partido)
        self.combo_jugador_tarjeta.setObjectName(u"combo_jugador_tarjeta")
        self.combo_jugador_tarjeta.setMinimumSize(QSize(174, 0))

        self.gridLayout_gestion.addWidget(self.combo_jugador_tarjeta, 10, 1, 1, 1)

        self.label_titulo = QLabel(self.grupo_gestion_partido)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_titulo.setFont(font)

        self.gridLayout_gestion.addWidget(self.label_titulo, 0, 0, 1, 6)

        self.table_tarjetas = QTableWidget(self.grupo_gestion_partido)
        if (self.table_tarjetas.columnCount() < 4):
            self.table_tarjetas.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_tarjetas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_tarjetas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_tarjetas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_tarjetas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_tarjetas.setObjectName(u"table_tarjetas")
        self.table_tarjetas.setColumnCount(4)

        self.gridLayout_gestion.addWidget(self.table_tarjetas, 12, 0, 1, 6)

        self.btn_anadir_gol = QPushButton(self.grupo_gestion_partido)
        self.btn_anadir_gol.setObjectName(u"btn_anadir_gol")

        self.gridLayout_gestion.addWidget(self.btn_anadir_gol, 6, 5, 1, 1)

        self.btn_volver = QPushButton(self.grupo_gestion_partido)
        self.btn_volver.setObjectName(u"btn_volver")
        self.btn_volver.setMinimumSize(QSize(218, 0))

        self.gridLayout_gestion.addWidget(self.btn_volver, 13, 3, 1, 1)

        self.label_titulo_goles = QLabel(self.grupo_gestion_partido)
        self.label_titulo_goles.setObjectName(u"label_titulo_goles")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_titulo_goles.setFont(font1)

        self.gridLayout_gestion.addWidget(self.label_titulo_goles, 5, 0, 1, 2)

        self.label_partido_y_equipos = QLabel(self.grupo_gestion_partido)
        self.label_partido_y_equipos.setObjectName(u"label_partido_y_equipos")
        self.label_partido_y_equipos.setFont(font1)

        self.gridLayout_gestion.addWidget(self.label_partido_y_equipos, 1, 0, 1, 2)

        self.btn_finalizar_partido = QPushButton(self.grupo_gestion_partido)
        self.btn_finalizar_partido.setObjectName(u"btn_finalizar_partido")
        self.btn_finalizar_partido.setMinimumSize(QSize(218, 0))

        self.gridLayout_gestion.addWidget(self.btn_finalizar_partido, 13, 1, 1, 1)

        self.table_goles = QTableWidget(self.grupo_gestion_partido)
        if (self.table_goles.columnCount() < 3):
            self.table_goles.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_goles.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_goles.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_goles.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.table_goles.setObjectName(u"table_goles")
        self.table_goles.setColumnCount(3)

        self.gridLayout_gestion.addWidget(self.table_goles, 8, 0, 1, 6)

        self.label_registrar_tarjetas = QLabel(self.grupo_gestion_partido)
        self.label_registrar_tarjetas.setObjectName(u"label_registrar_tarjetas")
        self.label_registrar_tarjetas.setFont(font1)

        self.gridLayout_gestion.addWidget(self.label_registrar_tarjetas, 9, 0, 1, 2)

        self.label_seleccionar_partido = QLabel(self.grupo_gestion_partido)
        self.label_seleccionar_partido.setObjectName(u"label_seleccionar_partido")

        self.gridLayout_gestion.addWidget(self.label_seleccionar_partido, 3, 0, 1, 1)

        self.label_tipo_tarjeta = QLabel(self.grupo_gestion_partido)
        self.label_tipo_tarjeta.setObjectName(u"label_tipo_tarjeta")
        self.label_tipo_tarjeta.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_gestion.addWidget(self.label_tipo_tarjeta, 10, 3, 1, 1)

        self.combo_tipo_tarjeta = QComboBox(self.grupo_gestion_partido)
        self.combo_tipo_tarjeta.addItem("")
        self.combo_tipo_tarjeta.addItem("")
        self.combo_tipo_tarjeta.addItem("")
        self.combo_tipo_tarjeta.setObjectName(u"combo_tipo_tarjeta")
        self.combo_tipo_tarjeta.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_gestion.addWidget(self.combo_tipo_tarjeta, 11, 3, 1, 1)


        self.main_layout.addWidget(self.grupo_gestion_partido)

        self.widget_reloj_container = QWidget(Resultados)
        self.widget_reloj_container.setObjectName(u"widget_reloj_container")
        self.widget_reloj_container.setMinimumSize(QSize(700, 0))

        self.main_layout.addWidget(self.widget_reloj_container)


        self.retranslateUi(Resultados)

        QMetaObject.connectSlotsByName(Resultados)
    # setupUi

    def retranslateUi(self, Resultados):
        self.grupo_gestion_partido.setTitle(QCoreApplication.translate("Resultados", u"Gesti\u00f3n de Partido", None))
        self.btn_anadir_tarjetas.setText(QCoreApplication.translate("Resultados", u"A\u00f1adir", None))
        self.label_jugador_gol.setText(QCoreApplication.translate("Resultados", u"Jugador", None))
        self.label_goles_registrados.setText(QCoreApplication.translate("Resultados", u"Goles registrados", None))
        self.label_tarjetas_registradas.setText(QCoreApplication.translate("Resultados", u"Tarjetas registradas", None))
        self.label_jugador_tarjeta.setText(QCoreApplication.translate("Resultados", u"Jugador", None))
        self.label_titulo.setText(QCoreApplication.translate("Resultados", u"Actualizaci\u00f3n de Resultados", None))
        ___qtablewidgetitem = self.table_tarjetas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Resultados", u"ID", None));
        ___qtablewidgetitem1 = self.table_tarjetas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Resultados", u"Jugador", None));
        ___qtablewidgetitem2 = self.table_tarjetas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Resultados", u"Tipo", None));
        ___qtablewidgetitem3 = self.table_tarjetas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Resultados", u"Minuto", None));
        self.btn_anadir_gol.setText(QCoreApplication.translate("Resultados", u"A\u00f1adir", None))
        self.btn_volver.setText(QCoreApplication.translate("Resultados", u"Volver", None))
        self.label_titulo_goles.setText(QCoreApplication.translate("Resultados", u"Registrar Goles", None))
        self.label_partido_y_equipos.setText(QCoreApplication.translate("Resultados", u"Partido y equipos", None))
        self.btn_finalizar_partido.setText(QCoreApplication.translate("Resultados", u"Partido jugado", None))
        ___qtablewidgetitem4 = self.table_goles.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Resultados", u"ID", None));
        ___qtablewidgetitem5 = self.table_goles.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Resultados", u"Jugador", None));
        ___qtablewidgetitem6 = self.table_goles.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Resultados", u"Minuto", None));
        self.label_registrar_tarjetas.setText(QCoreApplication.translate("Resultados", u"Registrar Tarjetas", None))
        self.label_seleccionar_partido.setText(QCoreApplication.translate("Resultados", u"Seleccionar partido", None))
        self.label_tipo_tarjeta.setText(QCoreApplication.translate("Resultados", u"Tipo", None))
        self.combo_tipo_tarjeta.setItemText(0, "")
        self.combo_tipo_tarjeta.setItemText(1, QCoreApplication.translate("Resultados", u"Amarilla", None))
        self.combo_tipo_tarjeta.setItemText(2, QCoreApplication.translate("Resultados", u"Roja", None))

        pass
    # retranslateUi

