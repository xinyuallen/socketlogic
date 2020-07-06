# author: yang time:2020/7/3.
import socket
#创建socket对象
sk = socket.socket()

#绑定ip和端口
sk.bind(('127.0.0.1',8000))

#监听
sk.listen()

#等待连接
while True:
    conn,addr = sk.accept()  #建立连接
    #接收数据
    data = conn.recv(2048).decode('utf-8')
    url = data.split()[1]
    print(url)
    #返回数据
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')

    if url == '/rihan':
        conn.send(b'/rihan/')
    elif url =='/oumei':
        conn.send(b'/oumei')
    else:
        conn.send(b'404not found')


    #断开连接
    conn.close()