def open_file(name,method='r',encode='utf-8',text='write text there',do=None):
    try:
        with open(name,method,encoding=encode) as f:
            if method == 'r':
                get = f.read()
            else:
                f.write(text)
                get = 'already write "' + text + '"'
            if do != None:
                try:
                    do()
                    get += '\ndo well'
                except:
                    get += '\ndo badly'
        f.close()
    except (OsError,SystemError,KeyError) as e:
        get = 'Error-happend: '+e
        ok = False
    except:
        get = 'Exception Error:filer did error.'
        ok = False
    else:
        ok = True
    finally:
        return (ok,get)

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

def copy_file(old_path, new_path):
    import os,shutil
    for file in os.listdir(old_path):
        try:
            shutil.copyfile(os.path.join(old_path, file), os.path.join(new_path, file))
        except:
            mkdir(new_path+'/'+file)
            copy_file(old_path+'/'+file, new_path+'/'+file)

def remove_tree(path):
    import shutil
    shutil.rmtree(path)