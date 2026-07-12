import os
import subprocess
import sys
def newimport(modelname):
    errordict = {"wx":"wxPython","cv2":"opencv-python","win32api":"pywin32","win32gui":"pywin32","win32con":"pywin32","webview":"pywebview"}
    try:
        exec(f"import {modelname}")
        print("导入成功！")
    except:
        if modelname in errordict:
            modelname1 = errordict[modelname]
        else:
            modelname1 = modelname
        module_path =  os.path.expanduser("~/学而思直播/code/site-packages")
        mn_path = os.path.join(module_path, modelname1)
        subprocess.check_output([sys.executable, "-m", "pip", "uninstall", modelname1, "-y"])
        if os.path.exists(mn_path):
            shutil.rmtree(mn_path)
        subprocess.check_output([sys.executable, "-m", "pip", "install", modelname1, "-t", module_path])
        exec(f"import {modelname}")
        print("安装成功！")