import os
import sys
import time
import random
from os import listdir

IMAGE_COUNT = 400
PROCESS_COUNT_MIN = 20
PROCESS_COUNT_MAX = 40
FILES_PATH = '/home/wei/vm_mem_dump_tool/files/'
DUMP_PATH = '/media/wei/be4108ae-9679-47ab-8ad8-7d4c9bc0f0a6/memdump/'
web_list = []
app_list = []
app_win_list = []
pdf_list = []
pic_list = []
doc_list = []
ppt_list = []
xls_list = []
prefer_pdf_app = ''
prefer_web_app = ''

def add_action(action_list_file, line):
    #print line
    file = open(action_list_file, 'a')
    file.write(str(line) + '\n')
    file.close()

def add_app(action_list_file, process_type):
    if process_type == 'app':
        app = random.sample(app_list,1)[0]
    elif process_type == 'app_win':
        app = random.sample(app_win_list,1)[0]
    line = 'app\t' + app
    add_action(action_list_file, line)

def add_pic(action_list_file):
    file_name = random.sample(pic_list, 1)[0]
    line = 'pic\t' + file_name
    add_action(action_list_file, line)

def add_doc(action_list_file):
    file_name = random.sample(doc_list, 1)[0]
    line = 'doc\t' + file_name
    add_action(action_list_file, line)

def add_ppt(action_list_file):
    file_name = random.sample(ppt_list, 1)[0]
    line = 'ppt\t' + file_name
    add_action(action_list_file, line)

def add_xls(action_list_file):
    file_name = random.sample(xls_list, 1)[0]
    line = 'xls\t' + file_name
    add_action(action_list_file, line)

def add_pdf(action_list_file):
    pdf = random.sample(pdf_list, 1)[0]
    line = prefer_pdf_app + '\t' + pdf
    add_action(action_list_file, line)

def add_web(action_list_file):
    website = random.sample(web_list, 1)[0]
    line = prefer_web_app + '\t' + website
    add_action(action_list_file, line)

def random_process_type():
    return random.sample(['web', 'web', 'app', 'app', 'app', 'app', 'app_win', 'pdf', 'pic', 'office'], 1)[0]

def load_all_actions():
    f = open(FILES_PATH + 'domain.txt','r')
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break
        line = 'https://www.' + line
        web_list.append(line)
    f.close()
    f = open(FILES_PATH + 'app.txt','r')
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break
        s = line.split('\t')
        app_list.append(s[1])
    f.close()
    f = open(FILES_PATH + 'app_windows.txt','r')
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break
        s = line.split('\t')
        app_win_list.append(s[1])
    f.close()
    for f in listdir(FILES_PATH + 'pdf/'):
        pdf_list.append(f)
    for f in listdir(FILES_PATH + 'pic/'):
        pic_list.append(f)
    for f in listdir(FILES_PATH + 'doc/'):
        doc_list.append(f)
    for f in listdir(FILES_PATH + 'ppt/'):
        ppt_list.append(f)
    for f in listdir(FILES_PATH + 'xls/'):
        xls_list.append(f)

def load_prefer_app():
    global prefer_pdf_app, prefer_web_app
    prefer_pdf_app = random.sample(['adobe', 'foxit'], 1)[0]
    prefer_web_app = random.sample(['firefox', 'chrome', 'ie'], 1)[0]
    
def main():
    machine_id = 'win7'
    action_list_file = FILES_PATH + 'sample_' + machine_id +'.txt'
    load_all_actions()
    load_prefer_app()
    for image_count in range(IMAGE_COUNT):
        print('======================================')
        os.system('date')
        os.system('rm -f ' + action_list_file)  # delete old action_list_file
        print 'Generating random actions.'
        PROCESS_COUNT = random.randint(PROCESS_COUNT_MIN, PROCESS_COUNT_MAX)
        for process_count in range(PROCESS_COUNT):
            process_type = random_process_type()
            if process_type == 'web':
                add_web(action_list_file)
            if process_type == 'pdf':
                add_pdf(action_list_file)
            if process_type == 'app' or process_type == 'app_win':
                add_app(action_list_file, process_type)
            if process_type == 'pic':
                add_pic(action_list_file)
            if process_type == 'office':
                office_type = random.sample(['doc', 'ppt', 'xls'], 1)[0]
                if office_type == 'doc':
                    add_doc(action_list_file)
                if office_type == 'ppt':
                    add_ppt(action_list_file)
                if office_type == 'xls':
                    add_xls(action_list_file)
        os.system('VBoxManage snapshot ' + machine_id + ' restore snapshot')
        os.system('VBoxManage startvm ' + machine_id + ' --type gui')
        time.sleep(240)
        os.system('rm -f ' + DUMP_PATH + 'memdump_' + machine_id + '_' +  str(image_count) + '.img')
        os.system('VBoxManage debugvm ' + machine_id + ' dumpvmcore --filename=' + DUMP_PATH + 'memdump_' + machine_id + '_' +  str(image_count) + '.img')
        print('Memory dumped.')
        os.system('mv ' + FILES_PATH + 'result_sample_' + machine_id + '.txt ' + DUMP_PATH + 'memdump_' + machine_id + '_' + str(image_count) + '.log')
        print('The ' + str(image_count) + 'th image is generated.')
        os.system('VBoxManage controlvm ' + machine_id + ' poweroff')
        print('VM closed.')
        time.sleep(3)

if __name__ == '__main__':
    main()
