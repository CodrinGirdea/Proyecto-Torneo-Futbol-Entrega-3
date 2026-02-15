# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'creditos_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Creditos(object):
    def setupUi(self, Creditos):
        if not Creditos.objectName():
            Creditos.setObjectName(u"Creditos")
        Creditos.resize(282, 340)
        self.verticalLayout = QVBoxLayout(Creditos)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(Creditos)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(18)
        self.label_titulo.setFont(font)

        self.verticalLayout.addWidget(self.label_titulo)

        self.label_subtitulo = QLabel(Creditos)
        self.label_subtitulo.setObjectName(u"label_subtitulo")

        self.verticalLayout.addWidget(self.label_subtitulo)

        self.label_version = QLabel(Creditos)
        self.label_version.setObjectName(u"label_version")

        self.verticalLayout.addWidget(self.label_version)

        self.label_autor = QLabel(Creditos)
        self.label_autor.setObjectName(u"label_autor")

        self.verticalLayout.addWidget(self.label_autor)

        self.label_fecha = QLabel(Creditos)
        self.label_fecha.setObjectName(u"label_fecha")

        self.verticalLayout.addWidget(self.label_fecha)

        self.label_instituto = QLabel(Creditos)
        self.label_instituto.setObjectName(u"label_instituto")

        self.verticalLayout.addWidget(self.label_instituto)

        self.btn_cerrar = QPushButton(Creditos)
        self.btn_cerrar.setObjectName(u"btn_cerrar")

        self.verticalLayout.addWidget(self.btn_cerrar)


        self.retranslateUi(Creditos)

        QMetaObject.connectSlotsByName(Creditos)
    # setupUi

    def retranslateUi(self, Creditos):
        Creditos.setWindowTitle(QCoreApplication.translate("Creditos", u"Form", None))
        self.label_titulo.setText(QCoreApplication.translate("Creditos", u"Cr\u00e9ditos", None))
        self.label_subtitulo.setText(QCoreApplication.translate("Creditos", u"Sistema de Gesti\u00f3n de Torneo de F\u00fatbol", None))
        self.label_version.setText(QCoreApplication.translate("Creditos", u"Version 3.0", None))
        self.label_autor.setText(QCoreApplication.translate("Creditos", u"Desarrollado por: \n"
" Codrin Girdea", None))
        self.label_fecha.setText(QCoreApplication.translate("Creditos", u"Fecha: Enero 2026", None))
        self.label_instituto.setText(QCoreApplication.translate("Creditos", u"Proyecto de Dise\u00f1o de Interfaces\n"
" 2\u00ba DAM - IES Brianda de Mendoza", None))
        self.btn_cerrar.setText(QCoreApplication.translate("Creditos", u"Cerrar", None))
    # retranslateUi

