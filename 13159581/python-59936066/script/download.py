from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui.ui_LoadDialog import Ui_DownloadDialog
from typing import Dict
import requests
import threading

USER_AGENT: str = "1145141919810"

def size_to_bytes(size_str: str) -> int:
    """
    将文件大小字符串转换为字节数
    :param size_str: 文件大小字符串，例如 "5M"
    :return: 字节数
    """
    units: Dict[str, int] = {
        "B": 1,
        "K": 1024,
        "M": 1024 ** 2,
        "G": 1024 ** 3
    }
    for unit, multiplier in units.items():
        if unit in size_str:
            number = float(size_str.replace(unit, ""))
            return int(number * multiplier)
    return None

class DownloadDialog(QDialog, Ui_DownloadDialog):
    """
    下载对话框类
    """
    progress_update = Signal(int)

    def __init__(self, parent: QWidget=None, file_info: Dict[str, str]=None, download_path: str=None):
        """
        初始化下载对话框
        :param parent: 父窗口
        :param file_info: 文件信息字典，包含链接、名称和大小信息
        :param download_path: 下载路径
        """
        super().__init__(parent)
        self.setupUi(self)
        self.file_info = file_info
        self.download_path = download_path
        self.progressBar.setValue(0)
        self.label.setText(f"{file_info['name']}\n正在下载...")
        self.progress_update.connect(self.update_progress)

        thread = threading.Thread(target=self.download_file)
        thread.daemon = True
        thread.start()
    
    def download_file(self):
        """
        下载文件
        """
        link = self.file_info['link']
        path = self.download_path
        try:
            response = requests.get(link, stream=True, headers={"User-Agent": USER_AGENT})
            response.raise_for_status()  # 检查请求是否成功
            total_length = size_to_bytes(self.file_info['size'].strip('B') if self.file_info['size'][-1] == 'B' else self.file_info['size'])
            with open(f"{path}/{self.file_info['name']}", 'wb') as f:
                dl = 0
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(100 * dl / total_length)
                    self.progress_update.emit(done)
            self.label.setText("下载完成")
            self.progress_update.emit(100)
        except requests.exceptions.RequestException as e:
            self.label.setText(f"下载失败: {e}")

    def update_progress(self, value):
        """
        更新进度条的显示
        :param value: 进度百分比
        """
        self.progressBar.setValue(value)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dialog = DownloadDialog(
        file_info={
            'link': 'https://livefile.xesimg.com/programme/python_assets/ba44a9e13264e6310378f6e8e24ede81.zip', 
            'name': 'pygame.zip',
            'size': '5MB'
        }, 
        download_path='.'
    )
    dialog.show()
    sys.exit(app.exec())
