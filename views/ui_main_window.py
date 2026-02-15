# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(self.centralwidget)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(19)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_titulo)

        self.btn_equipos = QPushButton(self.centralwidget)
        self.btn_equipos.setObjectName(u"btn_equipos")
        self.btn_equipos.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.btn_equipos)

        self.btn_participantes = QPushButton(self.centralwidget)
        self.btn_participantes.setObjectName(u"btn_participantes")
        self.btn_participantes.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.btn_participantes)

        self.btn_partidos = QPushButton(self.centralwidget)
        self.btn_partidos.setObjectName(u"btn_partidos")
        self.btn_partidos.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.btn_partidos)

        self.btn_resultados = QPushButton(self.centralwidget)
        self.btn_resultados.setObjectName(u"btn_resultados")
        self.btn_resultados.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.btn_resultados)

        self.btn_clasificacion = QPushButton(self.centralwidget)
        self.btn_clasificacion.setObjectName(u"btn_clasificacion")
        self.btn_clasificacion.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.btn_clasificacion)

        self.btn_creditos = QPushButton(self.centralwidget)
        self.btn_creditos.setObjectName(u"btn_creditos")
        self.btn_creditos.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.btn_creditos)

        self.btn_ayuda = QPushButton(self.centralwidget)
        self.btn_ayuda.setObjectName(u"btn_ayuda")
        self.btn_ayuda.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.btn_ayuda)

        self.btn_exportar = QPushButton(self.centralwidget)
        self.btn_exportar.setObjectName(u"btn_exportar")
        self.btn_exportar.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.btn_exportar)

        self.btn_informes = QPushButton(self.centralwidget)
        self.btn_informes.setObjectName(u"btn_informes")
        self.btn_informes.setMinimumSize(QSize(250, 40))
        self.btn_informes.setText("Generar Informes")

        self.verticalLayout.addWidget(self.btn_informes)

        self.btn_salir = QPushButton(self.centralwidget)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setMinimumSize(QSize(250, 40))

        self.verticalLayout.addWidget(self.btn_salir)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"Sistema de Gesti\u00f3n de Torneo de F\u00fatbol", None))
        self.btn_equipos.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Equipos", None))
        self.btn_participantes.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Participantes", None))
        self.btn_partidos.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Partidos", None))
        self.btn_resultados.setText(QCoreApplication.translate("MainWindow", u"Actualizar Resultados", None))
        self.btn_clasificacion.setText(QCoreApplication.translate("MainWindow", u"Clasificaci\u00f3n/Eliminatorias", None))
        self.btn_creditos.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9ditos", None))
        self.btn_ayuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.btn_exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar datos", None))
        self.btn_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

