from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui.ui_LoadDialog import Ui_DownloadDialog
import new_uploader, threading

class UploadDialog(QDialog, Ui_DownloadDialog):
    finished = Signal(str)
    def __init__(self, parent=None, filepath=None):
        super().__init__(parent)
        self.setupUi(self)

        self.label.setText(f"正在上传...")
        self.filepath = filepath
        self.upload_link = ""
        

        self.uploader = new_uploader.Uploader()
        self.uploader.progress_signal.connect(lambda value: self.progressBar.setValue(value))
        threading.Thread(target=self.upload, daemon=True).start()
    
    def upload(self):
        self.upload_link = self.uploader.upload_file(self.filepath)
        self.label.setText(f"上传成功")
        self.finished.emit(self.upload_link)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = UploadDialog(filepath="C:\\Users\\Administrator\\学而思直播\\code\\cache\\asset\\lrsXesPan\\XesPanPack.zip")
    dialog.finished.connect(lambda: print(dialog.upload_link))
    dialog.show()
    sys.exit(app.exec())
