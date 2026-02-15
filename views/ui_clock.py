# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clock.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Clock(object):
    def setupUi(self, Clock):
        if not Clock.objectName():
            Clock.setObjectName(u"Clock")
        Clock.resize(928, 605)
        font = QFont()
        font.setBold(True)
        Clock.setFont(font)
        self.gridLayout = QGridLayout(Clock)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Clock)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(36)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(Clock)

        QMetaObject.connectSlotsByName(Clock)
    # setupUi

    def retranslateUi(self, Clock):
        Clock.setWindowTitle(QCoreApplication.translate("Clock", u"Form", None))
        self.label.setText(QCoreApplication.translate("Clock", u"00:00:00", None))
    # retranslateUi

