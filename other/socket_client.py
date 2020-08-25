import socket

# 1. 创建socket
socket = socket.socket()

# 2. 连接服务器
socket.connect(('localhost', 9000))

# 3. 接收数据
msg = socket.recv(128)
print('Server:', msg.decode('utf-8'))

# 4. 向服务端发送 数据
socket.send('Fuck Today'.encode('utf-8'))


# 5. 关闭
socket.close()
