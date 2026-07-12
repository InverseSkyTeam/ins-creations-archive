from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui.ui_UploadDialog import Ui_UploadDialog
import uploader, threading

class UploadDialog(QDialog, Ui_UploadDialog):
    finished = Signal(str)
    def __init__(self, parent=None, filepath=None):
        super().__init__(parent)
        self.setupUi(self)

        self.label.setText(f"正在上传...")
        self.filepath = filepath
        self.upload_link = ""
        

        self.uploader = uploader.Uploader()
        self.uploader.progress_signal.connect(lambda value: self.progressBar.setValue(value))
        threading.Thread(target=self.upload, daemon=True).start()
    
    def upload(self) -> None:
        self.upload_link = self.uploader.upload_file(self.filepath)
        self.label.setText(f"上传成功")
        self.finished.emit(self.upload_link)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = UploadDialog(filepath="./uploader.py")
    dialog.finished.connect(lambda: print(dialog.upload_link))
    dialog.show()
    sys.exit(app.exec())
