from MailAPI import MailAPI
from MailBox import MailBox
from Parameters import Parameters
import json

param = Parameters()

api = MailAPI(param.mail_url,param.username,param.password)

def create_mailbox(username, mail, password):
    mailbox = MailBox(username, mail, password)
    response = api.create_mailbox(mailbox)
    if response.ok:
        #print(api.get_mailbox_Data(mailbox.email))
        print("Mailbox created: "+mailbox.name+" "+mailbox.email+" "+mailbox.password)
    else:
        print("Can't create account: "+mailbox.email)
        #print(response.content.decode())

def update_quota_mailbox(mail, storageLimit,countLimit):
    mailbox = MailBox("a",mail,"a")
    response = api.update_quota(mailbox, storageLimit, countLimit)
    if response.ok:
        #print(api.get_mailbox_Data(mailbox.email))
        print("Mailbox updated: "+mailbox.email+" size: "+str(storageLimit)+" count: "+str(countLimit))
    else:
        print("Can't update quota for account: "+mailbox.email)
        #print(response.content.decode())

