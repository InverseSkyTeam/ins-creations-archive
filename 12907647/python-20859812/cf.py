cf_py_name = 'Create file'
cf_live_path = "D:\\system_jhxc\\my_user"
def mkdir(path):
    import os
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        return True
    else:
        return False