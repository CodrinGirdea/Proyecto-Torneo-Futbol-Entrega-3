# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clasificacion_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Eliminatoria(object):
    def setupUi(self, Eliminatoria):
        if not Eliminatoria.objectName():
            Eliminatoria.setObjectName(u"Eliminatoria")
        Eliminatoria.resize(818, 686)
        Eliminatoria.setMaximumSize(QSize(1231323, 16777215))
        self.gridLayout = QGridLayout(Eliminatoria)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_titulo = QLabel(Eliminatoria)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_titulo.setFont(font)

        self.gridLayout.addWidget(self.label_titulo, 0, 0, 1, 2)

        self.graphics_view_bracket = QGraphicsView(Eliminatoria)
        self.graphics_view_bracket.setObjectName(u"graphics_view_bracket")
        self.graphics_view_bracket.setMinimumSize(QSize(800, 600))

        self.gridLayout.addWidget(self.graphics_view_bracket, 1, 0, 1, 2)

        self.btn_actualizar = QPushButton(Eliminatoria)
        self.btn_actualizar.setObjectName(u"btn_actualizar")

        self.gridLayout.addWidget(self.btn_actualizar, 2, 0, 1, 1)

        self.btn_volver = QPushButton(Eliminatoria)
        self.btn_volver.setObjectName(u"btn_volver")

        self.gridLayout.addWidget(self.btn_volver, 2, 1, 1, 1)


        self.retranslateUi(Eliminatoria)

        QMetaObject.connectSlotsByName(Eliminatoria)
    # setupUi

    def retranslateUi(self, Eliminatoria):
        Eliminatoria.setWindowTitle(QCoreApplication.translate("Eliminatoria", u"Form", None))
        self.label_titulo.setText(QCoreApplication.translate("Eliminatoria", u"Eliminatorias", None))
        self.btn_actualizar.setText(QCoreApplication.translate("Eliminatoria", u"Actualizar", None))
        self.btn_volver.setText(QCoreApplication.translate("Eliminatoria", u"Volver", None))
    # retranslateUi

