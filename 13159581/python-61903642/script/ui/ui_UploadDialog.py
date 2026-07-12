# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_UploadDialogZruTxV.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QProgressBar,
    QSizePolicy, QWidget)

class Ui_UploadDialog(object):
    def setupUi(self, DownloadDialog):
        if not DownloadDialog.objectName():
            DownloadDialog.setObjectName(u"DownloadDialog")
        DownloadDialog.resize(302, 186)
        self.progressBar = QProgressBar(DownloadDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 100, 261, 31))
        self.progressBar.setValue(0)
        self.label = QLabel(DownloadDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 231, 41))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(DownloadDialog)

        QMetaObject.connectSlotsByName(DownloadDialog)
    # setupUi

    def retranslateUi(self, DownloadDialog):
        DownloadDialog.setWindowTitle(QCoreApplication.translate("DownloadDialog", u"\u4e0a\u4f20", None))
        self.label.setText("")
    # retranslateUi

