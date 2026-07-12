# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_PreviewDialogXuihIE.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_PreviewDialog(object):
    def setupUi(self, PreviewDialog):
        if not PreviewDialog.objectName():
            PreviewDialog.setObjectName(u"PreviewDialog")
        PreviewDialog.resize(400, 302)
        PreviewDialog.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        # self.PreviewWidget = QTextBrowser(PreviewDialog)
        # self.PreviewWidget.setObjectName(u"PreviewWidget")
        # self.PreviewWidget.setGeometry(QRect(10, 10, 381, 281))

        self.retranslateUi(PreviewDialog)

        QMetaObject.connectSlotsByName(PreviewDialog)
    # setupUi

    def retranslateUi(self, PreviewDialog):
        PreviewDialog.setWindowTitle(QCoreApplication.translate("PreviewDialog", u"\u9884\u89c8", None))
    # retranslateUi

