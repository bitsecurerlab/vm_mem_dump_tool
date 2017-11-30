# !/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import webbrowser
import time
import random
import subprocess
import datetime

#subprocess.Popen("C:\\Program Files\\Notepad++\\notepad++.exe")

# url = "http://www.baidu.com"
# /usr/local/share
def OpenChrome(url):
    subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe " + url)
    return 0


def OpenPDF(name):
    file = name + ".pdf"
    # os.chdir("/home/ubuntu/pdf")
    subprocess.Popen("C:\Program Files\Foxit Software\Foxit Reader\FoxitReader.exe H:\\" + file)
    # os.chdir("/home/ubuntu")


def Benchmark():
    time.sleep(300)
    os.system("stress-ng --cpu 4 --vm 2 --hdd 1 --fork 8 --switch 4 --timeout 5m --metrics-brief")


def Random(a, b):
    r = random.randint(a, b)
    return r


if __name__ == "__main__":
    # /media/sf_share
    while (os.path.exists("H:\sample.txt") == False):
        time.sleep(2)
    f = open("H:\sample.txt", "r")
    result = []
    for line in open("H:\sample.txt"):
        line = f.readline()
        if (len(line) != 0):
            result.append(line.strip())
    f.close()
    log = []
    bufsize = 0
    f = open("H:\sample.txt", "a", bufsize)
    f.writelines("\n---------internal log---------\n")
    for i in result:
        if (len(i) != 0):
            if (i[0] == "p"):
                list = i.split(" ", 1)
                OpenPDF(list[1])
                f.writelines(str(datetime.datetime.now())+'\tpdf'+list[1]+'\n')
                time.sleep(2)
            # print(list[1])
            if (i[0] == "w"):
                list = i.split(" ", 1)
                # print(type(list[1]))
                OpenChrome(list[1])
                f.writelines(str(datetime.datetime.now())+'\twebsite '+list[1]+'\n')
                time.sleep(2)

            if (i[0] == "a"):
                list = i.split(" ", 1)
                print(list[1])
                try:
                    subprocess.Popen(str(list[1]))
                    f.writelines(str(datetime.datetime.now())+'\tapp '+list[1]+'\n')
                except:
                    f.writelines('error '+list[i]+'\n')
                time.sleep(2)

            if (i[0] == "p"):
                list = i.split(" ", 1)
                try:
                    subprocess.Popen("C:\Program Files\Meitu\KanKan\KanKan.exe H:\\photo\\"+str(list[1])+'.jpg')
                    f.writelines(str(datetime.datetime.now())+'\tphoto '+list[1]+'\n')
                except:
                    f.writelines('error '+list[i]+'\n')
                time.sleep(2)
    #f.writelines(log)
    f.close()





