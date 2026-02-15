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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_idioma = QLabel(self.centralwidget)
        self.label_idioma.setObjectName(u"label_idioma")
        self.label_idioma.setGeometry(QRect(10, 10, 111, 16))
        self.label_eventos = QLabel(self.centralwidget)
        self.label_eventos.setObjectName(u"label_eventos")
        self.label_eventos.setGeometry(QRect(10, 145, 781, 81))
        font = QFont()
        font.setPointSize(22)
        self.label_eventos.setFont(font)
        self.grupo_reloj = QGroupBox(self.centralwidget)
        self.grupo_reloj.setObjectName(u"grupo_reloj")
        self.grupo_reloj.setGeometry(QRect(10, 240, 781, 156))
        self.gridLayout = QGridLayout(self.grupo_reloj)
        self.gridLayout.setObjectName(u"gridLayout")
        self.check_24h = QCheckBox(self.grupo_reloj)
        self.check_24h.setObjectName(u"check_24h")
        self.check_24h.setChecked(True)

        self.gridLayout.addWidget(self.check_24h, 0, 0, 1, 2)

        self.label_hora = QLabel(self.grupo_reloj)
        self.label_hora.setObjectName(u"label_hora")

        self.gridLayout.addWidget(self.label_hora, 1, 0, 1, 1)

        self.spin_hora = QSpinBox(self.grupo_reloj)
        self.spin_hora.setObjectName(u"spin_hora")
        self.spin_hora.setMaximum(59)

        self.gridLayout.addWidget(self.spin_hora, 1, 1, 1, 1)

        self.label_minuto = QLabel(self.grupo_reloj)
        self.label_minuto.setObjectName(u"label_minuto")

        self.gridLayout.addWidget(self.label_minuto, 1, 2, 1, 1)

        self.spin_minuto = QSpinBox(self.grupo_reloj)
        self.spin_minuto.setObjectName(u"spin_minuto")
        self.spin_minuto.setMaximum(59)

        self.gridLayout.addWidget(self.spin_minuto, 1, 3, 1, 1)

        self.label_mensaje = QLabel(self.grupo_reloj)
        self.label_mensaje.setObjectName(u"label_mensaje")

        self.gridLayout.addWidget(self.label_mensaje, 1, 4, 1, 1)

        self.input_mensaje = QLineEdit(self.grupo_reloj)
        self.input_mensaje.setObjectName(u"input_mensaje")

        self.gridLayout.addWidget(self.input_mensaje, 1, 5, 1, 1)

        self.btn_configurar_alarma = QPushButton(self.grupo_reloj)
        self.btn_configurar_alarma.setObjectName(u"btn_configurar_alarma")

        self.gridLayout.addWidget(self.btn_configurar_alarma, 2, 0, 1, 6)

        self.btn_modo_reloj = QPushButton(self.grupo_reloj)
        self.btn_modo_reloj.setObjectName(u"btn_modo_reloj")

        self.gridLayout.addWidget(self.btn_modo_reloj, 3, 0, 1, 6)

        self.grupo_timer = QGroupBox(self.centralwidget)
        self.grupo_timer.setObjectName(u"grupo_timer")
        self.grupo_timer.setGeometry(QRect(10, 400, 781, 151))
        self.gridLayout_2 = QGridLayout(self.grupo_timer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_duracion = QLabel(self.grupo_timer)
        self.label_duracion.setObjectName(u"label_duracion")

        self.gridLayout_2.addWidget(self.label_duracion, 0, 0, 1, 1)

        self.spin_duracion = QSpinBox(self.grupo_timer)
        self.spin_duracion.setObjectName(u"spin_duracion")
        self.spin_duracion.setMinimum(1)
        self.spin_duracion.setMaximum(86400)
        self.spin_duracion.setValue(60)

        self.gridLayout_2.addWidget(self.spin_duracion, 0, 1, 1, 1)

        self.check_regresivo = QCheckBox(self.grupo_timer)
        self.check_regresivo.setObjectName(u"check_regresivo")
        self.check_regresivo.setChecked(True)

        self.gridLayout_2.addWidget(self.check_regresivo, 0, 2, 1, 1)

        self.btn_modo_timer = QPushButton(self.grupo_timer)
        self.btn_modo_timer.setObjectName(u"btn_modo_timer")
        self.btn_modo_timer.setMinimumSize(QSize(121, 0))

        self.gridLayout_2.addWidget(self.btn_modo_timer, 1, 0, 1, 1)

        self.btn_iniciar = QPushButton(self.grupo_timer)
        self.btn_iniciar.setObjectName(u"btn_iniciar")

        self.gridLayout_2.addWidget(self.btn_iniciar, 1, 1, 1, 1)

        self.btn_pausar = QPushButton(self.grupo_timer)
        self.btn_pausar.setObjectName(u"btn_pausar")

        self.gridLayout_2.addWidget(self.btn_pausar, 1, 2, 1, 1)

        self.btn_reiniciar = QPushButton(self.grupo_timer)
        self.btn_reiniciar.setObjectName(u"btn_reiniciar")

        self.gridLayout_2.addWidget(self.btn_reiniciar, 1, 3, 1, 1)

        self.combo_idioma = QComboBox(self.centralwidget)
        self.combo_idioma.addItem("")
        self.combo_idioma.addItem("")
        self.combo_idioma.setObjectName(u"combo_idioma")
        self.combo_idioma.setGeometry(QRect(120, 10, 86, 21))
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_idioma.setText(QCoreApplication.translate("MainWindow", u"Idioma:", None))
        self.label_eventos.setText(QCoreApplication.translate("MainWindow", u"Esperando eventos...", None))
        self.grupo_reloj.setTitle(QCoreApplication.translate("MainWindow", u"Controles de Reloj", None))
        self.check_24h.setText(QCoreApplication.translate("MainWindow", u"Formato 24 Horas", None))
        self.label_hora.setText(QCoreApplication.translate("MainWindow", u"Hora Alarma:", None))
        self.label_minuto.setText(QCoreApplication.translate("MainWindow", u"Minuto:", None))
        self.label_mensaje.setText(QCoreApplication.translate("MainWindow", u"Mensaje:", None))
        self.input_mensaje.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u00a1Alarma activada!", None))
        self.btn_configurar_alarma.setText(QCoreApplication.translate("MainWindow", u"Configurar Alarma", None))
        self.btn_modo_reloj.setText(QCoreApplication.translate("MainWindow", u"Cambiar a Modo Reloj", None))
        self.grupo_timer.setTitle(QCoreApplication.translate("MainWindow", u"Controles de Temporizador", None))
        self.label_duracion.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n (segundos):", None))
        self.check_regresivo.setText(QCoreApplication.translate("MainWindow", u"Regresivo", None))
        self.btn_modo_timer.setText(QCoreApplication.translate("MainWindow", u"Cambiar a Modo Timer", None))
        self.btn_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.btn_pausar.setText(QCoreApplication.translate("MainWindow", u"Pausar", None))
        self.btn_reiniciar.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.combo_idioma.setItemText(0, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.combo_idioma.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))

    # retranslateUi

