# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowpqWYUi.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 20, 81, 31))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 60, 391, 31))
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 81, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 20, 91, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 61, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XES\u56fe\u5e8a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6240\u9009\u56fe\u7247\uff1a\u65e0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u4e00\u4e2a\u56fe\u7247\u5427", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u8def\u5f84\uff1a", None))
    # retranslateUi

