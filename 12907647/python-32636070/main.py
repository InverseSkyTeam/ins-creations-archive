print('我家两台电脑，分别用下面两段代码来链接通讯，结果失败了，打开改编帮我康康问题出在哪里')
# 服务器端
# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',8080))
# s.listen()

# conn,address = s.accept()
# print(address)

# data = conn.recv(1024)
# print(data.decode())

# conn.send('你好'.encode())

# conn.close()
# s.close()



# 用户端
# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((服务器IP,8080))

# s.send(b'Hello')

# data = s.recv(1024)
# print(data.decode())

# s.close()