# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equipos_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 598)
        Form.setMaximumSize(QSize(600, 600))
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_titulo = QLabel(Form)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_titulo.setFont(font)

        self.gridLayout_2.addWidget(self.label_titulo, 0, 0, 1, 1)

        self.table_equipos = QTableWidget(Form)
        if (self.table_equipos.columnCount() < 4):
            self.table_equipos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_equipos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_equipos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_equipos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_equipos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_equipos.setObjectName(u"table_equipos")
        self.table_equipos.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_equipos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.gridLayout_2.addWidget(self.table_equipos, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_nombre = QLabel(Form)
        self.label_nombre.setObjectName(u"label_nombre")

        self.gridLayout.addWidget(self.label_nombre, 0, 0, 1, 1)

        self.label_curso = QLabel(Form)
        self.label_curso.setObjectName(u"label_curso")

        self.gridLayout.addWidget(self.label_curso, 1, 0, 1, 1)

        self.label_color_camiseta = QLabel(Form)
        self.label_color_camiseta.setObjectName(u"label_color_camiseta")

        self.gridLayout.addWidget(self.label_color_camiseta, 2, 0, 1, 1)

        self.label_escudo = QLabel(Form)
        self.label_escudo.setObjectName(u"label_escudo")

        self.gridLayout.addWidget(self.label_escudo, 3, 0, 1, 1)

        self.input_escudo = QLineEdit(Form)
        self.input_escudo.setObjectName(u"input_escudo")

        self.gridLayout.addWidget(self.input_escudo, 3, 1, 1, 1)

        self.btn_seleccionar_escudo = QPushButton(Form)
        self.btn_seleccionar_escudo.setObjectName(u"btn_seleccionar_escudo")
        self.btn_seleccionar_escudo.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.btn_seleccionar_escudo, 3, 2, 1, 1)

        self.input_color = QLineEdit(Form)
        self.input_color.setObjectName(u"input_color")

        self.gridLayout.addWidget(self.input_color, 2, 1, 1, 1)

        self.input_curso = QLineEdit(Form)
        self.input_curso.setObjectName(u"input_curso")

        self.gridLayout.addWidget(self.input_curso, 1, 1, 1, 1)

        self.input_nombre = QLineEdit(Form)
        self.input_nombre.setObjectName(u"input_nombre")

        self.gridLayout.addWidget(self.input_nombre, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_crear = QPushButton(Form)
        self.btn_crear.setObjectName(u"btn_crear")

        self.horizontalLayout.addWidget(self.btn_crear)

        self.btn_limpiar = QPushButton(Form)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.horizontalLayout.addWidget(self.btn_limpiar)

        self.btn_actualizar = QPushButton(Form)
        self.btn_actualizar.setObjectName(u"btn_actualizar")

        self.horizontalLayout.addWidget(self.btn_actualizar)

        self.btn_volver = QPushButton(Form)
        self.btn_volver.setObjectName(u"btn_volver")

        self.horizontalLayout.addWidget(self.btn_volver)

        self.btn_eliminar = QPushButton(Form)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.horizontalLayout.addWidget(self.btn_eliminar)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_titulo.setText(QCoreApplication.translate("Form", u"Gesti\u00f3n de Equipos", None))
        ___qtablewidgetitem = self.table_equipos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.table_equipos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem2 = self.table_equipos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Curso", None));
        ___qtablewidgetitem3 = self.table_equipos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Color Camiseta", None));
        self.label_nombre.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_curso.setText(QCoreApplication.translate("Form", u"Curso", None))
        self.label_color_camiseta.setText(QCoreApplication.translate("Form", u"Color Camiseta", None))
        self.label_escudo.setText(QCoreApplication.translate("Form", u"Escudo", None))
        self.btn_seleccionar_escudo.setText(QCoreApplication.translate("Form", u"Seleccionar Imagen", None))
        self.btn_crear.setText(QCoreApplication.translate("Form", u"Crear Equipo", None))
        self.btn_limpiar.setText(QCoreApplication.translate("Form", u"Limpiar Campos", None))
        self.btn_actualizar.setText(QCoreApplication.translate("Form", u"Actualizar Equipo", None))
        self.btn_volver.setText(QCoreApplication.translate("Form", u"Volver", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Form", u"Eliminar Equipo", None))
    # retranslateUi

