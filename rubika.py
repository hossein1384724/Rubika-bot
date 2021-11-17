import requests
import cryptorubika
class bot:
    def __init__(self,auth,user_guid,lang="en-us",):
        self._auth=auth
        self._user_guid=user_guid
        crypto = cryptorubika.encryption(self._auth)
        if lang == "en-us":
            self._lang = requests.get("https://web.rubika.ir/assets/locales/en-us.json?v=3.2.1")
            self.lang_code="en"
        elif lang == "fa-ir":
            self._lang = requests.get("https://web.rubika.ir/assets/locales/fa-ir.json")
            self.lang_code="fa"
        self.getdcmess = requests.post("https://getdcmess.iranlms.ir/",data='{"api_version":"4","method":"getDCs","client":{"app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"fa"}}')
        data = '{"method":"getUserInfo"}'
        self.UserInfo = requests.post("https://messengerg2c39.iranlms.ir/",data={data})   
    def edit_profile(self):
        pass
    def send_Massage(self):
        pass
#{"method":"getUserInfo","input":{"user_guid":"{_user_guid}"},"client":{"app_name":"Main","app_version":"3.2.1","platform":"Web","package":"web.rubika.ir","lang_code":"{lang_code}"}}