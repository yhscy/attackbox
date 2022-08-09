#-- coding: utf-8 --
#@Author : Schun
#@Time : 2022/8/9 15:49


"""

通过字典和gethostbyname函数，获取子域名挖掘ip

"""


import socket

def domain_ip(url):
    for a in open('dic.txt'):
        urls=a.strip()+'.'+url
        try:
            ip=socket.gethostbyname(urls)
            print(urls+'|'+ip)
        except Exception as e:
            pass

if __name__ == '__main__':
    url='zhishiweilai.com'
    domain_ip(url)
