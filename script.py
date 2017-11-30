import os
import time
import random
import shutil
#command1='VBoxManage startvm ubuntu --type gui'

#command2='VBoxManage debugvm ubuntu dumpvmcore --filename=d:\sample\test.img'

#os.chdir(path)
#os.system(command1)
#time.sleep(1800)
#os.system('VBoxManage controlvm ubuntu poweroff')
#path='C:\Program Files\Oracle\VirtualBox'
command2='VBoxManage debugvm win7 dumpvmcore --filename=/media/wei/be4108ae-9679-47ab-8ad8-7d4c9bc0f0a6/sample/coredump'
command1='VBoxManage startvm win7 --type gui' ##choose one vm
#AppList = ['vlc','filezilla','speedcrunch','geany','firefox','libreoffice','smplayer','clementine','gimp','stellarium']
app_dict={"Evernote":"C:\Program Files\Evernote\Evernote\Everton.exe","FSviewer":"C:\Program Files\FastStone Image Viewer\FSViewer.exe",
          "foxit":"C:\Program Files\Foxit Software\Foxit Reader\FoxitReader.exe","screen":"C:\Program Files\Free Fire Screensaver\Free Fire Screensaver.exe",
          "Lingoes":"C:\Program Files\Lingoes\Translator2\Lingoes.exe","BingDict":"C:\Program Files\Microsoft Bing Dictionary\BingDict.exe",
          "notepad":"C:\Program Files\\Notepad++\\notepad++.exe","Skype":"C:\Program Files\Skype\Phone\Skype.exe",
          "TeamViewer":"C:\Program Files\TeamViewe\TeamViewer.exe","UltraISO":"C:\Program Files\\UltraISO\\UltraISO.exe",
          "VLC":"C:\Program Files\VideoLAN\VLC\\vlc.exe","WinRAR":"C:\Program Files\WinRAR\WinRAR.exe",
          "Drive":"C:\Program Files\Google\Drive\googledrivesync.exe","earth":"C:\Program Files\Google\Google Earth\client\googleearth.exe",
          "Picasa":"C:\Program Files\Google\Picasa3\Picasa3.exe","kindle":"C:\\Users\enlighten\AppData\Local\Amazon\Kindle\\application\Kindle.exe",
          "et":"C:\Program Files\Kingsoft\WPS Office\\10.8.0.6206\office6\et.exe","wpp":"C:\Program Files\Kingsoft\WPS Office\\10.8.0.6206\office6\wpp.exe",
          "wps":"C:\Program Files\Kingsoft\WPS Office\\10.8.0.6206\office6\wps.exe","rio":"C:\Program Files\Rovio Entertainment Ltd\Angry Birds Rio\AngryBirdsRio.exe",
          "XMP":"C:\Program Files\Thunder Network\XMP\V5.4.0.6088\Bin\XMP.exe","spotify":"C:\\Users\enlighten\AppData\Roaming\Spotify\Spotify.exe",
          "connect":"C:\Program Files\Corel\CorelDRAW Graphics Suite 2017\Connect\Connect.exe","FontManager":"C:\Program Files\Corel\CorelDRAW Graphics Suite 2017\Programs\FontManager.exe",
          "XiuXiu":"C:\Program Files\Meitu\XiuXiu\XiuXiu.exe","YoukuDesktop":"C:\Program Files\YouKu\YoukuClient\proxy\YoukuDesktop.exe",
          "DB":"C:\TC\BIN\BD.EXE","English2Marathi":"C:\Program Files\AdeptDict\FREE English-Marathi Translator\English2Marathi.exe",
          "BarahaIME":"C:\Program Files\Baraha Software\Baraha 10\BarahaIME.exe","speedcrunch":"C:\Program Files\SpeedCrunch\speedcrunch.exe",
          "icq":"C:\\Users\enlighten\AppData\Roaming\ICQ\bin\icq.exe","Sense":"C:\Program Files\Sense\Sense.exe","LineLauncher":"C:\\Users\enlighten\AppData\Local\LINE\bin\LineLauncher.exe",
          "slack":"C:\\Users\enlighten\AppData\Local\slack\slack.exe","celestia":"C:\Program Files\Celestia\celestia.exe",
          "QQ":"C:\Program Files\Tencent\QQIntl\Bin\QQ.exe","Athan":"C:\Program Files\Athan\Athan.exe",
          "Scratch":"C:\Program Files\Scratch\Scratch.exe","MovieCatalog":"C:\Program Files\Ant Movie Catalog\MovieCatalog.exe",
          "AVCFree":"C:\Program Files\Anvsoft\Any Video Converter\AVCFree.exe","devcpp":"C:\Program Files\Dev-Cpp\devcpp.exe",
          "TomTomHOME":"C:\Program Files\TomTom HOME 2\TomTomHOME.exe","photoshine":"C:\Program Files\Photoshine\photoshine.exe",
          "MagicPhoto":"C:\Program Files\Magic Photo Editor\MagicPhoto.exe","blender":"C:\Program Files\Blender Foundation\Blender\blender.exe",
          "TuneItUp":"C:\Program Files\\Nero\\Nero TuneItUp\\TuneItUp.exe","IQ Option":"C:\Program Files\IQ Option\IQ Option.exe",
          "ChartNexus":"C:\\Users\enlighten\ChartNexus\ChartNexus.exe","thinkorswim":"\thinkorswimthinkorswim.exe",
          "maltego":"C:\Program Files\Paterva\Maltego\v3.5.0\bin\maltego.exe","TrueCafe":"C:\Program Files\TrueCafe\TrueCafe.exe",
          "NestTrader":"C:\Program Files\Omnesys\\NEST3\\NestTrader.exe","BioEdit":"C:\BioEdit\BioEdit.exe",
          "geogebra":"C:\\Users\enlighten\Downloads\geogebra.exe","terminal":"C:\\Users\enlighten\AppData\Roaming\Pepperstone MetaTrader 4\terminal.exe",
          "prism":"C:\Program Files\GraphPad\Prism 7\prism.exe","PCBWiz":"C:\Program Files\\New Wave Concepts\PCB Wizard 3 Demonstration\PCBWiz.exe",
          "Mtb":"C:\Program Files\Minitab\Minitab 18\Mtb.exe","WWTExplorer":"C:\Program Files\Microsoft Research\Microsoft WorldWide Telescope\WWTExplorer.exe",
          "Graph":"C:\Program Files\Graph\Graph.exe","WorldWind":"C:\Program Files\\NASA\World Wind 1.4\WorldWind.exe",
          "Lingo17":"C:\LINGO17\Lingo17.exe","artha":"C:\Program Files\Artha\bin\artha.exe",
          "Planet0273a":"C:\Program Files\Planetarium0273a\Planet0273a.exe","Orbitron":"C:\Program Files\Orbitron\Orbitron.exe",
          "Solve Elec":"C:\Program Files\Solve Elec 2.5\Solve Elec.exe","SimSolar":"C:\Program Files\SimSolar v2.0\SimSolar.exe",
          }
