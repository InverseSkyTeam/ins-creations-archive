from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from upload_dialog import UploadDialog
from ui.ui_main_window import Ui_MainWindow
from PIL import Image

def isImage(filepath):
    try:
        Image.open(filepath)
    except:
        return False
    return True

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(QSize(481, 121))

        self.img_path = None

        self.pushButton.clicked.connect(self.upload_image)
        self.pushButton_2.clicked.connect(self.select_image)
    
    def upload_image(self):
        if self.img_path is None:
            QMessageBox.warning(self, "警告", "请先选择图片！")
            return
        dialog = UploadDialog(self, self.img_path)
        dialog.finished.connect(self.upload_finished)
        dialog.show()

    def upload_finished(self, url):
        self.lineEdit.setText(url)
        self.img_path = None
        self.label.setText("所选图片：无")
    
    def select_image(self):
        img_path, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "*.*")
        if img_path:
            if not isImage(img_path):
                QMessageBox.warning(self, "警告", "请选择图片文件！")
                return
            self.img_path = img_path
            self.label.setText("所选图片："+img_path)
        
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()