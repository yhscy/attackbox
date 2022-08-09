#-- coding: utf-8 --
#@Author : Schun
#@Time : 2022/8/9 16:07
import queue
import socket
import threading




'''

利用socket模块connect完成端口扫描

'''
def port_scan(ip,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while not q.empty():
        port=q.get()
        try:
            server.connect((ip,port))
            print('主机%s的%s端口处于打开状态' % (ip, port))
            server.close()
        except Exception as e:
            print('主机%s的%s端口处于关闭状态' % (ip, port))
        finally:
            server.close()

if __name__ == '__main__':
    q=queue.Queue()
    ip=input("please input scan ip:")
    ports=[21,22,23,25,53,53,80,81,110,111,123,123,135,137,139,161,389,443,445,465,500,515,520,523,548,623,636,873,902,1080,1099,1433,1521,1604,1645,1701,1883,1900,2049,2181,2375,2379,2425,3128,3306,3389,4730,5060,5222,5351,5353,5432,5555,5601,5672,5683,5900,5938,5984,6000,6379,7001,7077,8080,8081,8443,8545,8686,9000,9001,9042,9092,9100,9200,9418,9999,11211,27017,37777,50000,50070,61616]
    for port in ports:
        q.put(port)
        t = threading.Thread(target=port_scan,args=(ip,port))
        t.start()
