from files.lib import cloudlib
userid = cloudlib.get_id(cloudlib.get_cookies())
if input('输入需要模式的序号(1.存储信息到云端 2.从云端读取信息):') == '1':cloudlib.save_to_cloud(input('输入标题'),input('输入一句话'),userid);print('\n\n\n存储完毕')
else:text = cloudlib.read_from_cloud(input('输入标题'),userid);print(text);print('\n\n\n读取完毕')
print('使用库后，10行代码开始云旅程~')