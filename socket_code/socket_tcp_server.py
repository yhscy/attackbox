#-- coding: utf-8 --
#@Author : Schun
#@Time : 2022/8/9 9:06

import socket


tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 7788)
tcp_server_socket.bind(address)
tcp_server_socket.listen(128)
print("服务端已启动，绑定7788端口....")
# 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的链接
client_socket, clientAddr = tcp_server_socket.accept()

while True:
    recv_data = client_socket.recv(1024)  # 接收1024个字节
    recv_data_str = recv_data.decode('utf-8')
    print('接收到的数据为:', recv_data_str)
    send_data = input("输入可执行命令:")
    client_socket.send(send_data .encode('utf-8'))
