# author: yang time:2020/7/5.
import socket
#创建socket对象
sk = socket.socket()

#绑定ip和端口
sk.bind(('127.0.0.1',8001))

#监听
sk.listen()

def rihan(url):
    return '欢迎访问日韩板块'.format(url)

def oumei(url):
    return '欢迎访问欧美板块'.format(url)
def guochan(url):
    return '欢迎访问欧美板块'.format(url)
def home(url):
    with open('home.html','r',encoding='utf-8') as f:
        ret = f.read()
        return ret

list = [
    ('/rihan',rihan),
    ('/oumei',oumei),
    ('/guochan',guochan),
    ('/home',home),
]

#等待连接
while True:
    conn,addr = sk.accept()  #建立连接
    #接收数据
    data = conn.recv(2048).decode('utf-8')
    url = data.split()[1]
    print(url)
    #返回数据
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n')

    func = None
    for i in list:
        if url == i[0]:
            func = i[1]
            break
    if func:
        ret = func(url)


    # if url == '/rihan':
    #     ret = rihan(url)
    # elif url =='/oumei':
    #     ret = oumei(url)
    # else:
    #     ret = '404notfound'
    #
    conn.send(ret.encode('utf-8'))
    #断开连接
    conn.close()