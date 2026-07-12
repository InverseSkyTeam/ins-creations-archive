"""
在此次运行中，你将编辑名为big-file.py的、10万行的、edcore.py复制n遍的大文件
你可以再将它复制十遍以达到100万行之效果
测试中，虽然TermEd高亮100万行需要快一分钟，甚至过程中CPU >30% 内存>1100MB，但是在高亮完毕后操作极其丝滑
"""

import os

os.system("start cmd /c \"python edcore.py big-file.py & pause\"")
