from socket import *
import platform
import time
import os
import requests
import threading
import cryptorubika
import rubika
from colorama import init,Fore
init()
os.system('cls')

server = socket(AF_INET,SOCK_STREAM)
auth = "orwvobnzmrfmwqaazeyflubnhcecipnn"
api = rubika.bot(auth,user_guid="u0CKH7902c3b29888c6cc82cd328a964",lang="en-us")
encryption = cryptorubika.encryption(auth)
listlog = []
server.connect(("web.rubika.ir",443))

def updatelog(mode="info",text=""):
    if(len(listlog)>=10):
        listlog.remove(listlog[0])
    if(mode == "info"):
        listlog.append(f"{Fore.CYAN}[{Fore.YELLOW}info{Fore.CYAN}]{Fore.RESET} : {text}")
    elif(mode == "Response"):
        listlog.append(f"{Fore.CYAN}[{Fore.YELLOW}Response{Fore.CYAN}]{Fore.RESET} : {text}")

def service():
    updatelog(mode="info",text="Starting bot rubika")
    updatelog(mode="info",text=f"Lang Rubika For {api._lang}")
    updatelog(mode="Response",text=f"{api.UserInfo.text}")

def ui():
    while True:
        print(f""+Fore.CYAN+"Rubika-bot"+Fore.RESET+" by "+Fore.CYAN+"web.rubika.ir "+Fore.RESET+"(Ctrl+C to quit)\n")
        print(f""+Fore.GREEN+"Session Status\t\t\t\t\tonline"+Fore.RESET)
        print(f"Account\t\t\t\t\t\t{platform.uname()[1]} (Plan: Full)")
        print(f"Region\t\t\t\t\t\t{time.ctime()}")
        print(f"Auth Account\t\t\t\t\t{auth}\n")
        print(f"Status Service\t\t\t\t\t"+Fore.GREEN+"Hello_World"+" Set_Time"+Fore.RESET+"\n")
        print(f"LOOGER BOT\n----------")
        
        for text in listlog:
            print(text)

        time.sleep(1)
        os.system('cls')
try:
    threading.Thread(target=service).start()
    threading.Thread(target=ui).start()
except KeyboardInterrupt:
    exit()