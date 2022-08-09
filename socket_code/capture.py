#-- coding: utf-8 --
#@Author : Schun
#@Time : 2022/8/9 16:27

from scapy.all import *


def CallBack(packet):
    print(packet.show())

    if packet.haslayer('TCP'):
        print(packet['TCP'].sport)
        print(packet['TCP'].dport)
        print(packet['TCP'].seq)
        print(packet['TCP'].dataofs)


filter = "tcp"

sniff(filter=filter, prn=CallBack, iface='', count=0)


# 待完善。。。。。