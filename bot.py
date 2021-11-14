from socket import *
import platform
import time
import os
import requests
import random
import threading
import cryptorubika
from colorama import init,Fore
init()
os.system('cls')

server = socket(AF_INET,SOCK_STREAM)
auth = "orwvobnzmrfmwqaazeyflubnhcecipnn"
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
    getdcmess = requests.post("https://getdcmess.iranlms.ir")
    updatelog(mode="info",text="Requests Send and get successfully")
    updatelog(mode="Response",text=getdcmess)
    data = encryption.decrypt("ix83LfTh54sOwcpZkmwkR9WxiDJMnjBb1q3lx7ulolXCMhZwxWKzwu8awTWc8jDrYSUvKfuvX2K2K2K2W0rCOP0w14C+PjkoqIyb3yRE4XaiX1oXMiPcMDjKcRakG8lhojVnBUCsn4rV4vfyPndCCd7VnL9t91VOTEISHvFvCx60arATlcwYKl2gbZK8JoVrc0ZKB1zU/eRYrECwhTuK8UeAmYPquD7AG65tmoRdOM6XrWQo/akkcRi12RnCkFD2ppc4VjsMDzSoVz7XIR39Bz+iQWSgEd2we36hx+xedbI=")
    updatelog(mode="Response",text=data)
    data = encryption.decrypt("8FuSvgfms4AhmzoL02ks1B03BZRLf6h8Xce4Is0J17EiHFh3DFKGUovLH2flz18bOinilgIagnZoy9H5Rmd1bkTmJ27D11pHtMlKcB1DkFbC259G/8VmlpSi+Ja80MD3pj9GHcANweXCwNqlzh+G2B56lhsJpIsj9iyfxF3TAU3xqLUbgVYl5zL28W484426wOWkFskPHwFsrESHg4Cid+PNPuNaR1AsXsjgO5Ake5sEsceMUL3pFcRaam+iGR7A/pwIjnBMVEPpClJAedXb+plTzZ+guv7S7tv6NBnz/7oQDedQQtwuGmElo6eyZaPc")
    updatelog(mode="Response",text=data)

def ui():
    while True:
        print(f""+Fore.CYAN+"Rubika-bot"+Fore.RESET+" by "+Fore.CYAN+"web.rubika.ir "+Fore.RESET+"(Ctrl+C to quit)\n")
        print(f""+Fore.GREEN+"Session Status\t\t\t\t\tonline"+Fore.RESET)
        print(f"Account\t\t\t\t\t\t{platform.uname()[1]} (Plan: Full)")
        print(f"Region\t\t\t\t\t\t{time.ctime()}")
        print(f"Auth Account\t\t\t\t\t{auth}\n")
        print(f"Status Service\t\t\t\t\t"+Fore.GREEN+"Hello World"+Fore.RESET+"\n")
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