
class MailBox:

    def __init__(self, name="", email="", password=""):
        if name and email and password:
            self.name = name
            self.email = email
            self.password = password
    
    def to_string(self):
        return "MailBox: "+self.name+" "+self.email
    
    def to_create(self):
        data = {
            "name": self.name,
            "email": self.email,
            "passwordPlaintext": self.password,
            "disabled": False,
            "superAdmin": False,
            "redirectTo": [],
            "referenceId": self.email
        }
        return data

    def to_patch(self,new_password):
        data = {
            "name": self.name,
            "passwordPlaintext": new_password,
            "disabled": False,
            "superAdmin": False,
            "referenceId": self.email
        }
        return data
    
    def to_update_quota(self, storageLimit, countLimit):
        data = {
            "storageLimit": storageLimit,
            "countLimit": countLimit
        }
        return data

    def from_json(self,data_json):
        self.name = data_json["name"]
        self.email = data_json["address"]
        self.disabled = data_json["disabled"]
        self.created = data_json["created"]
        self.updated = data_json["updated"]