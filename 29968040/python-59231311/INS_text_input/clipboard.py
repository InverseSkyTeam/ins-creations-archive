try:
    import pyperclip
    USE_PYPERCLIP = True
except ImportError:
    USE_PYPERCLIP = False
import pyperclip


class ClipBoard:
    _clipboard = ''

    @staticmethod
    def copy(text):
        if USE_PYPERCLIP:
            pyperclip.copy(text)
        else:
            ClipBoard._clipboard = text

    @staticmethod
    def paste():
        if USE_PYPERCLIP:
            return pyperclip.paste()
        else:
            return ClipBoard._clipboard
