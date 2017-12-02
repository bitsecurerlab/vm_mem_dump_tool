# !/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import webbrowser
import time
import random
import subprocess
import datetime

#subprocess.Popen('C:\\Program Files\\Notepad++\\notepad++.exe')
SAMPLE_PATH = 'F:\\sample.txt'
SHARE_PATH = 'F:\\'

def open_web(app, url):
    if app == 'chrome':
        app_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    elif app == 'firefox':
        app_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    elif app == 'ie':
        app_path = 'C:\\Program Files\\Internet Explorer\\iexplore.exe'
    subprocess.Popen(app_path + ' ' + url)

def open_pdf(app, name):
    if app == 'adobe':
        app_path = 'C:\\Program Files\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe'
    elif app == 'foxit':
        app_path = 'C:\\Program Files\\Foxit Software\\Foxit Reader\\FoxitReader.exe'
    subprocess.Popen(app_path + ' ' + SHARE_PATH + 'pdf\\' + name)

def open_app(app, f):
    try:
        subprocess.Popen(app)
        f.writelines(str(datetime.datetime.now()) + '\tapp\t' + app + '\n')
    except:
        f.writelines('error ' + app + '\n')

def open_pic(pic, f):
    try:
        #subprocess.Popen('C:\\Program Files\\Meitu\\KanKan\\KanKan.exe ' + SHARE_PATH + '\\pic\\' + pic)
        subprocess.Popen('mspaint ' + SHARE_PATH + '\\pic\\' + pic)
        f.writelines(str(datetime.datetime.now()) + '\tpic\t' + pic + '\n')
    except:
        f.writelines('error ' + pic + '\n')

def Benchmark():
    time.sleep(300)
    os.system('stress-ng --cpu 4 --vm 2 --hdd 1 --fork 8 --switch 4 --timeout 5m --metrics-brief')

def Random(a, b):
    r = random.randint(a, b)
    return r

def main():
    while (os.path.exists(SAMPLE_PATH) == False):
        time.sleep(2)
    result = []
    f = open(SAMPLE_PATH, 'r')
    for line in f:
        if '\t' not in line or 'internal log' in line:
            break
        if (len(line) != 0):
            result.append(line.strip())
    f.close()
    #print result
    log = []
    bufsize = 0
    f = open(SAMPLE_PATH, 'a', bufsize)
    f.writelines('\n---------internal log---------\n')
    for line in result:
        print line
        s = line.split('\t')
        if (s[0] == 'foxit' or s[0] == 'adobe'):
            open_pdf(s[0], s[1])
            f.writelines(str(datetime.datetime.now()) + '\t' + s[0] + '\t' + s[1] + '\n')
        elif (s[0] == 'ie' or s[0] == 'firefox' or s[0] == 'chrome'):
            open_web(s[0], s[1])
            f.writelines(str(datetime.datetime.now()) + '\t' + s[0] + '\t' + s[1] + '\n')
        elif (s[0] == 'app'):
            open_app(s[1], f)
        elif (s[0] == 'pic'):
            open_pic(s[1], f)
        time.sleep(4)
    f.close()

if __name__ == '__main__':
    main()
