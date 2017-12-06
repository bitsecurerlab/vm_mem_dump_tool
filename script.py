import os
import sys
import time
import random
import shutil
import subprocess
from os import listdir
from os.path import isfile, join

IMAGE_COUNT = 200
PROCESS_COUNT_MIN = 30
PROCESS_COUNT_MAX = 40
#SHARE_PATH = '/rhome/wsong008/bigdata/vm_mem_dump_tool/share/'
SHARE_PATH = '/home/wei/vm_mem_dump_tool/share/'
#IMAGE_PATH = '/rhome/wsong008/bigdata/vm_mem_dump_tool/memdump/'
IMAGE_PATH = '/media/wei/be4108ae-9679-47ab-8ad8-7d4c9bc0f0a6/memdump/'
INPUT = SHARE_PATH + 'sample_x.txt'
web_list = []
app_list = []
app_win_list = []
pdf_list = []
pic_list = []
doc_list = []
ppt_list = []
xls_list = []
executed = []
prefer_pdf_app = ''
prefer_web_app = ''

def Log(line):
    #print line
    file = open(INPUT, 'a')
    file.write(str(line) + '\n')
    file.close()

def add_app(process_type):
    try_time = 0
    while(True):
        if process_type == 'app':
            app = random.sample(app_list,1)[0]
        elif process_type == 'app_win':
            app = random.sample(app_win_list,1)[0]
        line = 'app\t' + app
        try_time += 1
        if try_time > 100:
            break
        if line not in executed:
            executed.append(line)
            Log(line)
            break

def add_pic():
    file_name = random.sample(pic_list, 1)[0]
    line = 'pic\t' + file_name
    Log(line)

def add_doc():
    file_name = random.sample(doc_list, 1)[0]
    line = 'doc\t' + file_name
    Log(line)

def add_ppt():
    file_name = random.sample(ppt_list, 1)[0]
    line = 'ppt\t' + file_name
    Log(line)

def add_xls():
    file_name = random.sample(xls_list, 1)[0]
    line = 'xls\t' + file_name
    Log(line)

def add_pdf():
    pdf = random.sample(pdf_list, 1)[0]
    line = prefer_pdf_app + '\t' + pdf
    Log(line)

def add_web():
    website = random.sample(web_list, 1)[0]
    line = prefer_web_app + '\t' + website
    Log(line)

def random_process_type():
    return random.sample(['web', 'web', 'app', 'app', 'app', 'app', 'app_win', 'pdf', 'pic', 'office'], 1)[0]

def load_list():
    f = open(SHARE_PATH + 'domain.txt','r')
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break
        line = 'https://www.' + line
        web_list.append(line)
    f.close()
    f = open(SHARE_PATH + 'app.txt','r')
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break
        s = line.split('\t')
        app_list.append(s[1])
    f.close()
    f = open(SHARE_PATH + 'app_windows.txt','r')
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break
        s = line.split('\t')
        app_win_list.append(s[1])
    f.close()
    for f in listdir(SHARE_PATH + 'pdf/'):
        pdf_list.append(f)
    for f in listdir(SHARE_PATH + 'pic/'):
        pic_list.append(f)
    for f in listdir(SHARE_PATH + 'doc/'):
        doc_list.append(f)
    for f in listdir(SHARE_PATH + 'ppt/'):
        ppt_list.append(f)
    for f in listdir(SHARE_PATH + 'xls/'):
        xls_list.append(f)

def load_prefer_app():
    global prefer_pdf_app, prefer_web_app
    prefer_pdf_app = random.sample(['adobe', 'foxit'], 1)[0]
    prefer_web_app = random.sample(['firefox', 'chrome', 'ie'], 1)[0]
    
def main():
    global INPUT
    #os.system('rm '+ IMAGE_PATH + '*')
    index = sys.argv[1]
    if index == '1':
        machine_id = 'win7'
        INPUT = SHARE_PATH + 'sample_' + machine_id +'.txt'
    elif index == '2':
        machine_id = 'win7_2'
        INPUT = SHARE_PATH + 'sample_' + machine_id + '.txt'
    else:
        exit()
    print machine_id
    load_list()
    load_prefer_app()
    for image_count in range(IMAGE_COUNT):
        print('======================================')
        os.system('date')
        os.system('rm -f ' + INPUT)
        PROCESS_COUNT = random.randint(PROCESS_COUNT_MIN, PROCESS_COUNT_MAX)
        print 'PROCESS_COUNT: ' + str(PROCESS_COUNT)
        for process_count in range(PROCESS_COUNT):
            process_type = random_process_type()
            if process_type == 'web':
                add_web()
            if process_type == 'pdf':
                add_pdf()
            if process_type == 'app' or process_type == 'app_win':
                add_app(process_type)
            if process_type == 'pic':
                add_pic()
            if process_type == 'office':
                office_type = random.sample(['doc', 'ppt', 'xls'], 1)[0]
                if office_type == 'doc':
                    add_doc()
                if office_type == 'ppt':
                    add_ppt()
                if office_type == 'xls':
                    add_xls()
        os.system('VBoxManage snapshot ' + machine_id + ' restore snapshot' + index)
        os.system('VBoxManage startvm ' + machine_id + ' --type gui')
        print('Started!')
        time.sleep(180)
        os.system('VBoxManage debugvm ' + machine_id + ' dumpvmcore --filename=' + IMAGE_PATH + 'memdump_' + machine_id + '_' +  str(image_count) + '.img')
        print('Dumped!')
        os.system('mv ' + SHARE_PATH + 'result_sample_' + machine_id + '.txt ' + IMAGE_PATH + 'memdump_' + machine_id + '_' + str(image_count) + '.log')
        print('The ' + str(image_count) + 'th image is generated.')
        os.system('VBoxManage controlvm ' + machine_id + ' poweroff')
        time.sleep(3)

if __name__ == '__main__':
    main()
