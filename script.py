import os
import time
import random
import shutil
from os import listdir
from os.path import isfile, join

IMAGE_COUNT = 1
PROCESS_COUNT = 40
share_path = '/home/wei/vm_mem_dump_tool/share/'
command2 = 'VBoxManage debugvm win7 dumpvmcore --filename = /media/wei/be4108ae-9679-47ab-8ad8-7d4c9bc0f0a6/sample/coredump'
command1 = 'VBoxManage startvm win7 --type gui' ##choose one vm
PDFlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
file_abs = share_path + 'sample.txt'
web_list = []
app_list = []
pdf_list = []
pic_list = []

def Log(line):
    print line
    file = open(file_abs, 'a')
    file.write(str(line) + '\n')
    file.close()

def start_app():
    app = random.sample(app_list,1)[0]
    line = 'app\t' + app
    Log(line)

def start_pic():
    #print 'pic', pic_list
    pic = random.sample(pic_list, 1)[0]
    line = 'pic\t' + pic
    Log(line)

def start_pdf():
    #print 'pdf', pdf_list
    pdf = random.sample(pdf_list, 1)[0]
    line = 'pdf\t' + pdf
    Log(line)

def start_web():
    website = random.sample(web_list, 1)[0]
    line = 'web\t' + website
    Log(line)

def get_process_type():
    return random.sample(['web', 'pdf', 'pic', 'app'], 1)[0]

def clear_output():
    f = open(share_path + 'sample.txt','w')
    f.close()

def main():
    clear_output()
    f = open(share_path + 'domain.txt','r')
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break
        line = 'https://www.' + line
        web_list.append(line)
    f.close()
    f = open(share_path + 'app.txt','r')
    for line in f:
        line = line.strip()
        if len(line) == 0:
            break
        s = line.split('\t')
        app_list.append(s[1])
    f.close()
    #pdf_list = [f for f in listdir(share_path + 'pdf/') if isfile(join(share_path + 'pdf/', f))]
    #pic_list = [f for f in listdir(share_path + 'pic/') if isfile(join(share_path + 'pic/', f))]
    for f in listdir(share_path + 'pdf/'):
        pdf_list.append(f)
    for f in listdir(share_path + 'pic/'):
        pic_list.append(f)
    for image_count in range(IMAGE_COUNT):
        for process_count in range(PROCESS_COUNT):
            process_type = get_process_type()
            if process_type == 'web':
                start_web()
            if process_type == 'pdf':
                start_pdf()
            if process_type == 'app':
                start_app()
            if process_type == 'pic':
                start_pic()
            continue
            os.system(command1)
            print('Started!')
            time.sleep(150)
            command = command2 + str(image_count) + '.img'
            os.system(command)
            print('Dumped!')
            os.system('VBoxManage controlvm win7 poweroff')
            time.sleep(5)
            os.rename(share_path + 'sample.txt', share_path + 'sample' + str(image_count) + '.txt')
            shutil.move(share_path + 'sample' + str(image_count) + '.txt', share_path + 'log/')
            print('The ' + str(image_count) + 'th has done')

if __name__ == '__main__':
    main()
