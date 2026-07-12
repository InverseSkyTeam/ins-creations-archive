print("""教你用os库
import os 

path_01='D:/User/wgy/workplace/data/notMNIST_large.tar.gar'  

path_02='D:/User/wgy/workplace/data/notMNIST_large'  

root_01=os.path.splitext(path_01)  

root_02=os.path.splitext(path_02)  

print(root_01)  

print(root_02)</span>

python中的os.path模块用法：

dirname()   用于去掉文件名，返回目录所在的路径

如：

>>> import os

>>> os.path.dirname('d:\\library\\book.txt')'d:\\library'

basename()   用于去掉目录的路径，只返回文件名

如：

>>> import os

>>> os.path.basename('d:\\library\\book.txt')'book.txt'

join()   用于将分离的各部分组合成一个路径名

如：

>>> import os

>>> os.path.join('d:\\library','book.txt')'d:\\library\\book.txt'

split()  用于返回目录路径和文件名的元组

如：

>>> import os

>>> os.path.split('d:\\library\\book.txt')('d:\\library', 'book.txt')

splitdrive()    用于返回盘符和路径字符元组

>>> import os

>>> os.path.splitdrive('d:\\library\\book.txt')('d:', '\\library\\book.txt')

splitext()    用于返回文件名和扩展名元组

如：

>>> os.path.splitext('d:\\library\\book.txt')('d:\\library\\book', '.txt')

>>> os.path.splitext('book.txt')('book', '.txt')""")