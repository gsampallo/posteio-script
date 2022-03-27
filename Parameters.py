import sys
import json,io
import os,os.path

class Parameters:

    __file_config = "configuration.json"

    def __init__(self) :
        if os.path.isfile(self.__file_config):
            self.load_parameters()
        else:
            print("There is not configuration file")
            sys.exit(1)
    

    def load_parameters(self):
        with open(self.__file_config) as json_file:
            data = json.load(json_file)
            self.mail_url = data["mail_url"]
            self.username = data["username"]
            self.password = data["password"]

    
