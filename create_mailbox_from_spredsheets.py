import io,os
import sys
import argparse
import xlrd
from MailAPI import MailAPI
import WrapperMailApi

def generate_password():
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

def create_mails(filename):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)

    for rx in range(1,sheet.nrows):
        
        name = sheet.cell_value(rx, 0)
        email = sheet.cell_value(rx, 1)
        size = sheet.cell_value(rx, 2)
        
        password = generate_password()
        #WrapperMailApi.create_mailbox(name, email, password)
        print(name, email, password)
        #WrapperMailApi.update_quota_mailbox(email,size,0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script allow to create a list of mailbox from a spreadsheet')
    parser.add_argument("filename", help="The spreadsheet file")
    
    args = parser.parse_args()

    if not os.path.isfile(args.filename):
        print("File not found: "+args.filename)
        sys.exit(1)

    create_mails(args.filename)