AppList = app_dict.values()

PDFlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

def Log(name):
    file = open(file_abs, 'a')
    file.write(str(name)+'\n')
    file.close()



def app_select():
    app_list = []
    for i in app_dict:
        app_list.append(app_dict[i])
    list=random.sample(app_list,10)
    for i in list:
         name="app"+" "+i
         Log(name)

def photo_select():
    list=random.sample(range(1,12),5)
    for i in list:
        name="photo "+str(i)
        Log(name)


def PDF_select():
    list=random.sample(range(1,10),5)
    for i in list:
        name="pdf"+" "+str(i)
        Log(name)

def web_select(web_list):
    list=random.sample(web_list,10)
    #print(list)
    for i in list:
        name="web"+" "+i
        Log(name)

if __name__ == "__main__":
    count = 0
    f=open("/home/wei/share/domain.txt",'r')
    web_list= []
    for i in open("/home/wei/share/domain.txt"):
        i='https://www.'+f.readline()
        i = i.strip()
        web_list.append(i)

    while (count<1): # core dump 5 times
        file_abs = "/home/wei/share/sample.txt"
        web_select(web_list)
        PDF_select()
        app_select()
        photo_select()
        #os.chdir(path)
        os.system(command1)
        print ('started!!')
        time.sleep(150)
        command=command2+str(count)+'.img'
        os.system(command)
        print('dumped!!')
        os.system('VBoxManage controlvm win7 poweroff')
        time.sleep(5)
        os.rename("/home/wei/share/sample.txt", "/home/wei/share/sample" + str(count) + ".txt")
        shutil.move("/home/wei/share/sample" + str(count) + ".txt", "/home/wei/log")
        print("the" + str(count) + "th has done")
        count=count+1
