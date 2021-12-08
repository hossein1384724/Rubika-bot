import platform
import time
import os
import threading
from random import choice
from pyrubika import Bot
from json import loads
from colorama import init,Fore
from requests import get
init()
os.system('cls')

auth = "fmwyeixiiqinwanryriojvzvpfwydqgr"
Bot = Bot(auth,lang="fa-ir")
listlog = []
joke = []

global state

def updatelog(mode="info",text=""):
    if(len(listlog)>=10):
        listlog.remove(listlog[0])

    if(mode == "info"):
        listlog.append(f"{Fore.CYAN}[{Fore.YELLOW}{time.ctime()[11:19]}{Fore.CYAN}]{Fore.RESET} {Fore.CYAN}[{Fore.YELLOW}INFO{Fore.CYAN}]{Fore.RESET} : {text}")
    elif(mode == "Response"):
        listlog.append(f"{Fore.CYAN}[{Fore.YELLOW}{time.ctime()[11:19]}{Fore.CYAN}]{Fore.RESET} {Fore.CYAN}[{Fore.YELLOW}RESPONSE{Fore.CYAN}]{Fore.RESET} : {text}")
    elif(mode == "message"):
        listlog.append(f"{Fore.CYAN}[{Fore.YELLOW}{time.ctime()[11:19]}{Fore.CYAN}]{Fore.RESET} {Fore.CYAN}[{Fore.YELLOW}Message{Fore.CYAN}]{Fore.RESET} : >>> {text}")    
    elif(mode == "decrypt"):
        text = Bot.crypto.decrypt(text)
        listlog.append(f"{Fore.CYAN}[{Fore.YELLOW}{time.ctime()[11:19]}{Fore.CYAN}]{Fore.RESET} {Fore.CYAN}[{Fore.YELLOW}Decrypt{Fore.CYAN}]{Fore.RESET} : {text}")
    elif(mode == "encrypt"):
        listlog.append(f"{Fore.CYAN}[{Fore.YELLOW}{time.ctime()[11:19]}{Fore.CYAN}]{Fore.RESET} {Fore.CYAN}[{Fore.YELLOW}Encrypt{Fore.CYAN}]{Fore.RESET} : {text}")

def service():
    guid = "g0BTkrT04c9eac7ab2c1d71c71a192e0"
    updatelog(mode="info",text="The robot was successfully launched and is being serviced")
    updatelog(mode="info",text=f"The robot has set its default server to {Bot.url}")
        
    # Bot.deleteChatHistory(guid)
    # Bot.send_Massage(object_guid=guid,text="""The bot is on and the service is coming ✅""")
    def ReadingPluginWebika(id):
        answered, sleeped, retries = [], False, {}
        
        while True:
            chat_min_id = loads(Bot.crypto.decrypt(Bot.getGroupInfo(id)["data_enc"]))["data"]["chat"]["last_message_id"]  
            while True:
                try:
                    MessageUpdates = loads(Bot.crypto.decrypt(Bot.getMessagesInterval(id,chat_min_id)["data_enc"]))["data"]["messages"]
                    break
                except:
                    continue
            
            open("id.txt","w+").write(str(MessageUpdates[-1].get("message_id")))    
            
            for msg in MessageUpdates:
                if msg["type"] == "Text" and not msg["message_id"] in answered:
                    if not sleeped:
                        if(msg["text"] == "/start"):
                            Bot.send_Massage(object_guid=id,text="The bot is now on and ready to serve ✅",id=msg["message_id"])
                        if("جوک" == msg["text"]):
                            text_joke = get(url="https://api.codebazan.ir/jok/").text
                            Bot.send_Massage(object_guid=id,text=text_joke,id=msg["message_id"])
                if msg["type"] == "Event":
                    pass
                            
            answered.append(msg["message_id"])    
                    
    threading.Thread(target=ReadingPluginWebika(guid)).start()
    
     
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