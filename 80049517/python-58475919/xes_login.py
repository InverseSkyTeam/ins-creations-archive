import webview
import time

_cookie = ''


def _while_wait_to_get_cookie(window):
    """while循环直到登录完毕"""
    global _cookie
    while True:
        try:
            url = window.get_current_url()
        except:
            _cookie = ''
            break
        else:
            if ('online.xueersi.com' in url) or ('www.xueersi.com' in url) or ('code.xueersi.com' in url):
                window.load_url("https://code.xueersi.com")
                time.sleep(2)

                cookies = window.get_cookies()
                _cookie = ""
                for cookie in cookies:
                    for key, value in sorted(cookie.items()):
                        _cookie += f"{key}={value.value};"

                window.destroy()
                break


def login_to_get_coo_kie():
    """通过登录来获取coo-kie"""
    win = webview.create_window("登录-学而思", "https://login.xueersi.com")
    webview.start(_while_wait_to_get_cookie, win, private_mode=False)
    return _cookie


if __name__ == '__main__':
    print(login_to_get_coo_kie())
