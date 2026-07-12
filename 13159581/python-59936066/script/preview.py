from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView
from ui.ui_PreviewDialog import Ui_PreviewDialog
from typing import List
import requests

class PreviewDialog(QDialog, Ui_PreviewDialog):
    def __init__(self, parent=None, file_link: str = ""):
        super().__init__(parent)
        self.setupUi(self)

        # 支持的图片格式列表
        image_formats: List[str] = ["jpg", "png", "jpeg", "gif", "svg"]
        # 支持的文本格式列表
        text_formats: List[str] = ["txt", "py", "java", "c", "cpp", "html", "css", "js"]

        # 获取文件扩展名
        file_extension: str = file_link.split(".")[-1]

        if file_extension in image_formats:
            # 如果是图片格式，使用QWebEngineView来显示
            self.PreviewWidget = QWebEngineView(self)
            self.PreviewWidget.setUrl(QUrl(file_link))
            self.PreviewWidget.setObjectName(u"PreviewWidget")
            self.PreviewWidget.setGeometry(QRect(10, 10, 381, 281))
        elif file_extension in text_formats:
            # 如果是文本格式，使用QTextBrowser来显示
            self.PreviewWidget = QTextBrowser(self)
            try:
                response = requests.get(file_link)
                response.raise_for_status()
                text: str = response.content.decode("utf-8")
                self.PreviewWidget.setText(text)
            except requests.RequestException as e:
                self.PreviewWidget.setText(f"无法加载文件: {str(e)}")
            self.PreviewWidget.setObjectName(u"PreviewWidget")
            self.PreviewWidget.setGeometry(QRect(10, 10, 381, 281))
        else:
            # 如果文件格式不受支持，显示提示信息
            self.PreviewWidget = QLabel(self)
            self.PreviewWidget.setText("暂不支持预览该文件类型")
            self.PreviewWidget.setObjectName(u"PreviewWidget")
            self.PreviewWidget.setGeometry(QRect(10, 10, 381, 281))
            self.PreviewWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
