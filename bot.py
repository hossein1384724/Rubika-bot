from socket import *
import platform
import time
import os
import requests
import threading
import cryptorubika
import api
from colorama import init,Fore
init()
os.system('cls')

server = socket(AF_INET,SOCK_STREAM)
auth = ""
encryption = cryptorubika.encryption(auth)
bot = api.bot()
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
    data = requests.post("https://messengerg2c32.iranlms.ir/",data='{"api_version":"5","auth":"orwvobnzmrfmwqaazeyflubnhcecipnn","data_enc":"zFFCUV7Ur2TtwIcscHTZGOZ7wv9svWqKWoRcifhJJ1j1FuGJ9K0Bub8pFzLk/kQp+IxRabd7AxD1kX8nnAXhVyH+FSB8paM3JPvDvPa0mwy1ezYMq6jtgpjJsLHp7p6whajIDremB0ZUYH1DEXmyigGjF/2T0jTesgXcUDE/FLp4kxO9lGYM1cyq9wH9XBdPDnC7l3qpv1qtCOPqf8HYEA=="}')
    updatelog(mode="info",text=encryption.decrypt('orwvobnzmrfmwqaazeyflubnhcecipnn","data_enc":"zFFCUV7Ur2TtwIcscHTZGOZ7wv9svWqKWoRcifhJJ1j1FuGJ9K0Bub8pFzLk/kQp+IxRabd7AxD1kX8nnAXhVyH+FSB8paM3JPvDvPa0mwy1ezYMq6jtgpjJsLHp7p6whajIDremB0ZUYH1DEXmyigGjF/2T0jTesgXcUDE/FLp4kxO9lGYM1cyq9wH9XBdPDnC7l3qpv1qtCOPqf8HYEA=='))
    updatelog(mode="Response",text=encryption.decrypt(data.text.split('"')[3]))

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