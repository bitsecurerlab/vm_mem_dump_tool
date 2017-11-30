#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import webbrowser
import time
import random


# url = 'http://www.baidu.com'
# /usr/local/share
def OpenChrome(url):
    # sys.path.append("libs")
    webbrowser.open(url)
    os.system('exit')
    return 0


def OpenPDF(name):
    file = name + '.pdf'
    os.chdir('/home/ubuntu/pdf')
    os.system('evince' + ' ' + file)
    os.chdir('/home/ubuntu')


def Benchmark():
    time.sleep(300)
    os.system('stress-ng --cpu 4 --vm 2 --hdd 1 --fork 8 --switch 4 --timeout 5m --metrics-brief')


def Random(a, b):
    r = random.randint(a, b)
    return r


# OpenChrome(url)
# time.sleep(10)
# os.system('killall -9 chrome')

if __name__ == "__main__":
    # /media/sf_share
    f = open('/media/sf_share/sample.txt', 'r')
    result = []
    for line in f:
        line = f.readline()
        result.append(line)
    f.close()
    for i in result:
        if (i[0] == 'p'):
            list = i.split(' ',1)
            OpenPDF(list[1])
            time.sleep(2)
        if (i[0]=='w'):
            list = i.split(' ', 1)
            OpenChrome(list[1])
            time.sleep(2)
        if(i[0]=='a'):
            list=i.split(' ',1)
            os.system(list[1])
            time.sleep(2)




