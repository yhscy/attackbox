#-- coding: utf-8 --
#@Author : Schun
#@Time : 2022/8/9 9:18

import socket

'''

Address Family：IP地址类型; AF_INET表示ipv4类型、AF_INET6表示ipv6类型; 
Type：套接字类型，可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）

'''




udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dest_addr = ('123.56.124.130', 7799)  # 注意 是元组，ip是字符串，端口是数字

send_data = input("请输入要发送的数据:")

udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

