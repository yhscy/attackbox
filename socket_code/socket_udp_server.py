#-- coding: utf-8 --
#@Author : Schun
#@Time : 2022/8/9 9:26



from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)


local_addr = ('',7799)
udp_socket.bind(local_addr)
print("端口绑定成功")
recv_data = udp_socket.recvfrom(1024) #  1024表示本次接收的最大字节数
print(recv_data[0].decode('utf-8'))
udp_socket.close()