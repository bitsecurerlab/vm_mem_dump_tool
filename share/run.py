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

def OpenChrome(url):
    subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe " + url)

def OpenPDF(name):
    file = name + ".pdf"
    subprocess.Popen("C:\\Program Files\\Foxit Software\\Foxit Reader\\FoxitReader.exe H:\\pdf\\" + file)

def Benchmark():
    time.sleep(300)
    os.system("stress-ng --cpu 4 --vm 2 --hdd 1 --fork 8 --switch 4 --timeout 5m --metrics-brief")

def Random(a, b):
    r = random.randint(a, b)
    return r

if __name__ == "__main__":
    while (os.path.exists("H:\\sample.txt") == False):
        time.sleep(2)
    f = open("H:\\sample.txt", "r")
    result = []
    for line in open("H:\\sample.txt"):
        line = f.readline()
        if '\t' not in line or 'internal log' in line:
            break
        if (len(line) != 0):
            result.append(line.strip())
    f.close()
    print result
    log = []
    bufsize = 0
    f = open("H:\\sample.txt", "a", bufsize)
    f.writelines("\n---------internal log---------\n")
    for line in result:
        s = line.split('\t')
        if (s[0] == "pdf"):
            OpenPDF(s[1])
            f.writelines(str(datetime.datetime.now())+'\tpdf\t'+s[1]+'\n')
        if (s[0] == "web"):
            OpenChrome(s[1])
            f.writelines(str(datetime.datetime.now())+'\twebsite\t'+s[1]+'\n')
        if (s[0] == "app"):
            try:
                subprocess.Popen(str(s[1]))
                f.writelines(str(datetime.datetime.now())+'\tapp\t'+s[1]+'\n')
            except:
                f.writelines('error '+s[i]+'\n')
        if (s[0] == "photo"):
            try:
                subprocess.Popen("C:\\Program Files\\Meitu\\KanKan\\KanKan.exe H:\\photo\\"+str(s[1])+'.jpg')
                f.writelines(str(datetime.datetime.now())+'\tphoto\t'+s[1]+'\n')
            except:
                f.writelines('error '+s[i]+'\n')
        time.sleep(2)
    f.close()