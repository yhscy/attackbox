#-- coding: utf-8 --
#@Author : Schun
#@Time : 2022/8/3 17:32

'''
将下载下来的文件md5或sha加密与官网公布的值做比对
SHA256: bf825a3a2788bdfe91b489a63671b1a53b9b79b772c1dc5ee1d2924537697c32
MD5: 972174cd9604a0f5e9b860cf347de19e

'''

import hashlib


def md5_check():
    open_value = '972174cd9604a0f5e9b860cf347de19e'    #公布的md5值
    file = './burpsuite_pro_windows-x64_v2022_7_1.exe'           #下载下来的包存放的路径
    with open(file,'rb') as f:
        data = f.read()

    md5hash = hashlib.md5(data)
    md5 = md5hash.hexdigest()
    if md5 ==open_value:
        print("ok!")



if __name__ == '__main__':
    md5_check()
