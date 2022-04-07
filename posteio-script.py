import io,os
import sys
import argparse
import xlrd
import xlwt
from MailAPI import MailAPI
from MailBox import MailBox
from Word import Words
from Parameters import Parameters
from datetime import datetime

class PosteioScript:

    def __init__(self,filename,action):
        self.words = Words('palabras.txt')
        param = Parameters()
        self.api = MailAPI(param.mail_url,param.username,param.password) 

        self.wb = xlwt.Workbook()
        self.ws = self.wb.add_sheet("Mailbox")
        self.ws.write(0, 0, "Name")
        self.ws.write(0, 1, "Email")
        self.ws.write(0, 2, "Storage Limit")
        self.ws.write(0, 3, "Password")

        if action == "new":
            print("create")
            self.create_mails(filename)

        if action == "quota":
            print("update")
            self.update_mails_qouta(filename)

        now = datetime.now()
        output = "mailboxs_"+f'{now:%Y%m%d_%H%M%S}.xls'

        self.wb.save(output)

    def create_mailbox(self,username, mail, password):
        mailbox = MailBox(username, mail, password)
        return self.api.create_mailbox(mailbox)

    def update_quota_mailbox(self,mail, storageLimit,countLimit):
        mailbox = MailBox("a",mail,"a")
        return self.api.update_quota(mailbox, storageLimit, countLimit)

    def update_mails_qouta(self,filename):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)

        for rx in range(1,sheet.nrows):
            name = sheet.cell_value(rx, 0)
            email = sheet.cell_value(rx, 1)
            size = str(sheet.cell_value(rx, 2))
            
            response_quota = self.update_quota_mailbox(email, size, 0)
            if response_quota.ok:
                self.ws.write(rx, 0, name)
                self.ws.write(rx, 1, email)
                self.ws.write(rx, 2, size)
                self.ws.write(rx, 3,"Mailbox updated: "+email+" size: "+str(size)+" count: 0")
                print("Mailbox updated: "+email+" size: "+str(size)+" count: 0")
            else:
                self.ws.write(rx, 0, name)
                self.ws.write(rx, 1, email)
                self.ws.write(rx, 2, size)
                self.ws.write(rx, 3,"Can't update account: "+email)
                print("Can't update account: "+email)
                print(response_quota.content.decode())


    def create_mails(self,filename):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)

        for rx in range(1,sheet.nrows):
            
            name = sheet.cell_value(rx, 0)
            email = sheet.cell_value(rx, 1)
            size = sheet.cell_value(rx, 2)
            
            password = self.words.get_password(2)
            response = self.create_mailbox(name, email, password)
            if response.ok:
                self.ws.write(rx, 0, name)
                self.ws.write(rx, 1, email)
                self.ws.write(rx, 2, size)
                self.ws.write(rx, 3, password)
                print("Mailbox created: "+name+" "+email+" "+password)
                response_quota = self.update_quota_mailbox(email, size, 0)
                if response_quota.ok:
                    print("Mailbox updated: "+email+" size: "+str(size)+" count: 0")
            else:
                self.ws.write(rx, 0, name)
                self.ws.write(rx, 1, email)
                self.ws.write(rx, 2, size)
                self.ws.write(rx, 3, "Can't create account: "+email)
                print("Can't create account: "+email)
                print(response.content.decode())



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script allow to create a list of mailbox from a spreadsheet')
    
    parser.add_argument("action", help="Use 'new' to create a list of mailboxs or Use 'quota' to update the quota of a list of mailboxs")
    parser.add_argument("filename", help="The spreadsheet file")
    
    args = parser.parse_args()

    if not args.action:
        print("Error: create or update is required")
        sys.exit(1)

    if not os.path.isfile(args.filename):
        print("File not found: "+args.filename)
        sys.exit(1)

    script = PosteioScript(args.filename,args.action)

