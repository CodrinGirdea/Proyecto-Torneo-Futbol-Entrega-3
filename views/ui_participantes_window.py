# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'participantes_window.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Gestion_de_participantes(object):
    def setupUi(self, Gestion_de_participantes):
        if not Gestion_de_participantes.objectName():
            Gestion_de_participantes.setObjectName(u"Gestion_de_participantes")
        Gestion_de_participantes.resize(800, 580)
        Gestion_de_participantes.setMinimumSize(QSize(800, 580))
        Gestion_de_participantes.setMaximumSize(QSize(800, 900))
        self.gridLayout_2 = QGridLayout(Gestion_de_participantes)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_subtitulo = QLabel(Gestion_de_participantes)
        self.label_subtitulo.setObjectName(u"label_subtitulo")
        font = QFont()
        font.setPointSize(12)
        self.label_subtitulo.setFont(font)

        self.gridLayout_2.addWidget(self.label_subtitulo, 1, 0, 1, 1)

        self.table_participantes = QTableWidget(Gestion_de_participantes)
        if (self.table_participantes.columnCount() < 7):
            self.table_participantes.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_participantes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_participantes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_participantes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_participantes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_participantes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_participantes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_participantes.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_participantes.setObjectName(u"table_participantes")

        self.gridLayout_2.addWidget(self.table_participantes, 2, 0, 1, 2)

        self.groupBox = QGroupBox(Gestion_de_participantes)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_nombre = QLabel(self.groupBox)
        self.label_nombre.setObjectName(u"label_nombre")

        self.gridLayout.addWidget(self.label_nombre, 0, 0, 1, 1)

        self.input_nombre = QLineEdit(self.groupBox)
        self.input_nombre.setObjectName(u"input_nombre")

        self.gridLayout.addWidget(self.input_nombre, 0, 1, 1, 2)

        self.label_tipo = QLabel(self.groupBox)
        self.label_tipo.setObjectName(u"label_tipo")

        self.gridLayout.addWidget(self.label_tipo, 0, 3, 1, 1)

        self.check_es_jugador = QCheckBox(self.groupBox)
        self.check_es_jugador.setObjectName(u"check_es_jugador")

        self.gridLayout.addWidget(self.check_es_jugador, 0, 4, 1, 2)

        self.check_es_arbitro = QCheckBox(self.groupBox)
        self.check_es_arbitro.setObjectName(u"check_es_arbitro")

        self.gridLayout.addWidget(self.check_es_arbitro, 0, 6, 1, 1)

        self.label_fecha_nac = QLabel(self.groupBox)
        self.label_fecha_nac.setObjectName(u"label_fecha_nac")

        self.gridLayout.addWidget(self.label_fecha_nac, 1, 0, 1, 1)

        self.input_fecha_nac = QDateEdit(self.groupBox)
        self.input_fecha_nac.setObjectName(u"input_fecha_nac")

        self.gridLayout.addWidget(self.input_fecha_nac, 1, 1, 1, 2)

        self.label_curso = QLabel(self.groupBox)
        self.label_curso.setObjectName(u"label_curso")

        self.gridLayout.addWidget(self.label_curso, 1, 3, 1, 1)

        self.input_curso = QLineEdit(self.groupBox)
        self.input_curso.setObjectName(u"input_curso")

        self.gridLayout.addWidget(self.input_curso, 1, 5, 1, 2)

        self.label_posicion = QLabel(self.groupBox)
        self.label_posicion.setObjectName(u"label_posicion")

        self.gridLayout.addWidget(self.label_posicion, 2, 0, 1, 1)

        self.combo_posicion = QComboBox(self.groupBox)
        self.combo_posicion.addItem("")
        self.combo_posicion.addItem("")
        self.combo_posicion.addItem("")
        self.combo_posicion.addItem("")
        self.combo_posicion.addItem("")
        self.combo_posicion.setObjectName(u"combo_posicion")

        self.gridLayout.addWidget(self.combo_posicion, 2, 1, 1, 2)

        self.label_equipo = QLabel(self.groupBox)
        self.label_equipo.setObjectName(u"label_equipo")

        self.gridLayout.addWidget(self.label_equipo, 2, 3, 1, 1)

        self.combo_equipo = QComboBox(self.groupBox)
        self.combo_equipo.setObjectName(u"combo_equipo")

        self.gridLayout.addWidget(self.combo_equipo, 2, 5, 1, 2)

        self.label_t_amarillas = QLabel(self.groupBox)
        self.label_t_amarillas.setObjectName(u"label_t_amarillas")

        self.gridLayout.addWidget(self.label_t_amarillas, 3, 0, 1, 2)

        self.spin_t_amarillas = QSpinBox(self.groupBox)
        self.spin_t_amarillas.setObjectName(u"spin_t_amarillas")

        self.gridLayout.addWidget(self.spin_t_amarillas, 3, 2, 1, 1)

        self.label_t_rojas = QLabel(self.groupBox)
        self.label_t_rojas.setObjectName(u"label_t_rojas")

        self.gridLayout.addWidget(self.label_t_rojas, 3, 3, 1, 2)

        self.spin_t_rojas = QSpinBox(self.groupBox)
        self.spin_t_rojas.setObjectName(u"spin_t_rojas")

        self.gridLayout.addWidget(self.spin_t_rojas, 3, 5, 1, 1)

        self.label_goles = QLabel(self.groupBox)
        self.label_goles.setObjectName(u"label_goles")

        self.gridLayout.addWidget(self.label_goles, 4, 0, 1, 1)

        self.spin_goles = QSpinBox(self.groupBox)
        self.spin_goles.setObjectName(u"spin_goles")

        self.gridLayout.addWidget(self.spin_goles, 4, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_actualizar = QPushButton(Gestion_de_participantes)
        self.btn_actualizar.setObjectName(u"btn_actualizar")

        self.horizontalLayout.addWidget(self.btn_actualizar)

        self.btn_crear = QPushButton(Gestion_de_participantes)
        self.btn_crear.setObjectName(u"btn_crear")

        self.horizontalLayout.addWidget(self.btn_crear)

        self.btn_eliminar = QPushButton(Gestion_de_participantes)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.horizontalLayout.addWidget(self.btn_eliminar)

        self.btn_limpiar = QPushButton(Gestion_de_participantes)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.horizontalLayout.addWidget(self.btn_limpiar)

        self.btn_volver = QPushButton(Gestion_de_participantes)
        self.btn_volver.setObjectName(u"btn_volver")

        self.horizontalLayout.addWidget(self.btn_volver)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 2)

        self.label_titulo = QLabel(Gestion_de_participantes)
        self.label_titulo.setObjectName(u"label_titulo")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_titulo.setFont(font1)

        self.gridLayout_2.addWidget(self.label_titulo, 0, 0, 1, 1)


        self.retranslateUi(Gestion_de_participantes)

        QMetaObject.connectSlotsByName(Gestion_de_participantes)
    # setupUi

    def retranslateUi(self, Gestion_de_participantes):
        Gestion_de_participantes.setWindowTitle(QCoreApplication.translate("Gestion_de_participantes", u"Form", None))
        self.label_subtitulo.setText(QCoreApplication.translate("Gestion_de_participantes", u"Tabla de participantes", None))
        ___qtablewidgetitem = self.table_participantes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Gestion_de_participantes", u" ID", None));
        ___qtablewidgetitem1 = self.table_participantes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Gestion_de_participantes", u"Nombre", None));
        ___qtablewidgetitem2 = self.table_participantes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Gestion_de_participantes", u"Fecha Nac", None));
        ___qtablewidgetitem3 = self.table_participantes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Gestion_de_participantes", u"Curso", None));
        ___qtablewidgetitem4 = self.table_participantes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Gestion_de_participantes", u"Tipo ", None));
        ___qtablewidgetitem5 = self.table_participantes.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Gestion_de_participantes", u"Posici\u00f3n", None));
        ___qtablewidgetitem6 = self.table_participantes.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Gestion_de_participantes", u"Equipo", None));
        self.groupBox.setTitle(QCoreApplication.translate("Gestion_de_participantes", u"Formulario de datos", None))
        self.label_nombre.setText(QCoreApplication.translate("Gestion_de_participantes", u"Nombre", None))
        self.label_tipo.setText(QCoreApplication.translate("Gestion_de_participantes", u"Tipo", None))
        self.check_es_jugador.setText(QCoreApplication.translate("Gestion_de_participantes", u"Jugador", None))
        self.check_es_arbitro.setText(QCoreApplication.translate("Gestion_de_participantes", u"Arbitro", None))
        self.label_fecha_nac.setText(QCoreApplication.translate("Gestion_de_participantes", u"Fecha Nac", None))
        self.label_curso.setText(QCoreApplication.translate("Gestion_de_participantes", u"Curso", None))
        self.label_posicion.setText(QCoreApplication.translate("Gestion_de_participantes", u"Posicion", None))
        self.combo_posicion.setItemText(0, "")
        self.combo_posicion.setItemText(1, QCoreApplication.translate("Gestion_de_participantes", u"Portero", None))
        self.combo_posicion.setItemText(2, QCoreApplication.translate("Gestion_de_participantes", u"Defensa", None))
        self.combo_posicion.setItemText(3, QCoreApplication.translate("Gestion_de_participantes", u"Centrocampista", None))
        self.combo_posicion.setItemText(4, QCoreApplication.translate("Gestion_de_participantes", u"Delantero", None))

        self.label_equipo.setText(QCoreApplication.translate("Gestion_de_participantes", u"Equipo", None))
        self.label_t_amarillas.setText(QCoreApplication.translate("Gestion_de_participantes", u"Tarjetas amarillas", None))
        self.label_t_rojas.setText(QCoreApplication.translate("Gestion_de_participantes", u"Tarjetas rojas", None))
        self.label_goles.setText(QCoreApplication.translate("Gestion_de_participantes", u"Goles", None))
        self.btn_actualizar.setText(QCoreApplication.translate("Gestion_de_participantes", u"Actualizar Participante", None))
        self.btn_crear.setText(QCoreApplication.translate("Gestion_de_participantes", u"Crear Participante", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Gestion_de_participantes", u"Eliminar Participante", None))
        self.btn_limpiar.setText(QCoreApplication.translate("Gestion_de_participantes", u"Limpiar Campos", None))
        self.btn_volver.setText(QCoreApplication.translate("Gestion_de_participantes", u"Volver", None))
        self.label_titulo.setText(QCoreApplication.translate("Gestion_de_participantes", u"Gesti\u00f3n de Participantes", None))
    # retranslateUi

