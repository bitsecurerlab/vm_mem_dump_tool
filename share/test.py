#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
import sys
import webbrowser
import time
import random
import subprocess

# url = 'http://www.baidu.com'
# /usr/local/share
def OpenChrome(url):
    # sys.path.append("libs")
    webbrowser.open(url)
    os.system('exit')
    return 0


def OpenPDF(name):
    file = name + '.pdf'
    #os.chdir('/home/ubuntu/pdf')
    subprocess.Popen('evince' + ' /home/ubuntu/pdf/' + file,shell=True)
    #os.chdir('/home/ubuntu')


def Benchmark():
    time.sleep(300)
    os.system('stress-ng --cpu 4 --vm 2 --hdd 1 --fork 8 --switch 4 --timeout 5m --metrics-brief')


def Random(a, b):
    r = random.randint(a, b)
    return r



if __name__ == "__main__":
    # /media/sf_share
    while(os.path.exists('/media/sf_share/sample.txt')==False):
	time.sleep(2)
    f = open('/media/sf_share/sample.txt', 'r')
    result = []
    for line in open('/media/sf_share/sample.txt'):
    	line=f.readline()
	if(len(line)!=0):
		result.append(line.strip())
    f.close()
    log=[]
    for i in result:
	if(len(i)!=0):
        	if (i[0]=='p'):
         		list = i.split(' ',1)
            		OpenPDF(list[1])
			log.append(list[1])
          		time.sleep(4)
	    	 	#print(list[1])
        	if (i[0]=='w'):
          		list = i.split(' ', 1)
	  		#print(type(list[1]))
          		OpenChrome(list[1])
			log.append(list[1])
           		time.sleep(4)
	  
      		if(i[0]=='a'):
         		list=i.split(' ',1)
          		subprocess.Popen(list[1],shell=True)
			log.append(list[1])	
              		time.sleep(4)
    f=open('/media/sf_share/sample.txt', 'a')
    f.writelines("---------internal log---------")
    f.writelines(log)
    f.close()

    



