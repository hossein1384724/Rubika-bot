from requests import post,get
from random import randint
from json import loads,dumps
import asyncio,base64,glob,math,urllib3,os,pathlib,random,sys,concurrent.futures,time
from tqdm import tqdm
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class encryption:
    def __init__(self, auth):
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex('00000000000000000000000000000000')

    def replaceCharAt(self, e, t, i):
        return e[0:t] + i + e[t + len(i):]

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while s < len(n):
            e = n[s]
            if e >= '0' and e <= '9':
                t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))
                n = self.replaceCharAt(n, s, t)
            else:
                t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))
                n = self.replaceCharAt(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        raw = pad(text.encode('utf-8'),AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = aes.encrypt(raw)
        result = base64.b64encode(enc).decode('UTF-8')
        return result

    def decrypt(self, text):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = aes.decrypt(base64.urlsafe_b64decode(text.encode('UTF-8')))
        result = unpad(dec, AES.block_size).decode('UTF-8')
        return result
    
class Bot:
    def __init__(self,auth,lang="en-us",):
        self.auth = auth
        self.crypto = encryption(self.auth)

        # if lang == "en-us":
        #     self.lang = get("https://web.rubika.ir/assets/locales/en-us.json?v=3.2.1").json()
        #     self.lang_code="en"
        # elif lang == "fa-ir":
        #     self.lang = get("https://web.rubika.ir/assets/locales/fa-ir.json").json()
        #     self.lang_code="fa"
        
        self.lang_code = "fa"
            
        data_getdcmess = {
            "api_version":"4",
            "method":"getDCs",
            "client":{"app_name":"Main",
                      "app_version":"3.2.1",
                      "platform":"Web",
                      "package":"web.rubika.ir",
                      "lang_code":self.lang_code
            }
        }
        self.url = []
        self.getdcmess = loads(post("https://getdcmess.iranlms.ir/",json=data_getdcmess).text)
        for server in self.getdcmess["data"]["default_api_urls"]:
            self.url.append(server)
        self.url = random.choice(self.url)

    def req(self,data):
        r = post(self.url,json=data).json() 
        
        return r

    def encreq(self,data):
        auth = self.auth
        data=data.replace(']','}')
        data=data.replace('[','{')
        data=data.replace(')',']')
        data=data.replace('(','[')
        json = {
            "api_version" : "5",
            "auth" : auth,
            "data_enc" : self.crypto.encrypt(str(data))
        }
        return self.req(json)

    def getChatAds(self): 
        data_getChatAds=f'["method":"getChatAds","input":["state":"{1637820520}"],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_getChatAds)
        return result
    
    def edit_profile(self):
        pass
    
    def send_Massage(self,object_guid,text,id=None):
        if (id == None):
            data_send = f'["method":"sendMessage","input":["object_guid":"{object_guid}","rnd":{random.randint(10000,99999)},"text":"{text}",],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        else:   
            data_send = f'["method":"sendMessage","input":["object_guid":"{object_guid}","rnd":{random.randint(10000,99999)},"text":"{text}","reply_to_message_id":"{id}"],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]' 
        result = self.encreq(data_send)
        return result
    
    def getGroupInfo(self,object_guid):
        data_send = f'["method":"getGroupInfo","input":["group_guid":"{object_guid}"],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_send)
        return result
    
    def getChatsUpdates(self):
        data_send = f'["method":"getChatsUpdates","input":["state":{1637990000}],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_send)
        return result
    
    def getMessagesInterval(self,object_guid,min_id):
        # middle_message_id = loads(self.crypto.decrypt(self.getGroupInfo(object_guid=object_guid)["data_enc"]))["data"]["chat"]["last_seen_my_mid"]
        data_send = f'["method":"getMessagesInterval","input":["object_guid":"{object_guid}","middle_message_id":{min_id}],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_send)
        return result
    
    def getAbsObjects(self,array_guid):
        data_send = f'["method":"getAbsObjects","input":["objects_guids":("u0CMDpx0babf04c1cdfc80841cbae1f8","u0D1i5Y07ab7b89b8d4dc9c7aad8c3a4","u0CAoW902ecf8599e454a7aa468c7533","u0Ce7US0f09a7c2c371888b7379e52e0","u0CmvbW0b2d95e66858bec4649a5f3d9","u0CMoQl02f2b8a7cf5669f18d956f76c")],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_send)
        return result
    
    def getMessagesByID(self):
        data_send = f'["method":"getMessagesByID","input":["object_guid":"g0BAdlj01dadd47124a3d60530559","message_ids":("179185592292559","179133563530559","179139568705559","179185592047559")],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"fa"]]'
        result = self.encreq(data_send)
        return result
    
    def get_Message(self):
        pass

    def getMyStickerSets(self):
        data_send = f'["method":"getMyStickerSets","input":[],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_send)
        return result
    
    def getMessagesUpdates(self,object_guid,state):
        data_send = f'["method":"getMessagesUpdates","input":["object_guid":"{object_guid}","state":"{state}"],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_send)
        return result
    
    def seenChats(self,object_guid):
        data_send = f'["method":"seenChats","input":["seen_list":["{object_guid}":"179238612685559"]],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_send)
        return result
    
    def deleteChatHistory(self,object_guid):
        last_message = loads(self.crypto.decrypt(self.getGroupInfo(object_guid=object_guid)["data_enc"]))["data"]["chat"]["last_message"]["message_id"]
        data_send = f'["method":"deleteChatHistory","input":["object_guid":"{object_guid}","last_message_id":"{last_message}"],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_send)
        return result
    
    def updated_messages(self):
        data_send = f'["status":"OK","status_det":"OK","data":["updated_messages":(),"new_state":1638603339,"status":"OK"]]'
        result = self.encreq(data_send)
        return result
    
    def addGroupMembers(self,group_guid,member_guids):
        data_send = f'["method":"addGroupMembers","input":["group_guid":"{group_guid}","member_guids":("{member_guids}")],"client":["app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{self.lang_code}"]]'
        result = self.encreq(data_send)
        return result
    
if __name__ == "__main__":
    print("your example code goes here")  