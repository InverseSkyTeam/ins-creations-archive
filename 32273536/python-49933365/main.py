print("Welcome! 支持 + - * / ^ ( ) 等运算符！")

return_code = __import__("os").system("klang.exe")

if return_code != 0:
    print("检测到崩溃。请在下方提交报告。")