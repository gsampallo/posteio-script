from base64 import encode
from urllib.parse import urlencode
from MailBox import MailBox
import requests
from requests.auth import HTTPBasicAuth
import json


class MailAPI:

    def __init__(self,mail_url,username,password):
        self.mail_url = mail_url
        self.username = username
        self.password = password


    def getData(self,request_url):
        data = requests.get(request_url,auth=HTTPBasicAuth(self.username,self.password))
        if data.ok:
            return json.loads(data.content)
        else:
            return "Error en la peticion"


    def get_mailbox_Data(self,mail_box):
        url_mailbox = self.mail_url+"/admin/api/v1/boxes/"+mail_box
        return self.getData(url_mailbox)


    def post(self,url,data):
        headers = {"Content-Type": "application/json "}
        response = requests.post(url,data=data,headers=headers,auth=HTTPBasicAuth(self.username,self.password))
        return response

    def patch(self,url,data):
        headers = {"Content-Type": "application/json "}
        response = requests.patch(url,data=data,headers=headers,auth=HTTPBasicAuth(self.username,self.password))
        return response

    def create_mailbox(self,mailbox:MailBox):
        url_mailbox = self.mail_url+"/admin/api/v1/boxes"
        data_json = json.dumps(mailbox.to_create())        
        return self.post(url_mailbox,data_json)

    
    def patch_mailbox(self, mailbox:MailBox, new_password):
        url_mailbox = self.mail_url+"/admin/api/v1/boxes/"+mailbox.email
        data_json = json.dumps(mailbox.patch_json(new_password))
        headers = {"Content-Type": "application/json "}
        return self.patch(url_mailbox,data_json)


    def update_quota(self, mailbox:MailBox, storageLimit, countLimit):
        url_mailbox = self.mail_url+"/admin/api/v1/boxes/{}/quota".format(urllib.parse.quote(mailbox.email))
        data_json = json.dumps(mailbox.to_update_quota(storageLimit, countLimit))
        return self.patch(url_mailbox,data_json)
    
