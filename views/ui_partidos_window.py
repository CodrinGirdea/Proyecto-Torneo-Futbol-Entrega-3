# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partidos_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QTimeEdit, QWidget)

class Ui_Gestion_de_partidos(object):
    def setupUi(self, Gestion_de_partidos):
        if not Gestion_de_partidos.objectName():
            Gestion_de_partidos.setObjectName(u"Gestion_de_partidos")
        Gestion_de_partidos.resize(920, 660)
        Gestion_de_partidos.setMinimumSize(QSize(920, 660))
        self.gridLayout_3 = QGridLayout(Gestion_de_partidos)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.table_partidos = QTableWidget(Gestion_de_partidos)
        if (self.table_partidos.columnCount() < 9):
            self.table_partidos.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_partidos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_partidos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_partidos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_partidos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_partidos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_partidos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_partidos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_partidos.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_partidos.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.table_partidos.setObjectName(u"table_partidos")

        self.gridLayout_3.addWidget(self.table_partidos, 3, 0, 1, 6)

        self.gb_resultado = QGroupBox(Gestion_de_partidos)
        self.gb_resultado.setObjectName(u"gb_resultado")
        self.gridLayout_2 = QGridLayout(self.gb_resultado)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spin_goles_visitante = QSpinBox(self.gb_resultado)
        self.spin_goles_visitante.setObjectName(u"spin_goles_visitante")

        self.gridLayout_2.addWidget(self.spin_goles_visitante, 0, 3, 1, 1)

        self.label_jugado = QLabel(self.gb_resultado)
        self.label_jugado.setObjectName(u"label_jugado")

        self.gridLayout_2.addWidget(self.label_jugado, 0, 4, 1, 1)

        self.spin_goles_local = QSpinBox(self.gb_resultado)
        self.spin_goles_local.setObjectName(u"spin_goles_local")

        self.gridLayout_2.addWidget(self.spin_goles_local, 0, 1, 1, 1)

        self.label_goles_visitante = QLabel(self.gb_resultado)
        self.label_goles_visitante.setObjectName(u"label_goles_visitante")

        self.gridLayout_2.addWidget(self.label_goles_visitante, 0, 2, 1, 1)

        self.check_jugado = QCheckBox(self.gb_resultado)
        self.check_jugado.setObjectName(u"check_jugado")

        self.gridLayout_2.addWidget(self.check_jugado, 0, 5, 1, 1)

        self.label_goles_local = QLabel(self.gb_resultado)
        self.label_goles_local.setObjectName(u"label_goles_local")

        self.gridLayout_2.addWidget(self.label_goles_local, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.gb_resultado, 5, 0, 1, 6)

        self.gb_programar_partido = QGroupBox(Gestion_de_partidos)
        self.gb_programar_partido.setObjectName(u"gb_programar_partido")
        self.gridLayout = QGridLayout(self.gb_programar_partido)
        self.gridLayout.setObjectName(u"gridLayout")
        self.combo_equipo_visitante = QComboBox(self.gb_programar_partido)
        self.combo_equipo_visitante.setObjectName(u"combo_equipo_visitante")

        self.gridLayout.addWidget(self.combo_equipo_visitante, 0, 5, 1, 3)

        self.label_hora = QLabel(self.gb_programar_partido)
        self.label_hora.setObjectName(u"label_hora")

        self.gridLayout.addWidget(self.label_hora, 1, 3, 1, 1)

        self.label_arbitro = QLabel(self.gb_programar_partido)
        self.label_arbitro.setObjectName(u"label_arbitro")

        self.gridLayout.addWidget(self.label_arbitro, 2, 5, 1, 1)

        self.input_hora = QTimeEdit(self.gb_programar_partido)
        self.input_hora.setObjectName(u"input_hora")

        self.gridLayout.addWidget(self.input_hora, 1, 4, 1, 3)

        self.label_equipo_local = QLabel(self.gb_programar_partido)
        self.label_equipo_local.setObjectName(u"label_equipo_local")

        self.gridLayout.addWidget(self.label_equipo_local, 0, 0, 1, 1)

        self.input_fecha = QDateEdit(self.gb_programar_partido)
        self.input_fecha.setObjectName(u"input_fecha")

        self.gridLayout.addWidget(self.input_fecha, 1, 1, 1, 2)

        self.combo_equipo_local = QComboBox(self.gb_programar_partido)
        self.combo_equipo_local.setObjectName(u"combo_equipo_local")
        self.combo_equipo_local.setMinimumSize(QSize(262, 0))

        self.gridLayout.addWidget(self.combo_equipo_local, 0, 1, 1, 3)

        self.label_eliminatoria = QLabel(self.gb_programar_partido)
        self.label_eliminatoria.setObjectName(u"label_eliminatoria")

        self.gridLayout.addWidget(self.label_eliminatoria, 2, 0, 1, 1)

        self.label_equipo_visitante = QLabel(self.gb_programar_partido)
        self.label_equipo_visitante.setObjectName(u"label_equipo_visitante")

        self.gridLayout.addWidget(self.label_equipo_visitante, 0, 4, 1, 1)

        self.label_fecha = QLabel(self.gb_programar_partido)
        self.label_fecha.setObjectName(u"label_fecha")

        self.gridLayout.addWidget(self.label_fecha, 1, 0, 1, 1)

        self.combo_arbitro = QComboBox(self.gb_programar_partido)
        self.combo_arbitro.setObjectName(u"combo_arbitro")

        self.gridLayout.addWidget(self.combo_arbitro, 2, 6, 1, 2)

        self.combo_eliminatoria = QComboBox(self.gb_programar_partido)
        self.combo_eliminatoria.addItem("")
        self.combo_eliminatoria.addItem("")
        self.combo_eliminatoria.addItem("")
        self.combo_eliminatoria.addItem("")
        self.combo_eliminatoria.addItem("")
        self.combo_eliminatoria.setObjectName(u"combo_eliminatoria")

        self.gridLayout.addWidget(self.combo_eliminatoria, 2, 1, 1, 4)


        self.gridLayout_3.addWidget(self.gb_programar_partido, 4, 0, 1, 6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_crear = QPushButton(Gestion_de_partidos)
        self.btn_crear.setObjectName(u"btn_crear")

        self.horizontalLayout.addWidget(self.btn_crear)

        self.btn_actualizar = QPushButton(Gestion_de_partidos)
        self.btn_actualizar.setObjectName(u"btn_actualizar")

        self.horizontalLayout.addWidget(self.btn_actualizar)

        self.btn_eliminar = QPushButton(Gestion_de_partidos)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.horizontalLayout.addWidget(self.btn_eliminar)

        self.btn_volver = QPushButton(Gestion_de_partidos)
        self.btn_volver.setObjectName(u"btn_volver")

        self.horizontalLayout.addWidget(self.btn_volver)

        self.btn_limpiar = QPushButton(Gestion_de_partidos)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.horizontalLayout.addWidget(self.btn_limpiar)


        self.gridLayout_3.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.label_subtitulo = QLabel(Gestion_de_partidos)
        self.label_subtitulo.setObjectName(u"label_subtitulo")
        font = QFont()
        font.setPointSize(12)
        self.label_subtitulo.setFont(font)

        self.gridLayout_3.addWidget(self.label_subtitulo, 2, 0, 1, 1)

        self.label_titulo = QLabel(Gestion_de_partidos)
        self.label_titulo.setObjectName(u"label_titulo")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_titulo.setFont(font1)

        self.gridLayout_3.addWidget(self.label_titulo, 1, 0, 1, 1)


        self.retranslateUi(Gestion_de_partidos)

        QMetaObject.connectSlotsByName(Gestion_de_partidos)
    # setupUi

    def retranslateUi(self, Gestion_de_partidos):
        Gestion_de_partidos.setWindowTitle(QCoreApplication.translate("Gestion_de_partidos", u"Form", None))
        ___qtablewidgetitem = self.table_partidos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Gestion_de_partidos", u"ID", None));
        ___qtablewidgetitem1 = self.table_partidos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Gestion_de_partidos", u"Equipo Local", None));
        ___qtablewidgetitem2 = self.table_partidos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Gestion_de_partidos", u"Equipo Visitante", None));
        ___qtablewidgetitem3 = self.table_partidos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Gestion_de_partidos", u"\u00c1rbitro", None));
        ___qtablewidgetitem4 = self.table_partidos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Gestion_de_partidos", u"Fecha", None));
        ___qtablewidgetitem5 = self.table_partidos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Gestion_de_partidos", u"Hora", None));
        ___qtablewidgetitem6 = self.table_partidos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Gestion_de_partidos", u"Eliminatoria", None));
        ___qtablewidgetitem7 = self.table_partidos.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Gestion_de_partidos", u"Resultado", None));
        ___qtablewidgetitem8 = self.table_partidos.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Gestion_de_partidos", u"Estado", None));
        self.gb_resultado.setTitle(QCoreApplication.translate("Gestion_de_partidos", u"Resultado", None))
        self.label_jugado.setText(QCoreApplication.translate("Gestion_de_partidos", u"           Jugado", None))
        self.label_goles_visitante.setText(QCoreApplication.translate("Gestion_de_partidos", u"Goles visitante", None))
        self.check_jugado.setText("")
        self.label_goles_local.setText(QCoreApplication.translate("Gestion_de_partidos", u"Goles local", None))
        self.gb_programar_partido.setTitle(QCoreApplication.translate("Gestion_de_partidos", u"Programar partido", None))
        self.label_hora.setText(QCoreApplication.translate("Gestion_de_partidos", u"Hora", None))
        self.label_arbitro.setText(QCoreApplication.translate("Gestion_de_partidos", u"\u00c1rbitro asignado", None))
        self.label_equipo_local.setText(QCoreApplication.translate("Gestion_de_partidos", u"Equipo local", None))
        self.label_eliminatoria.setText(QCoreApplication.translate("Gestion_de_partidos", u"Eliminatoria", None))
        self.label_equipo_visitante.setText(QCoreApplication.translate("Gestion_de_partidos", u"Equipo visitante", None))
        self.label_fecha.setText(QCoreApplication.translate("Gestion_de_partidos", u"Fecha", None))
        self.combo_eliminatoria.setItemText(0, "")
        self.combo_eliminatoria.setItemText(1, QCoreApplication.translate("Gestion_de_partidos", u"Octavos", None))
        self.combo_eliminatoria.setItemText(2, QCoreApplication.translate("Gestion_de_partidos", u"Cuartos", None))
        self.combo_eliminatoria.setItemText(3, QCoreApplication.translate("Gestion_de_partidos", u"Semifinal", None))
        self.combo_eliminatoria.setItemText(4, QCoreApplication.translate("Gestion_de_partidos", u"Final", None))

        self.btn_crear.setText(QCoreApplication.translate("Gestion_de_partidos", u"Crear partido", None))
        self.btn_actualizar.setText(QCoreApplication.translate("Gestion_de_partidos", u"Actualizar partido", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Gestion_de_partidos", u"Eliminar partido", None))
        self.btn_volver.setText(QCoreApplication.translate("Gestion_de_partidos", u"Volver", None))
        self.btn_limpiar.setText(QCoreApplication.translate("Gestion_de_partidos", u"Limpiar campos", None))
        self.label_subtitulo.setText(QCoreApplication.translate("Gestion_de_partidos", u"Tabla de Partidos", None))
        self.label_titulo.setText(QCoreApplication.translate("Gestion_de_partidos", u"Gesti\u00f3n de Partidos", None))
    # retranslateUi

