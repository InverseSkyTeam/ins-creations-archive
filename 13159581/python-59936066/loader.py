"""
    Universal Loader
    -----------------------
    这是一个简单的 Python 加载器
    看似 Universal 实则未考虑 32 位设备
    不过还是带来了 Python 3.12.5 on Xueersi Python Helper！
    -----------------------
    使用方法：
    看示例作品得了（
    作品链接：https://code.xueersi.com/ide/code/59318686
"""

import os
import shutil
import zipfile
import requests
import sys

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}

runtime_url = (
    "https://livefile.xesimg.com/programme/python_assets/0f53697bdcecfb97b99ac8aa9d9a9e13.zip"
)
runtime_ver = "3.12.5"
packages_name = None
chunk_size = 2048

if not os.path.exists("../UniversalRuntime"):
    os.mkdir("../UniversalRuntime")


def _download_file(url: str, save_to: str):
    with open(save_to, "wb") as file:
        res = requests.get(url, headers=header, stream=True)
        # total_size = res.headers["Content-Length"]
        # pending_size = 0
        for chunk in res.iter_content(chunk_size):
            file.write(chunk)
            # pending_size += len(chunk)


def _load_runtime():
    if os.path.exists(f"../UniversalRuntime/runtimes/downloads/{runtime_ver}.zip"):
        os.remove(f"../UniversalRuntime/runtimes/downloads/{runtime_ver}.zip")
    shutil.rmtree(f"../UniversalRuntime/runtimes/{runtime_ver}")
    os.mkdir(f"../UniversalRuntime/runtimes/{runtime_ver}")

    print(f"正在下载 Python {runtime_ver}...")
    _download_file(runtime_url, f"../UniversalRuntime/runtimes/downloads/{runtime_ver}.zip")
    print(f"Python {runtime_ver} 下载完毕！")

    with zipfile.ZipFile(f"../UniversalRuntime/runtimes/downloads/{runtime_ver}.zip") as zip:
        zip.extractall(f"../UniversalRuntime/runtimes/{runtime_ver}")
    print(f"Python {runtime_ver} 解压完毕！")


def load_runtime():
    if not os.path.exists("../UniversalRuntime/runtimes"):
        os.mkdir("../UniversalRuntime/runtimes")
    if not os.path.exists(f"../UniversalRuntime/runtimes/downloads"):
        os.mkdir("../UniversalRuntime/runtimes/downloads")
    if not os.path.exists(f"../UniversalRuntime/runtimes/{runtime_ver}"):
        os.mkdir(f"../UniversalRuntime/runtimes/{runtime_ver}")
    if not os.path.exists(f"../UniversalRuntime/runtimes/{runtime_ver}/done.txt"):
        _load_runtime()
        with open(f"../UniversalRuntime/runtimes/{runtime_ver}/done.txt", "w"):
            pass
    else:
        print(f"已存在 Python {runtime_ver}！")


def _load_packages(packages_url: str):
    if os.path.exists(f"../UniversalRuntime/packages/downloads/{packages_name}.zip"):
        os.remove(f"../UniversalRuntime/packages/downloads/{packages_name}.zip")
    shutil.rmtree(f"../UniversalRuntime/packages/{packages_name}")
    os.mkdir(f"../UniversalRuntime/packages/{packages_name}")

    print("正在下载依赖库...")
    _download_file(packages_url, f"../UniversalRuntime/packages/downloads/{packages_name}.zip")
    print("依赖库下载完毕！")

    with zipfile.ZipFile(f"../UniversalRuntime/packages/downloads/{packages_name}.zip") as zip:
        zip.extractall(f"../UniversalRuntime/packages/{packages_name}")
    print("依赖库解压完毕！")


def load_packages(packages_url: str):
    global packages_name
    packages_name = packages_url.split("/")[-1].split(".")[0]

    if not os.path.exists("../UniversalRuntime/packages"):
        os.mkdir("../UniversalRuntime/packages")
    if not os.path.exists("../UniversalRuntime/packages/downloads"):
        os.mkdir("../UniversalRuntime/packages/downloads")
    if not os.path.exists(f"../UniversalRuntime/packages/{packages_name}"):
        os.mkdir(f"../UniversalRuntime/packages/{packages_name}")
    if not os.path.exists(f"../UniversalRuntime/packages/{packages_name}/done.txt"):
        _load_packages(packages_url)
        with open(f"../UniversalRuntime/packages/{packages_name}/done.txt", "w"):
            pass
    else:
        print("已存在依赖库！")


def _setup_runtime():
    short_ver_num = "".join(runtime_ver.split(".")[:2])
    with open(
        f"../UniversalRuntime/runtimes/{runtime_ver}/python{short_ver_num}._pth",
        "w",
        encoding="utf-8",
    ) as file:
        data = f"""python{short_ver_num}.zip\n.\n"""
        if packages_name:
            data = data + "\n".join(
                [
                    os.path.abspath(f"../UniversalRuntime/packages/{packages_name}"),
                    os.path.abspath(f"../UniversalRuntime/packages/{packages_name}/site-packages"),
                    os.path.abspath(f"./script"),
                ]
            )
        file.write(data)


def run(windowed=False):
    _setup_runtime()
    os.chdir("./script")

    if windowed:
        program = os.path.normpath(
            f"../../UniversalRuntime/runtimes/{runtime_ver}/pythonw.ex" + "e"
        )
        os.system(" ".join(["start", program, "./main.py", *sys.argv[1:]]))
    else:
        program = os.path.normpath(f"../../UniversalRuntime/runtimes/{runtime_ver}/python.ex" + "e")
        os.system(" ".join([program, "./main.py", *sys.argv[1:]]))
