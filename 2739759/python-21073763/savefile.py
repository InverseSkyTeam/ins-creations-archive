import os
def save_path(filename):
    basepath = os.path.dirname(__file__)
    return os.path.join(basepath,'static/images/'+filename)