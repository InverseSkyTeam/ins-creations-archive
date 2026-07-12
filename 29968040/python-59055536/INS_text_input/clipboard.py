try:
    import pyperclip
    USE_PYPERCLIP = True
except ImportError:
    USE_PYPERCLIP = False
import pyperclip

_clipboard = ''


class ClipBoard:
    @staticmethod
    def copy(text):
        global _clipboard
        if USE_PYPERCLIP:
            pyperclip.copy(text)
        else:
            _clipboard = text

    @staticmethod
    def paste():
        global _clipboard
        if USE_PYPERCLIP:
            return pyperclip.paste()
        else:
            return _clipboard
