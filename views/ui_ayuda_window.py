# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ayuda_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 462)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(Form)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(18)
        self.label_titulo.setFont(font)

        self.verticalLayout.addWidget(self.label_titulo)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.plainTextEdit_2 = QPlainTextEdit(Form)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_2)

        self.plainTextEdit_3 = QPlainTextEdit(Form)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_3)

        self.plainTextEdit_4 = QPlainTextEdit(Form)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_4)

        self.plainTextEdit_5 = QPlainTextEdit(Form)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit_5)

        self.btn_cerrar = QPushButton(Form)
        self.btn_cerrar.setObjectName(u"btn_cerrar")

        self.verticalLayout.addWidget(self.btn_cerrar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_titulo.setText(QCoreApplication.translate("Form", u"Ayuda", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Instrucciones de uso", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Form", u" 1. Gesti\u00f3n de Equipos:                       \n"
"     - Crea los equipos del torneo             \n"
"     - Asigna nombre, curso y colores ", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("Form", u"2. Gesti\u00f3n de Participantes:                 \n"
"     - Registra jugadores y \u00e1rbitros           \n"
"     - Asigna jugadores a sus equipos", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("Form", u"3. Gesti\u00f3n de Partidos:                      \n"
"     - Programa los partidos del torneo        \n"
"     - Asigna equipos, \u00e1rbitros y fechas", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("Form", u"4. Actualizaci\u00f3n de Resultados:              \n"
"      - Registra goles y tarjetas               \n"
"      - Marca partidos como jugados", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("Form", u"5. Clasificaci\u00f3n/Eliminatorias:              \n"
"      - Visualiza el cuadro del torneo", None))
        self.btn_cerrar.setText(QCoreApplication.translate("Form", u"Cerrar", None))
    # retranslateUi

