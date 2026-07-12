from distutils.core import setup
from distutils.extension import Extension  # 导入Extension类
from Cython.Build import cythonize
import numpy as np
import sys

# 根据平台设置OpenMP参数
if sys.platform.startswith("win"):
    openmp_arg = '/openmp'
    o2_arg = '/O2'
else:
    openmp_arg = '-fopenmp'
    o2_arg = '-O2'

# 创建Extension对象，明确传递OpenMP参数
extensions = [
    Extension(
        "sandbox_speedup",  # 模块名称
        ["sandbox_speedup.pyx"],  # 源文件
        extra_compile_args=[openmp_arg, o2_arg],  # 编译参数
        extra_link_args=[openmp_arg],     # 链接参数
    )
]

setup(
    name="sandbox_speedup",
    ext_modules=cythonize(
        extensions,  # 使用自定义的Extension列表
        annotate=True,
        compiler_directives={
            'language_level': "3",
            'boundscheck': False,
            'wraparound': False,
            'initializedcheck': False
        }
    ),
    include_dirs=[np.get_include()]  # 包含numpy头文件
)