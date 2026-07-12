# 这个改自lrs的XesPan：https://code.xueersi.com/home/project/detail?lang=code&pid=58475913&version=offline&form=python&langType=python
from PySide6.QtCore import *
from typing import TypedDict
import requests
import hashlib
import os

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}

class UploadParam(TypedDict):
    host: str
    vpc_host: str
    headers: dict
    cdn: str
    key: str
    url: str

class Uploader(QObject):
    progress_signal = Signal(int)
    
    def _get_oss_upload_param(self, filename, md5) -> UploadParam:
        response = requests.get(
            "https://code.xueersi.com/api/assets/get_oss_upload_params"
            f"?scene=offline_python_assets&md5={md5}&filename={filename}"
        )
        data = response.json()
        return data["data"]
    
    def _file_sender(self, filepath, total_size):
        uploaded_size = 0
        with open(filepath, "rb") as f:
            chunk = f.read(10240)
            while chunk:
                yield chunk
                uploaded_size += len(chunk)
                self.progress_signal.emit(int(uploaded_size / total_size * 100))
                chunk = f.read(10240)
    
    def upload_file(self, filepath) -> str:
        if not os.path.exists(filepath):
            raise FileNotFoundError("文件不存在")
        
        with open(filepath, "rb") as f:
            content = f.read()
            md5 = hashlib.md5(content).hexdigest()
            total_size = len(content)
            del content
        
        params: UploadParam = self._get_oss_upload_param(filepath, md5)
        requests.put(
            params["url"],
            data=self._file_sender(filepath, total_size),
            headers=params["headers"],
            stream=True
        )
        return params["url"]

def test_uploader():
    def callback(e: int):
        print(e)
    uploader = Uploader()
    uploader.progress_signal.connect(callback)
    print(uploader._get_oss_upload_param("what.txt", "9904167b30f18d8642a4c70a2924177b"))
    print(uploader.upload_file("what.txt"))


if __name__ == "__main__":
    test_uploader()