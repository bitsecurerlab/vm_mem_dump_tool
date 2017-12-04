import os
import time
import random
import shutil
from os import listdir
from os.path import isfile, join

IMAGE_COUNT = 1
PROCESS_COUNT = 30
SHARE_PATH = '/rhome/wsong008/bigdata/vm_mem_dump_tool/share/'
IMAGE_PATH = '/rhome/wsong008/bigdata/vm_mem_dump_tool/memdump/'
COMMAND_START_VM = 'VBoxManage startvm win7 --type gui' ##choose one vm
COMMAND_DUMP = 'VBoxManage debugvm win7 dumpvmcore --filename = ' + IMAGE_PATH
OUTPUT = SHARE_PATH + 'sample.txt'
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
    print line
    file = open(OUTPUT, 'a')
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
    return random.sample(['web', 'pdf', 'pic', 'app', 'app', 'app', 'app_win', 'doc' ,'ppt', 'xls'], 1)[0]

def clear_output():
    f = open(SHARE_PATH + 'sample.txt','w')
    f.close()

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
    clear_output()
    load_list()
    load_prefer_app()
    for image_count in range(IMAGE_COUNT):
        print('======================================')
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
            if process_type == 'doc':
                add_doc()
            if process_type == 'ppt':
                add_ppt()
            if process_type == 'xls':
                add_xls()
        #os.system(COMMAND_START_VM)
        print('Started!')
        time.sleep(2)########
        #os.system(COMMAND_DUMP + 'memdump_' + str(image_count) + '.img')
        print('Dumped!')
        #os.system('VBoxManage controlvm win7 poweroff')
        time.sleep(5)
        print('mv ' + SHARE_PATH + 'result_sample.txt ' + IMAGE_PATH + 'memdump_' + str(image_count) + '.log')
        os.system('mv ' + SHARE_PATH + 'result_sample.txt ' + IMAGE_PATH + 'memdump_' + str(image_count) + '.log')
        print('The ' + str(image_count) + 'th image is generated.')

if __name__ == '__main__':
    main()
