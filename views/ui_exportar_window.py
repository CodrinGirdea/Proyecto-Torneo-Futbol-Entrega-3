# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exportar_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ExportarWindow(object):
    def setupUi(self, ExportarWindow):
        if not ExportarWindow.objectName():
            ExportarWindow.setObjectName(u"ExportarWindow")
        ExportarWindow.resize(650, 600)
        ExportarWindow.setMinimumSize(QSize(650, 600))
        ExportarWindow.setMaximumSize(QSize(650, 600))
        self.verticalLayout = QVBoxLayout(ExportarWindow)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, 25, 25, 25)
        self.label_titulo = QLabel(ExportarWindow)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_titulo)

        self.groupBox_estadisticas = QGroupBox(ExportarWindow)
        self.groupBox_estadisticas.setObjectName(u"groupBox_estadisticas")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_estadisticas)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_clasificacion = QPushButton(self.groupBox_estadisticas)
        self.btn_clasificacion.setObjectName(u"btn_clasificacion")
        self.btn_clasificacion.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.btn_clasificacion)

        self.btn_goleadores = QPushButton(self.groupBox_estadisticas)
        self.btn_goleadores.setObjectName(u"btn_goleadores")
        self.btn_goleadores.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.btn_goleadores)

        self.btn_tarjetas = QPushButton(self.groupBox_estadisticas)
        self.btn_tarjetas.setObjectName(u"btn_tarjetas")
        self.btn_tarjetas.setMinimumSize(QSize(0, 50))

        self.verticalLayout_2.addWidget(self.btn_tarjetas)


        self.verticalLayout.addWidget(self.groupBox_estadisticas)

        self.groupBox_partidos = QGroupBox(ExportarWindow)
        self.groupBox_partidos.setObjectName(u"groupBox_partidos")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_partidos)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_partidos_jugados = QPushButton(self.groupBox_partidos)
        self.btn_partidos_jugados.setObjectName(u"btn_partidos_jugados")
        self.btn_partidos_jugados.setMinimumSize(QSize(0, 50))

        self.verticalLayout_3.addWidget(self.btn_partidos_jugados)

        self.btn_calendario = QPushButton(self.groupBox_partidos)
        self.btn_calendario.setObjectName(u"btn_calendario")
        self.btn_calendario.setMinimumSize(QSize(0, 50))

        self.verticalLayout_3.addWidget(self.btn_calendario)


        self.verticalLayout.addWidget(self.groupBox_partidos)

        self.groupBox_general = QGroupBox(ExportarWindow)
        self.groupBox_general.setObjectName(u"groupBox_general")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_general)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_jugadores = QPushButton(self.groupBox_general)
        self.btn_jugadores.setObjectName(u"btn_jugadores")
        self.btn_jugadores.setMinimumSize(QSize(0, 50))

        self.verticalLayout_4.addWidget(self.btn_jugadores)


        self.verticalLayout.addWidget(self.groupBox_general)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_volver = QPushButton(ExportarWindow)
        self.btn_volver.setObjectName(u"btn_volver")
        self.btn_volver.setMinimumSize(QSize(0, 45))

        self.verticalLayout.addWidget(self.btn_volver)


        self.retranslateUi(ExportarWindow)

        QMetaObject.connectSlotsByName(ExportarWindow)
    # setupUi

    def retranslateUi(self, ExportarWindow):
        ExportarWindow.setWindowTitle(QCoreApplication.translate("ExportarWindow", u"Exportar Datos a CSV", None))
        self.label_titulo.setText(QCoreApplication.translate("ExportarWindow", u"Exportar Datos del Torneo a CSV", None))
        self.groupBox_estadisticas.setTitle(QCoreApplication.translate("ExportarWindow", u"Estad\u00edsticas y Clasificaci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btn_clasificacion.setToolTip(QCoreApplication.translate("ExportarWindow", u"Exporta la tabla de clasificaci\u00f3n con estad\u00edsticas de cada equipo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_clasificacion.setText(QCoreApplication.translate("ExportarWindow", u"Exportar Clasificaci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btn_goleadores.setToolTip(QCoreApplication.translate("ExportarWindow", u"Exporta la tabla de goleadores del torneo", None))
#endif // QT_CONFIG(tooltip)
        self.btn_goleadores.setText(QCoreApplication.translate("ExportarWindow", u"Exportar Goleadores", None))
#if QT_CONFIG(tooltip)
        self.btn_tarjetas.setToolTip(QCoreApplication.translate("ExportarWindow", u"Exporta estad\u00edsticas de tarjetas por jugador", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tarjetas.setText(QCoreApplication.translate("ExportarWindow", u" Exportar Tarjetas", None))
        self.groupBox_partidos.setTitle(QCoreApplication.translate("ExportarWindow", u"Partidos y Calendario", None))
#if QT_CONFIG(tooltip)
        self.btn_partidos_jugados.setToolTip(QCoreApplication.translate("ExportarWindow", u"Exporta solo los partidos que ya se han jugado", None))
#endif // QT_CONFIG(tooltip)
        self.btn_partidos_jugados.setText(QCoreApplication.translate("ExportarWindow", u"Exportar Partidos Jugados", None))
#if QT_CONFIG(tooltip)
        self.btn_calendario.setToolTip(QCoreApplication.translate("ExportarWindow", u"Exporta todos los partidos (jugados y pendientes)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_calendario.setText(QCoreApplication.translate("ExportarWindow", u"Exportar Calendario Completo", None))
        self.groupBox_general.setTitle(QCoreApplication.translate("ExportarWindow", u"Datos Generales", None))
#if QT_CONFIG(tooltip)
        self.btn_jugadores.setToolTip(QCoreApplication.translate("ExportarWindow", u"Exporta la lista completa de jugadores con sus estad\u00edsticas", None))
#endif // QT_CONFIG(tooltip)
        self.btn_jugadores.setText(QCoreApplication.translate("ExportarWindow", u"Exportar Jugadores", None))
#if QT_CONFIG(tooltip)
        self.btn_volver.setToolTip(QCoreApplication.translate("ExportarWindow", u"Volver al men\u00fa principal", None))
#endif // QT_CONFIG(tooltip)
        self.btn_volver.setText(QCoreApplication.translate("ExportarWindow", u"Volver al Men\u00fa Principal", None))
    # retranslateUi

