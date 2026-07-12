import jhx.filer
def download():
    jhx.filer.remove_tree('../'*5+'学而思直播/code/site-packages/jhx')
    jhx.filer.mkdir('../'*5+'学而思直播/code/site-packages/jhx')
    jhx.filer.copy_file('jhx','../'*5+'学而思直播/code/site-packages/jhx')
def down_other(old_path,newpath='../../../../../学而思直播/code/site-packages/jhx'):
    jhx.filer.mkdir(newpath)
    jhx.filer.copy_file(old_path,newpath)
def add_method(name,codes,fp='../../../../../学而思直播/code/site-packages/jhx'):
    jhx.filer.mkdir('../'*5+'学而思直播/code/site-packages/jhx')
    jhx.filer.open_file('../'*5+'学而思直播/code/site-packages/jhx'+name,method='w',text=codes)

dld = download
dor = down_other
amd = add_method